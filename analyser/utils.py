import json
import base64
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from matplotlib.figure import Figure

def analyze_search_history(data):
    """Process the search history file and create visualization"""
    # Load JSON file
    # with open(file_path, "r", encoding="utf-8") as f:
    #     data = json.load(f)
    
    # Convert to DataFrame and preprocess
    df = pd.DataFrame(data)[['time', 'header', 'title', 'titleUrl']]
    df['time'] = pd.to_datetime(df['time'], format='mixed')
    
    # Filter date range (UTC)
    start_date = pd.to_datetime('2020-12-01').tz_localize('UTC')
    end_date = pd.to_datetime('2024-11-30').tz_localize('UTC')
    df = df[(df['time'] >= start_date) & (df['time'] <= end_date)].copy()
    df['month_year'] = df['time'].dt.strftime('%m-%Y')
    
    # Total search volume data
    all_months = pd.date_range('2020-12-01', '2024-11-01', freq='MS').strftime('%m-%Y')
    search_volume_df = (
        df.groupby('month_year')
        .size()
        .reset_index(name='search_volume')
    )
    search_volume_df = (
        pd.DataFrame({'month_year': all_months})
        .merge(search_volume_df, on='month_year', how='left')
    )
    search_volume_df['search_volume'] = search_volume_df['search_volume'].fillna(0).astype(int)
    search_volume_df['datetime'] = pd.to_datetime(search_volume_df['month_year'], format='%m-%Y')
    search_volume_df = search_volume_df.sort_values('datetime')
    
    # Find first ChatGPT search
    chatgpt_mask = (
        df['header'].str.contains('chatgpt', case=False, na=False) |
        df['title'].str.contains('chatgpt', case=False, na=False) |
        df['titleUrl'].str.contains('chatgpt', case=False, na=False)
    )
    
    try:
        first_chatgpt_date = df[chatgpt_mask]['time'].min()
        first_chatgpt_month = pd.to_datetime(first_chatgpt_date.strftime('%Y-%m-01'))
    except:
        # If no ChatGPT search found, use ChatGPT launch date as default
        first_chatgpt_month = pd.to_datetime('2023-01-01')
    
    chatgpt_launch = pd.to_datetime('2022-11-01')
    
    # GenAI keywords and monthly counts
    genai_keywords = {'ChatGPT': 'chatgpt', 'Gemini': 'gemini', 'Claude': 'claude'}
    genai_df = pd.DataFrame({'month_year': all_months})
    
    for label, kw in genai_keywords.items():
        m = (
            df['header'].str.contains(kw, case=False, na=False) |
            df['title'].str.contains(kw, case=False, na=False) |
            df['titleUrl'].str.contains(kw, case=False, na=False)
        )
        tmp = df[m].groupby('month_year').size().reset_index(name=label)
        genai_df = genai_df.merge(tmp, on='month_year', how='left')
    
    for label in genai_keywords:
        genai_df[label] = genai_df[label].fillna(0).astype(int)
    
    genai_df['datetime'] = pd.to_datetime(genai_df['month_year'], format='%m-%Y')
    genai_df = genai_df.sort_values('datetime')
    genai_df['tot_count'] = genai_df['ChatGPT'] + genai_df['Gemini'] + genai_df['Claude']
    genai_df = genai_df[['month_year', 'tot_count']]
    
    search_volume_df['search_volume'] = search_volume_df['search_volume'] - genai_df['tot_count']
    
    # Create plot
    plt.figure(figsize=(12, 5))
    plt.fill_between(search_volume_df['datetime'], search_volume_df['search_volume'], alpha=0.5)
    plt.plot(search_volume_df['datetime'], search_volume_df['search_volume'], linewidth=2, label='Search Volume')
    plt.axvline(chatgpt_launch, color='red', linestyle='--', linewidth=2, label='ChatGPT Launch')
    plt.axvline(first_chatgpt_month, color='green', linestyle='--', linewidth=2, label='Your 1st ChatGPT Search')
    
    plt.title('Total Search Volume Over Time', fontsize=16)
    plt.xlabel('Month-Year', fontsize=12)
    plt.ylabel('Search Count', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.tight_layout()
    
    # Save plot to base64 string
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_data = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    
    return plot_data

def analyze_chrome_history(data):
    """Process the chrome history file and create visualization"""
    # Load JSON file
    # with open(file_path, "r", encoding="utf-8") as f:
    #     data = json.load(f)
    
    # Convert to DataFrame and preprocess
    df = pd.DataFrame(data)[['time', 'header', 'title', 'titleUrl']]
    df['time'] = pd.to_datetime(df['time'], format='mixed')
    
    # Filter date range
    start_date = pd.to_datetime('2020-12-01').tz_localize('UTC')
    end_date = pd.to_datetime('2024-11-30').tz_localize('UTC')
    df = df[(df['time'] >= start_date) & (df['time'] <= end_date)].copy()
    df['month_year'] = df['time'].dt.strftime('%m-%Y')
    
    # Find first ChatGPT visit
    chatgpt_mask = (
        df['header'].str.contains('chatgpt', case=False, na=False) |
        df['title'].str.contains('chatgpt', case=False, na=False) |
        df['titleUrl'].str.contains('chatgpt', case=False, na=False)
    )
    
    try:
        first_chatgpt_visit_date = df[chatgpt_mask]['time'].min()
        first_chatgpt_visit_month = pd.to_datetime(first_chatgpt_visit_date.strftime('%Y-%m-01'))
    except:
        # If no ChatGPT visit found, use ChatGPT launch date as default
        first_chatgpt_visit_month = pd.to_datetime('2023-01-01')
    
    chatgpt_launch = pd.to_datetime('2022-11-01')
    
    # GenAI keywords and counts
    genai_keywords = {
        'ChatGPT': 'chatgpt',
        'Gemini': 'gemini',
        'Claude': 'claude'
    }
    
    all_months = pd.date_range(start='2020-12-01', end='2024-11-01', freq='MS').strftime('%m-%Y')
    genai_df = pd.DataFrame({'month_year': all_months})
    for label, keyword in genai_keywords.items():
        mask = (
            df['header'].str.contains(keyword, case=False, na=False) |
            df['title'].str.contains(keyword, case=False, na=False) |
            df['titleUrl'].str.contains(keyword, case=False, na=False)
        )
        temp_df = df[mask].groupby('month_year').size().reset_index(name=label)
        genai_df = genai_df.merge(temp_df, on='month_year', how='left')
    
    for label in genai_keywords.keys():
        genai_df[label] = genai_df[label].fillna(0).astype(int)
    
    genai_df['datetime'] = pd.to_datetime(genai_df['month_year'], format='%m-%Y')
    
    # Create plot
    plt.figure(figsize=(12, 5))
    for label in genai_keywords.keys():
        plt.plot(genai_df['datetime'], genai_df[label], linewidth=2, label=label)
    
    plt.axvline(first_chatgpt_visit_month, color='green', linestyle='--', label='First ChatGPT Visit')
    plt.axvline(chatgpt_launch, color='red', linestyle='--', label='ChatGPT Launch')
    plt.title('ChatGPT Visits Over Time', fontsize=16)
    plt.xlabel('Time (Month-Year)', fontsize=12)
    plt.ylabel('Number of Mentions', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.tight_layout()
    
    # Save plot to base64 string
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_data = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    
    return plot_data
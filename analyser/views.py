import os
import base64
from io import BytesIO
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
# from .models import UploadedFile
from .utils import (
    analyze_search_history, 
    analyze_chrome_history
)

def index(request):
    """View for the home page with file upload form"""
    if request.method == 'POST':
        # Check if both files are provided
        if 'search_history' in request.FILES and 'chrome_history' in request.FILES:
            search_file = request.FILES['search_history']
            chrome_file = request.FILES['chrome_history']
            
            # Read file contents directly
            search_data = json.loads(search_file.read().decode('utf-8'))
            chrome_data = json.loads(chrome_file.read().decode('utf-8'))
            
            # Process data and generate plots
            search_plot = analyze_search_history(search_data)
            chrome_plot = analyze_chrome_history(chrome_data)
            
            # Send plots to results page
            context = {
                'search_plot': search_plot,
                'chrome_plot': chrome_plot
            }
            return render(request, 'analyser/results.html', context)
        else:
            messages.error(request, "Please upload both Search History and Chrome History files")
    
    return render(request, 'analyser/index.html')

def results(request):
    """View for displaying analysis results"""
    # uploaded_files_id = request.session.get('uploaded_files_id')
    
    # if not uploaded_files_id:
    #     messages.error(request, "No files found for analysis. Please upload files first.")
    #     return redirect('analyser:index')
    
    # try:
    #     uploaded_files = UploadedFile.objects.get(pk=uploaded_files_id)
    # except UploadedFile.DoesNotExist:
    #     messages.error(request, "Files not found. Please upload again.")
    #     return redirect('analyser:index')

    # Get file paths
    search_data = json.loads(request.FILES['search_history'].read().decode('utf-8'))
    chrome_data = json.loads(request.FILES['chrome_history'].read().decode('utf-8'))
    
    # Generate plots
    search_plot = analyze_search_history(search_data)
    chrome_plot = analyze_chrome_history(chrome_data)
    
    context = {
        'search_plot': search_plot,
        'chrome_plot': chrome_plot
    }
    
    return render(request, 'analyser/results.html', context)
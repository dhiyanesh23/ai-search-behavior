# AI Search Behavior Analysis

## Prerequisites

Before you begin, ensure you have the necessary Google Activity data:

1.  **Visit Google My Activity:** Go to [https://myactivity.google.com/myactivity](https://myactivity.google.com/myactivity).
2.  **Check Web & App Activity:**
    * Verify that "Web & App Activity" is turned on. If it's off, no data is being stored, and the graph analysis will not work as expected.
3.  **Filter Activity Data:**
    * Select "Filter by date & product".
    * Set the date range from January 1, 2020, to January 1, 2023.
    * Choose "Chrome" and "Search" as the products.
4.  **Confirm Data Availability:**
    * Check if there is data within the specified timeframe. If you find data, you can proceed to the next steps.  If there is no data, the graph will not contain information.

## Download Google Activity Data

Follow these steps to download your Google Activity data:

1.  **Go to Google Takeout:** Visit [https://takeout.google.com/](https://takeout.google.com/).
2.  **Create a New Export:**
    * Click "Deselect all" to uncheck all data options.
3.  **Select My Activity:**
    * Scroll down and select "My Activity."
4.  **Configure My Activity Export:**
    * Click on "Multiple formats."
    * Change the format of "Activity records" to "JSON."
    * Click on "All activity data included."
    * Click "Deselect all"
    * Choose only "Chrome" and "Search."
    * Click "OK".
5.  **Proceed to Next Step:** Click "Next step" to configure the export details.
6.  **Choose Export Settings:**
    * You don't need to change any settings on this page.  The defaults are fine.
7.  **Create Export:** Click "Create export."
8.  **Download the Report:**
    * Wait for the report to be generated (this may take 3-5 minutes).
    * Once ready, the report will be available for download on the same page and you will also receive a download link via email.
    * Download the report and extract (unzip) the contents.

## Setup and Installation

Follow these steps to set up the project:

1.  **Create a Folder:** Create a new folder on your local machine to store the project.
2.  **Open Git Bash:** Open Git Bash (or your preferred terminal) inside the newly created folder.
3.  **Clone the Repository:**
    ```bash
    git clone https://github.com/dhiyanesh23/ai-search-behavior.git
    ```
4.  **Create a Virtual Environment (Optional but Recommended):**
    ```bash
    python -m venv venv
    ```
5.  **Activate the Virtual Environment (Optional):**
    * For Windows (cmd):
        ```bash
        .\venv\Scripts\activate
        ```
    * For Windows (git bash):
        ```bash
        source venv/Scripts/activate
        ```
6.  **Navigate to the Project Directory:**
    ```bash
    cd ai-search-behavior
    ```
7.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
8.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```
9.  **Upload Your Data:**
    * Open your web browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
    * Upload the files you downloaded from Google Takeout.
    * **Note:** The analysis is performed locally. You can even do this without an internet connection.

## Contact

If you have any questions or need assistance, feel free to reach out.

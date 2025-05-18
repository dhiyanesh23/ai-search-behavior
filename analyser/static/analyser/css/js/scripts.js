// Custom JavaScript for the Search Vs AI application

// Display the name of the selected file in the file input label
document.addEventListener('DOMContentLoaded', function() {
    const searchFileInput = document.getElementById('search_history');
    const chromeFileInput = document.getElementById('chrome_history');
    
    if (searchFileInput) {
        searchFileInput.addEventListener('change', function() {
            const fileName = this.files[0]?.name || 'No file chosen';
            const label = this.nextElementSibling;
            if (label) {
                label.textContent = fileName;
            }
        });
    }
    
    if (chromeFileInput) {
        chromeFileInput.addEventListener('change', function() {
            const fileName = this.files[0]?.name || 'No file chosen';
            const label = this.nextElementSibling;
            if (label) {
                label.textContent = fileName;
            }
        });
    }
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const closeButton = alert.querySelector('.btn-close');
            if (closeButton) {
                closeButton.click();
            }
        }, 5000);
    });
});
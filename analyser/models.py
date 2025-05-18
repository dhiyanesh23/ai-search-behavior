from django.db import models

# class UploadedFile(models.Model):
#     """Model to store uploaded history files"""
#     search_history = models.FileField(upload_to='history_files/')
#     chrome_history = models.FileField(upload_to='history_files/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"Files uploaded at {self.uploaded_at}"
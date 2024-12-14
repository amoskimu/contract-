from django.db import models

class ServiceRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    service_type = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

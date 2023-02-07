from django.db import models

class Note(models.Model):
    name = models.CharField(max_length= 256, primary_key= True)
    description = models.TextField(null=True, blank= True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

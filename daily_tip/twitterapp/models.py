from django.db import models

# Create your models here.

class TwitterAuthModel(models.Model):
    """
    Twitter Credentials for Authentication
    """

    screen_name = models.CharField(max_length=255, null=False)
    access_token = models.CharField(max_length=255)
    access_token_secret = models.CharField(max_length=255)
    is_authenticated = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.screen_name)
    

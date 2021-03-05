from django.db import models

# Create your models here.
class Tips(models.Model):
    """
    Tips Model
    (tweets)
    """
    id = models.BigIntegerField(primary_key=True, blank=False, unique=True)
    tip = models.TextField(blank=False)
    timestamp = models.DateTimeField(blank=False)
    author = models.CharField(blank=False, unique=False, max_length=255)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.id)

class Links(models.Model):
    """
    Links from tips
    """
    tip = models.ForeignKey(Tips, on_delete=models.CASCADE)
    link = models.TextField(unique=True)








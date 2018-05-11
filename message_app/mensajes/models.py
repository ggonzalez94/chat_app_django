from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Mensajes(models.Model):
    message = models.CharField(max_length=255, blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User,related_name='sender',on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name='receiver',on_delete=models.CASCADE)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.message)

    class Meta:
        ordering = ('date_sent',)

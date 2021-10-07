from django.db import models
from datetime import datetime


class Mail(models.Model):
    name = models.CharField(max_length=35, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    message_text = models.TextField(verbose_name='Message')
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return str(self.id) + ' ' + format(self.message_text)

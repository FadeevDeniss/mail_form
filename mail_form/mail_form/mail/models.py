from django.db import models


class Mail(models.Model):
    name = models.CharField(max_length=35, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    message_text = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.message_text

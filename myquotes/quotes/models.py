# файл models.py

from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.CharField(max_length=255)
    born_location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.fullname

class Quote(models.Model):
    author = models.ForeignKey(Author, related_name='quotes', on_delete=models.CASCADE)
    quote = models.TextField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.quote[:50]

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    message_sent = models.BooleanField(default=False)
    preferred_contact_method = models.CharField(max_length=255, choices=[('email', 'Email'), ('sms', 'SMS')])

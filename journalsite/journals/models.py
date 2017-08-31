from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class User(models.Model):
    email_text = models.CharField('email', max_length=200)
    password_hash = models.CharField('password', max_length=200)
    def __str__(self):
        return self.email_text
    
@python_2_unicode_compatible
class Journal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField('date created')
    modified_date = models.DateTimeField('date modified')
    name_text = models.CharField('journal name', max_length=200)
    description_text = models.CharField('journal description', max_length=200)
    def __str__(self):
        return self.name_text
    
@python_2_unicode_compatible
class EntryLog(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    
@python_2_unicode_compatible
class Entry(models.Model):
    entry_log = models.ForeignKey(EntryLog, on_delete=models.CASCADE)
    title_text = models.CharField('entry title', max_length=200)
    body_text = models.CharField('entry body', max_length=200)
    published_date = models.DateTimeField('published date')
    hidden_boolean = models.BooleanField('hidden', default=False)
    deleted_boolean = models.BooleanField('deleted', default=False)
    def __str__(self):
        return self.title_text

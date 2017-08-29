from django.contrib import admin

from .models import Journal, User, Entry, EntryLog

admin.site.register(User)
admin.site.register(EntryLog)
admin.site.register(Entry)
admin.site.register(Journal)

# Register your models here.

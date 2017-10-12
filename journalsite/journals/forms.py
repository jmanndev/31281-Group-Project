from django import forms
from django.forms import Textarea, TextInput

from .models import Journal, Entry
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username","email","password1","password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = "Username"
            self.fields["email"].label = "Email address"


class JournalCreateForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ("name_text", "description_text")

        widgets = {
            'name_text':forms.TextInput(attrs={'class':'textinputclass'}),
            'description_text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

        }

class JournalEditForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ("name_text", "description_text")

        widgets = {
            'name_text':forms.TextInput(attrs={'class':'textinputclass',"readonly":True}),
            'description_text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

        }



class EntryCreateForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ("title_text", "body_text")

        widgets = {
            'title_text':forms.TextInput(attrs={'class':'textinputclass'}),
            'body_text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

        }

class EntryCopyForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ("journal", "title_text", "body_text", "created_date", "hidden_boolean", "deleted_boolean", "orginal_entry")

class EntryUpdateForm(forms.ModelForm):


    class Meta:
        model = Entry
        fields = ("title_text", "body_text","created_date","hidden_boolean","deleted_boolean")
        widgets = {

            # 'journal':forms.Select(attrs={"disabled":True}),
            'title_text':forms.TextInput(attrs={'class':'textinputclass', "readonly":True}),
            'body_text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'created_date':TextInput(attrs={'readonly':True}),
            # 'orginal_id': forms.IntegerField(attrs={"disabled": True}),


        }

class EntryDetailForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ("title_text", "body_text","created_date","hidden_boolean","deleted_boolean")
        widgets = {

            # 'journal':forms.Select(attrs={"disabled":True}),
            'title_text':forms.TextInput(attrs={'class':'textinputclass', "readonly":True}),
            'body_text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'created_date':TextInput(attrs={'readonly':True}),
            # 'orginal_id': forms.IntegerField(attrs={"disabled": True}),


        }





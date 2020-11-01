from django import forms


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name',)
    '''list = Group.objects.all()
    temp = []
    for group in list:
        select = (group.slug, group.title)
        temp.append(select)
    OPTIONS = tuple(
        temp,
    )'''
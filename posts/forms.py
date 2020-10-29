from django import forms
from .models import Group
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
    '''list = Group.objects.all()
    temp = []
    for group in list:
        select = (group.slug, group.title)
        temp.append(select)
    OPTIONS = tuple(
        temp,
    )'''
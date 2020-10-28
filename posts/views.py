from django.shortcuts import render
from .models import Post
from .models import Group


def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})

def watch_group_list(request):
    groupList = Group.objects.all()
    return render(request, "groups/groupsList.html", {'groupList':groupList},)

def watch_group(request, slug):
    idGroup = Group.objects.filter(slug=slug)[:1]
    groupName = idGroup[0].title
    idGroup = idGroup[0].id
    latest = Post.objects.order_by("-pub_date").filter(group=idGroup)[:10]
    return render(request, "groups/group.html", {'groupName':groupName, 'posts':latest})
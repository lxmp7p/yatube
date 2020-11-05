from django.shortcuts import render, redirect
from .models import Post
from .models import Group
from .forms import PostForm
from .func import get_group_list
import datetime
from .func import get_id_group_on_slug
from django.contrib.auth import get_user_model
import django.contrib.auth
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/')
def index(request):
    get_group_list(title=True)
    latest = Post.objects.order_by("-pub_date").select_related()[:11]
    return render(request, "index.html", {"posts": latest})

@login_required(login_url='/auth/login/')
def watch_group_list(request):
    groupList = Group.objects.select_related().all()
    return render(request, "groups/groupsList.html", {'groupList':groupList},)

@login_required(login_url='/auth/login/')
def watch_group(request, slug):
    idGroup = Group.objects.filter(slug=slug)[:1]
    groupName = idGroup[0].title
    descriptionGroup = idGroup[0].description
    idGroup = idGroup[0].id
    latest = Post.objects.order_by("-pub_date").filter(group=idGroup).prefetch_related()[:10]
    return render(request, "groups/group.html", {'groupName':groupName, 'posts':latest, 'groupSlug':slug, 'descriptionGroup':descriptionGroup, })

@login_required(login_url='/auth/login/')
def add_post(request,slug):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            userObject = None
            User = get_user_model()
            for user in User.objects.all():
                if (str(user) == request.user.username):
                    userObject = user
            post = form.save(commit=False)
            post.author = userObject
            post.pub_date = datetime.datetime.now()
            post.group_id = get_id_group_on_slug(slug)
            post.save()
            return redirect('../../groups/' + slug)
    return render(request, "groups/addPost.html", {"form": form})
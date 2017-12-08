from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from main.models import *

from django.shortcuts import render
from .forms import PostForm, Groups, Users_to_groups_form

def index(request):
    return render(request, 'main/index.html')

# def post_new(request):
#     form = PostForm()
#     return render(request, 'main/new_contact.html', {'form': form})
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.created_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'main/new_contact.html', {'form': form})


@login_required()
def groups(request):
    if request.method == "POST":
        form = Groups(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.created_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = Groups()
        # currentGroups =
    return render(request, 'main/new_group.html', {'form': form})

def users_to_groups(request):
    if request.method == "POST":
        form = Gr(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.created_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = Groups()
    return render(request, 'main/new_group.html', {'form': form})

def users_to_groups(request):
    if request.method == 'POST':
        form = Users_to_groups_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = Users_to_groups_form()
        data = Contacts.objects.all()
    return render(request, 'main/users_to_groups.html', {'data': data, 'form':form})
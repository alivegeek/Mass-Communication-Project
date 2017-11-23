from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.shortcuts import render
from .forms import PostForm, groupsForm

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

def groupsForm(request):
    if request.method == "POST":
        form = groupsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.created_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = groupsForm
    return render(request, 'main/new_group.html', {'form': form})


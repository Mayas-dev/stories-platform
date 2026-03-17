from django.shortcuts import render,redirect
from .forms import StoryForm
from django.contrib.auth.decorators import login_required
from .models import Story
from django.shortcuts import get_object_or_404
from .forms import SignUpForm
from .serializers import StorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@login_required
def submit_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.save()
            return redirect('submission_success')
    else:
        form = StoryForm()

    return render(request, 'cont\submit_story.html', {'form': form})

def submission_success(request):
    return render(request, 'cont\submission_success.html')

def published_stories(request):
    stories = Story.objects.filter(
        status=Story.Status.APPROVED
    ).order_by('-created_at')

    return render(request, 'cont\published_stories.html', {'stories': stories})


def story_detail(request, pk):
    story = get_object_or_404(
        Story,
        pk=pk,
        status=Story.Status.APPROVED
    )
    return render(request, 'cont\story_detail.html', {'story': story})
@login_required
def my_stories(request):
    stories = Story.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'cont\my_stories.html', {'stories': stories})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = SignUpForm()

    return render(request, 'cont\signup.html', {'form': form})

@api_view(['GET'])
def api_stories(request):
    stories = Story.objects.filter(status=Story.Status.APPROVED)
    serializer = StorySerializer(stories, many=True)
    return Response(serializer.data)
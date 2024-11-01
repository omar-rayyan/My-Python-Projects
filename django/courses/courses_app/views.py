from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.contrib import messages

def index(request):
    context = {
        "courses": Course.objects.all(),
    }
    return render(request, 'index.html', context)
def add_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    description = Description.objects.create(content=request.POST['description'])
    Course.objects.create(name=request.POST['name'], description=description)
    return redirect('/')
def add_comment(request):
    errors = Comment.objects.basic_validator(request.POST)
    course = Course.objects.get(id=int(request.session['course']))
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/comments/{course.id}')
    Comment.objects.create(text=request.POST['text'], course=course)
    return redirect(f'/comments/{course.id}')
def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    course_id = int(request.session['course'])
    return redirect(f'/comments/{course_id}')
def view_comments(request, id):
    course = Course.objects.get(id=id)
    comments = course.comments.all()
    request.session['course'] = id
    context = {
        "course": course,
        "comments": comments,
    }
    return render(request, 'comments.html', context)
from django.shortcuts import render, redirect
from django.contrib import messages
from users_app.models import User
from wall_app.models import Message, Comment

def redirect_to_home_wall(request):
    if not 'first_name' in request.session:
        messages.error(request, 'You must first login.', extra_tags='login')
        return redirect('/')
    user = User.objects.get(id=int(request.session['user_id']))
    context = {
        'wall_messages': user.messages.all(),
    }
    request.session['displayed_wall_id'] = user.id
    return render(request,'wall.html', context)
def view_wall(request, id):
    if not 'first_name' in request.session:
        messages.error(request, 'You must first login.', extra_tags='login')
        return redirect('/')
    user = User.objects.get(id=id)
    context = {
        'user': user,
        'wall_messages': user.messages.all(),
    }
    request.session['displayed_wall_id'] = user.id
    return render(request,'wall.html', context)
def post_message(request):
    wall_user_id = int(request.session['displayed_wall_id'])
    errors = Message.objects.message_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='messages')
        return redirect(f'/wall/{wall_user_id}')
    wall_user = User.objects.get(id=wall_user_id)
    commentor_user = User.objects.get(id=int(request.session['user_id']))
    Message.objects.create_message(request.POST, wall_user, commentor_user)
    return redirect(f'/wall/{wall_user_id}')
def post_comment(request):
    message_id = int(request.POST['message-id'])
    wall_user_id = int(request.session['displayed_wall_id'])
    errors = Message.objects.message_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='messages')
        return redirect(f'/wall/{wall_user_id}')
    message = Message.objects.get(id=message_id)
    commentor_user = User.objects.get(id=int(request.session['user_id']))
    Comment.objects.create_comment(request.POST, message, commentor_user)
    return redirect(f'/wall/{wall_user_id}')
def delete_message(request, id):
    message = Message.objects.get(id=id)
    message.delete()
    wall_user_id = int(request.session['displayed_wall_id'])
    return redirect(f'/wall/{wall_user_id}')
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    wall_user_id = int(request.session['displayed_wall_id'])
    return redirect(f'/wall/{wall_user_id}')
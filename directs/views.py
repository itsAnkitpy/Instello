from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from directs.models import Message


@login_required
def inbox(request):
    messages = Message.get_message(user=request.user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=request.user, recipient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0

    context = {
        'directs':directs,
        'messages': messages,
        'active_direct': active_direct,
        
    }
    return render(request, 'directs/direct.html', context)

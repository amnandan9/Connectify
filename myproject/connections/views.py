from django.shortcuts import redirect ,render, get_object_or_404
from django.contrib.auth.models import User
from .models import Connection
from django.views.decorators.http import require_POST
from notifications.models import Notification

@require_POST
def send_request(request, user_id):
    receiver = User.objects.get(id=user_id)

    if not Connection.objects.filter(sender=request.user, receiver=receiver).exists():
        Connection.objects.create(sender=request.user, receiver=receiver)

        Notification.objects.create(
        user=receiver,
        message=f"{request.user.username} sent you a connection request"
    )

    return redirect('connections')

def accept_request(request, request_id):
    conn = Connection.objects.get(id=request_id)
    conn.accepted = True
    conn.save()
    return redirect('feed')

def connection_list(request):
    users = User.objects.exclude(id=request.user.id)

    sent_requests = Connection.objects.filter(sender=request.user)
    received_requests = Connection.objects.filter(receiver=request.user, accepted=False)

    return render(request, 'connections.html', {
        'users': users,
        'sent_requests': sent_requests,
        'received_requests': received_requests
    })



from django.shortcuts import redirect ,render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Connection
from django.views.decorators.http import require_POST
from notifications.models import Notification

@login_required
@require_POST
def send_request(request, user_id):
    receiver = get_object_or_404(User, id=user_id)

    if receiver == request.user:
        return redirect('connections')

    if not Connection.objects.filter(sender=request.user, receiver=receiver).exists():
        Connection.objects.create(sender=request.user, receiver=receiver)

        Notification.objects.create(
            user=receiver,
            message=f"{request.user.username} sent you a connection request"
        )

    return redirect('connections')

@login_required
def accept_request(request, request_id):
    conn = get_object_or_404(Connection, id=request_id, receiver=request.user)
    conn.accepted = True
    conn.save()

    # Create notification for the sender
    Notification.objects.create(
        user=conn.sender,
        message=f"{request.user.username} accepted your connection request"
    )

    return redirect('connections')

@login_required
def connection_list(request):
    users = User.objects.exclude(id=request.user.id)

    sent_requests = Connection.objects.filter(sender=request.user)
    received_requests = Connection.objects.filter(receiver=request.user, accepted=False)
    my_connections = Connection.objects.filter(
        Q(sender=request.user, accepted=True) |
        Q(receiver=request.user, accepted=True)
    )

    return render(request, 'connections.html', {
        'users': users,
        'sent_requests': sent_requests,
        'received_requests': received_requests,
        'my_connections': my_connections
    })



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Conversation, Message


@login_required
def messages_view(request, conversation_id=None):
    conversations = Conversation.objects.filter(
        participants=request.user
    ).distinct().order_by("-updated_at")
    for convo in conversations:
        convo.other_user = convo.participants.exclude(id=request.user.id).first()


    active_conversation = None
    messages = []

    if conversation_id:
        active_conversation = get_object_or_404(
            Conversation,
            id=conversation_id,
            participants=request.user
        )
        active_conversation.other_user = (
            active_conversation.participants.exclude(id=request.user.id).first()
        )

        messages = active_conversation.messages.select_related("sender").order_by("created_at")

        if request.method == "POST":
            Message.objects.create(
                conversation=active_conversation,
                sender=request.user,
                content=request.POST["content"]
            )
            active_conversation.save()  # bumps updated_at
            return redirect("messages", conversation_id=active_conversation.id)

    return render(request, "messages/messages.html", {
        "conversations": conversations,
        "active_conversation": active_conversation,
        "messages": messages,
    })

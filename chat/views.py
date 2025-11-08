from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer

def bot_reply(text):
    t=text.lower()
    if "hi" in t or "hello" in t:
        return "Hello! 👋 How can I help you?"
    if "price" in t:
        return "I can't fetch real prices yet, but ask me anything!"
    if t.endswith("?"):
        return "Good question! (demo bot reply)"
    return "Thanks! (demo bot reply)"

class ChatListCreate(APIView):
    def get(self,request):
        msgs=Message.objects.all()
        return Response(MessageSerializer(msgs,many=True).data)
    def post(self,request):
        text=request.data.get("content","")
        user=Message.objects.create(role="user",content=text)
        bot=Message.objects.create(role="bot",content=bot_reply(text))
        return Response({"user":MessageSerializer(user).data,
                         "bot":MessageSerializer(bot).data},
                         status=status.HTTP_201_CREATED)

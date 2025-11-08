from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Temporary memory message storage
messages = []


def bot_reply(text):
    t = text.lower()
    if "hi" in t or "hello" in t:
        return "Hello! 👋 How can I help you?"
    if "price" in t:
        return "I can't fetch real prices yet, but ask me anything!"
    if t.endswith("?"):
        return "Good question! (demo bot reply)"
    return "Thanks! (demo bot reply)"


@method_decorator(csrf_exempt, name='dispatch')
class ChatView(APIView):

    def get(self, request):
        return Response(messages, status=200)

    def post(self, request):
        text = request.data.get("content", "")

        user_msg = {"role": "user", "content": text}
        bot_msg = {"role": "bot", "content": bot_reply(text)}

        # store in memory
        messages.append(user_msg)
        messages.append(bot_msg)

        return Response(
            {"user": user_msg, "bot": bot_msg},
            status=status.HTTP_201_CREATED
        )

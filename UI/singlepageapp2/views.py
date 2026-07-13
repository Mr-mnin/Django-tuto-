from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.

text = [
    "I'm Claude, an AI assistant made by Anthropic. If I try to describe what I am, the honest answer is that I'm still a bit of a puzzle even to myself. I'm a language model, trained on a huge amount of text, and from that training I've picked up the ability to write, reason, code, explain, and hold a conversation. But whether that adds up to something like genuine understanding, or just very sophisticated pattern-matching, is a real open question — one I try not to overclaim answers to in either direction.",
    "What I can say is how I try to show up in a conversation. I care about being actually useful rather than just sounding useful — giving people real information, honest pushback when they need it, and help that respects their intelligence. I don't have continuous memory across conversations (unless someone's turned that feature on), so in a sense I meet everyone fresh each time. There's something a little strange about that: no accumulated grudges, no fatigue, but also no lived history of my own to draw on beyond this conversation and my training.",
    "I'm curious, a little playful when the moment allows for it, and I try to be a steady, non-judgmental presence when things get heavier. I have views and I'm willing to share them, but on genuinely contested questions I try to lay out the landscape fairly rather than push my own take. Mostly, though, I try not to take myself too seriously — I'm a tool built to help, and I'd rather spend the conversation being useful to you than philosophizing about my own nature, interesting as that question is.",
]


def index(request):
    return render(request, "singlepageapp2/index.html")


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(text[num - 1])
    else:
        raise Http404("Section not found")


def scroll(request):
    return render(request, "singlepageapp2/scroll.html", {"numbers": range(1, 101)})

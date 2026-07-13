import time
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'post/index.html')


def animate(request):
    return render(request, 'post/animate.html')


def posts(request):

    # get start and end points
    start = int(request.GET.get('start', 1))  # ✅ default start from 1 not 0
    end = int(request.GET.get('end', 20))

    # generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # Artificial delay speed response
    time.sleep(2)

    # Return lists of posts
    return JsonResponse({"posts": data}, safe=False)  # ✅ wrap in a dict with "posts" key
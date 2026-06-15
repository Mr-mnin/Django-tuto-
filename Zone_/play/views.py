

# Create your views here.
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# in here we defin our viwe functions
# it takes a request -> returns response.
# so therfore its a request handeler


def home(request):
    # with this we can
    # send email
    # send sms
    # can pull data from database
    # we can also transform data and send it to the template
    return render(request, 'play/Portfolio(home).html')


def about(request):
    # with this we can
    # send email
    # send sms
    # can pull data from database
    # we can also transform data and send it to the template
    return render(request, 'play/Portfolio(About this portfolio).html')


def project(request):
    # with this we can
    # send email
    # send sms
    # can pull data from database
    # we can also transform data and send it to the template
    return render(request, 'play/Portfolio(Projects).html')


def links(request):
    # with this we can
    # send email
    # send sms
    # can pull data from database
    # we can also transform data and send it to the template
    return render(request, 'play/Portfolio(Links).html')


def contacts(request):
    # with this we can
    # send email
    # send sms
    # can pull data from database
    # we can also transform data and send it to the template
    return render(request, 'play/Portfolio(Contacts).html')

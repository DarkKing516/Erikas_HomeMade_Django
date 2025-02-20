# home/views.py
from django.shortcuts import render
from logger.api_client import request_api


def bad_request(request, exception):
    return render(request, '404.html', status=400)


def permission_denied(request, exception):
    return render(request, '404.html', status=403)


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def server_error(request):
    return render(request, '404.html', status=500)


def home(request):
    endpoint = "https://postman-echo.com/post"
    data = {
        "name": "Carlos"
    }
    response = request_api(endpoint, method="POST", data=data)
    return render(request, 'index.html', {'resultApi': response})

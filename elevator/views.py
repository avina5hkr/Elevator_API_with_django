from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Below is a sample view with vanilla Django just for testing purposes
@require_http_methods(["POST"])
@csrf_exempt 
def create_new_elevator(request):
    res = {
        "status": "created",
        "elevator_id": 1,
        "trigger": "up",
        "current_floor": 1,
        "destination_floor": 5,
        "direction": "up",
        "time": "2020-01-01 00:00:00"
    }
    return JsonResponse(res)



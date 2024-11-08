from django.http import JsonResponse

def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/rooms',
        'GET /api/room/:id'
    ]
    return JsonResponse(routes, safe=False)
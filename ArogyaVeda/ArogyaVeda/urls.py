from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
def api_root(request):
    return JsonResponse({
        "project": "ArogyaVeda",
        "status": "Running",
        "message": "Welcome to ArogyaVeda API. Please use /api/ for endpoints."
    })
urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/prediction/', include('Prediction_App.urls')),
]

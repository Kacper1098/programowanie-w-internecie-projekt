from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from mydentist.functions import verify

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token-auth/', obtain_jwt_token),
    path('api/', include('mydentist.urls')),
    re_path(r'^verify/(?P<uuid>[a-z0-9\-]+)/', verify, name='verify'),
]

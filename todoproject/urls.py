from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todoapp.views import TodoViewSet

# create a new router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'todoapp', TodoViewSet) #register "/todos" routes


urlpatterns = [
    # add all of our router urls
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
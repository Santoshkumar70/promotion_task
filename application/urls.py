from django.urls import path
from .views import hrgetmethod,getmethod, postmethod, updatemethod

urlpatterns = [
    path('get', getmethod),
    path('hrget',hrgetmethod),
    path('create',postmethod),
    path('update/<int:id>',updatemethod),
]

from django.contrib import admin
from django.urls import path
from feed import views as feed_views
from chicken import views as chicken_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', feed_views.index),
    path('feed/create/', feed_views.create),
    path('chicken/', chicken_views.index),
    path('chicken/create/', chicken_views.create),
]

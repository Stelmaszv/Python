"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from assets import views
from django.conf import settings
from django.conf.urls.static import static
from assets.views import GameList,ShowGameView,LiberyList,UserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', GameList.as_view(), name='MainPage'),
    url('Create', views.Create, name='Create'),
    url('logout', views.logoutUser, name='logoutUser'),
    url('login', views.loginUser, name='loginUser'),
    url('Register', views.Register, name='Register'),
    url('MyLibrary',  LiberyList.as_view(), name='MyLibraryView'),
    url('LibraryAdd/(?P<Game_id>[-\w]+)/', views.MyLibraryAction, name='MyLibraryAction'),
    url('remowe/(?P<Game_id>[-\w]+)/', views.ItemRemuveAction, name='ItemRemuveAction'),
    url('Edit/(?P<Game_id>[-\w]+)/', views.EditGame, name='EditGame'),
    url('Game/(?P<pk>\d+)/$', ShowGameView.as_view(), name='ShowGame'),
    url('Dalete/?P<id>\d+/$', views.Dalete, name='Dalete'),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
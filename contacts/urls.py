"""contacts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from accounts.views import (login_view, register_view, logout_view)
from posts.views import (manage_contacts, list_contacts, delete, edit_contacts, search_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^accounts/login', login_view, name="login"),
    url(r'^register/', register_view, name="register"),

    url(r'^search/$', search_view, name="search"),
    
    url(r'^delete/(?P<person_pk>.*)$', delete , name='delete-person'),
    url(r'^edit/(?P<person_pk>.*)$', edit_contacts , name='delete-person'),

  
    url(r'^posts/', manage_contacts),
    url(r'^$', list_contacts),
   
    url(r'^logout/', logout_view, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






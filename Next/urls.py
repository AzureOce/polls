"""Next URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # You should always use include() when you include other URL patterns. admin.site.urls is the only exception to
    # this. Note that these regular expressions do not search GET and POST parameters, or the domain name. For
    # example, in a request to https://www.example.com/myapp/, the URLconf will look for myapp/. In a request to
    # https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/.

    # these regular expressions are compiled the first time the URLconf module is loaded.
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls')),
]

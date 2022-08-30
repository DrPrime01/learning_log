"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from argparse import Namespace
from django.contrib import admin
from django.urls import path, re_path
from learning_logs.views import homepage, about, topics, topic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="learning_logs"),
    path('about/', about, name="about_page"),
    path('topics/', topics, name="topics"),
    re_path(r'^topic/(?P<topic_id>\d+)/$', topic, name="topic")
]

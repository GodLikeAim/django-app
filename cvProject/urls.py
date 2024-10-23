"""
URL configuration for cvProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from contact.views import contact_send, about_view

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.index, name="index"),
    path("about/", about_view, name="about"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("blog/", include("blog.urls")),
    path("user/", include("user.urls")),
    path("contact", contact_send, name="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

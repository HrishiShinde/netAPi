"""netAPi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from API import views

urlpatterns = [
    path('djadmin/', admin.site.urls),
    path('user/<int:id>/advisor/', views.getAdvisor),
    path('admin/advisor/', views.setAdvisor),
    path('user/register/', views.usrRegis),
    path('user/login/', views.usrLog),
    path('user/<int:uId>/advisor/<int:aId>/', views.bookAdvisor),
    path('user/<int:uId>/advisor/booking/', views.getBookAdvisor),
    # path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('tokenrefresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

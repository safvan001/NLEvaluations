"""
URL configuration for Webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Androidapp import views
from django.urls import path
from .views import AndroidAppListCreateView, UserTaskSubmitView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

app_name='Androidapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('adminregistration/',views.admin_registration,name='adminregistration'),
    path('adminlogin/', views.admin_login, name='admin_login'),
    path('addapp', views.add_app,name='add_app'),
    path('appview/<int:app_id>', views.display_android_app, name='view'),
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('userview', views.user_view, name='user_view'),
    path('app/<int:p>',views.app_view,name='appview'),




    path('api/admin/apps/', AndroidAppListCreateView.as_view(), name='android-app-list-create'),
    # path('api/user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/user/tasks/<int:app_id>/submit/', UserTaskSubmitView.as_view(), name='user-task-submit'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

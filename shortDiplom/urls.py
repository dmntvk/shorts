from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews
from short import views as userViews
from short.views import root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gl.urls')),
    path('login/', authViews.LoginView.as_view(template_name='short/auth_sign-in.html'), name='login'),
    path('reg/', userViews.reg, name='reg'),
    path('exit/', authViews.LogoutView.as_view(template_name='short/exit.html'), name='exit'),
    path('profile/', userViews.profile, name='profile'),
    path('create/', userViews.create_url.as_view(), name='create'),
    path('<str:url_hash>/', root, name='root'),

]

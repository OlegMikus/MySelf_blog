from django.contrib import admin
from django.urls import path, include
from blog.views import PostsUserListView
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from users.views import ProfileListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile_settings/', user_views.profile_settings, name='profile_settings'),
    path('profile/', ProfileListView.as_view(), name='profile'),
    path('user/<str:username>', PostsUserListView.as_view(), name='profile-public'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

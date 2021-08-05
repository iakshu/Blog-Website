from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from blogapp.views import home, addpost, blogpage ,update, deletepost
from auapp.views import user_login, user_logout, user_signup, editprofile

app_name = 'blogapp'

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', home, name='home'),
	# path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='user_login'),
	path('user_login/', user_login, name='user_login'),
	path('user_signup/', user_signup, name='user_signup'),
	path('user_logout/', user_logout, name='user_logout'),

	path('password/change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
	path('password/change/done', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
	path('password/reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
	path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
	path('password/reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
	path('password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

	path('edit/', editprofile, name='editprofile'),
	path('addpost/', addpost, name='addpost'),
	path('blogpage/<pk>', blogpage, name='blogpage'),
	path('update/<pk>', update, name='update'),
	path('deletepost/<pk>', deletepost, name='deletepost'),
]


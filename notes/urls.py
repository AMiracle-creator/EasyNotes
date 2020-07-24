from django.urls import path
from . import views

app_name = "notes"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.index, name="index"),
    path("signup/",views.sign_up,name='sign_up'),
    path('create/', views.create, name='create'),
    path('signin/', views.sign_in, name='sign_in'),
    path('board/', views.board, name='board'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path('settings/', views.settings, name='settings')
    # path('<int:algorithm_id>/', views.detail, name='detail'),
    # path('<int:algorithm_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]

from django.urls import path

from day6 import views

app_name = 'day6'

urlpatterns = [
    # path('성진/', views.show_성진, name='성진'),
    # path('youngk/', views.show_youngk, name='youngk'),
    # path('원필/', views.show_원필, name='원필'),
    # path('도운/', views.show_도운, name='도운'),
    path('<멤버>/', views.show_멤버, name='멤버'),


]
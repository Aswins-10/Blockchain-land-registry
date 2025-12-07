from django.urls import path
from . import views


urlpatterns = [
    # path('company/', views.company_login, name='company_login'),
    # path('customer/', views.customer_login, name='customer_login'),
    # path('staff/', views.staff_login, name='staff_login'),
    # path('customer/', views.customer_login, name='upload_staff'),
    # path('staff/', views.staff_login, name='company_login'),
    path('logout/', views.logout, name='logout'),
]


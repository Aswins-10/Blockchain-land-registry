from django.urls import path

from donate import views

urlpatterns = [
    path('nedonate/', views.upload, name='upload_donate'),
    path('all', views.donates_all, name='donates_all'),
    path('nedonate/<int:donates_id>', views.update_donates, name='update_donates'),
    #path('getdonate/<int:uid_id>', views.update_donate_uid, name='update_donated_uid'),
    path('productdonationtrace/<int:product_id>', views.project_donated_dtls, name='project_donated_dtls'),
    path('delete/<int:donates_id>', views.delete_donates, name='delete_donates'),
    path('productdonated/', views.project_donated, name='project_donated'),
    path('nedonateproduct/<int:product_id>', views.update_project_donates, name='update_project_donates'),

]


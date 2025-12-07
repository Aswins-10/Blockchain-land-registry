from django.urls import path

from complaint import views

urlpatterns = [
    # path('newcomplaints/', views.upload, name='upload_complaints'),
    path('all', views.complaint_all, name='complaint_all'),
    # path('newcomplaints/<int:complaints_id>', views.update_complaints, name='update_complaints'),
    path('delete/<int:complaint_id>', views.delete_complaint, name='delete_complaint'),
    path('customcomplaint/', views.upload_custom, name='upload_custon_complaint'),
    path('customcomplaint/<int:complaint_id>', views.update_custom, name='customcomplaint'),  # view customer wise

]

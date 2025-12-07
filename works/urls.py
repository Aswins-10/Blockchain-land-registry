from django.urls import path

from works import views

urlpatterns = [
    path('newwork/', views.upload, name='upload_work'),
    path('all', views.works_all, name='works_all'),
    path('propertyownerall', views.Property_owner_all, name='Property_owner_all'),
    path('landsetsell/<int:land_id>', views.land_set_sell, name='land_set_sell'),
    path('landsetapprove/<int:land_id>', views.land_set_approve, name='land_set_approve'),
    path('landforpurchase', views.land_for_purchase, name='land_for_purchase'),
    path('landmoredetails/<int:land_id>', views.land_more_details, name='land_more_details'),
    path('purchasereq', views.purchase_req, name='purchase_req'),
    path('landpurchaserequest', views.land_purchase_request, name='land_purchase_request'),
    path('landpinterest/<int:interest_id>', views.land_p_interest, name='land_p_interest'),
    path('approvesale', views.approve_sale, name='approve_sale'),
    path('requestapprove/<int:interest_id>', views.request_approve, name='request_approve'),

    path('request_accept/<int:interest_id>', views.request_accept, name='request_accept'),
    path('newwork/<int:works_id>', views.update_works, name='update_works'),
    path('delete/<int:works_id>', views.delete_works, name='delete_works'),
    path('changestatus/<int:work_id>', views.changestatus_workexp, name='changestatus_workexp'),
    path('newexpenditure/', views.upload_expenditure, name='upload_expenditure'),
    path('allexpenditure', views.expenditure_all, name='expenditure_all'),
    path('newexpenditure/<int:expenditure_id>', views.update_expenditure, name='update_expenditure'),
    path('deleteexpenditure/<int:expenditure_id>', views.delete_expenditure, name='delete_expenditure'),

]


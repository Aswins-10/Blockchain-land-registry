from django.urls import path

from comment import views

urlpatterns = [
    # path('newcomment/', views.upload, name='upload_comment'),
    path('all', views.comment_all, name='comment_all'),
    # path('newcomment/<int:comment_id>', views.update_comment, name='update_comment'),
     path('delete/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('customcomment/', views.upload_custom, name='upload_custon_comment'),
    path('customcomment/<int:comment_id>', views.update_custom, name='customcomment'),  # view customer wise
    path('analysecomment/<int:pjt_id>', views.analyse_comment, name='analyse_comment'),
    path('commentlist', views.comment_list, name='comment_list'),

]


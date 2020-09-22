from django.urls import path

from . import views

urlpatterns = [
    #home
    path('',views.index,name="index"),
    path('topics/',views.topics,name="topics"),
    path('topics/<str:name>',views.entries,name="entries"),
    path('new_topic/',views.new_topic,name = 'new_topic'),
    path('topics/<str:name>/new_entry',views.new_entry,name = 'new_entry'),
    path('topics/<str:name>/edit_entry/<int:entry_id>',views.edit_entry, name = 'edit_entry'),
]
app_name = 'learning_logs'
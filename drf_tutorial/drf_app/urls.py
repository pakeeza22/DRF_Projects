from django.urls import path

from .views import StudentListCreate, StudentRUD

app_name = 'drf_app'
urlpatterns = [
      # for Function based API View
#     path('std_api/', student_api, name='student'),
#     path('std_model_api/', student_api, name='student'),

      # for class based API View
#       path('std_model_api/', StudentApi.as_view(), name='student'),
#       path('std_model_api/<int:pk>/', StudentApi.as_view(), name='student'),

      # for Generic API View
      #  path('std_list/', StudentList.as_view(), name='student'),
      #  path('std_create/', StudentCreate.as_view(), name='student'),
      #  path('std_retrieve/<int:pk>/', StudentRetrieve.as_view(), name='student'),
      #  path('std_update/<int:pk>/', StudentUpdate.as_view(), name='student'),
      #  path('std_delete/<int:pk>/', StudentDestroy.as_view(), name='student'),
       path('std_lc/', StudentListCreate.as_view(), name='student'),
       # path('std_ru/<int:pk>/', StudentRtUpdate.as_view(), name='student'),
       # path('std_rd/<int:pk>/', StudentRtDestroy.as_view(), name='student'),
       path('std_rud/<int:pk>/', StudentRUD.as_view(), name='student'),
]

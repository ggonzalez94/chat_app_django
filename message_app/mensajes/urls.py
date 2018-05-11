from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView,ListMessagesView,ListUsersView
from .views import index

urlpatterns = [
    path('users/', ListUsersView.as_view(), name='user-list'),    # GET for all users list
    path('mensajes/', CreateView.as_view(), name="create"),
    path('listar_mensajes/', ListMessagesView.as_view(), name="list"),
    path('',index,name='index'),
    path('auth/', include('rest_framework.urls', # ADD THIS URL
                                   namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

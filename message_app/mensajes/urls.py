from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView,ListMessagesView,ListUsersView
from .views import user_list,message_list

urlpatterns = [
        # URL form : "/api/messages/1/2"
    path('messages/<int:sender>/<int:receiver>',message_list, name='message-detail'),  # For GET request.
    # URL form : "/api/messages/"
    path('messages/', message_list, name='message-list'),   # For POST
    # URL form "/api/users/1"
    path('users/<int:pk>', user_list, name='user-detail'),      # GET request for user with id
    path('users/', ListUsersView.as_view(), name='user-list'),    # POST for new user and GET for all users list
    path('mensajes/', CreateView.as_view(), name="create"),
    path('listar_mensajes/', ListMessagesView.as_view(), name="list"),
    path('auth/', include('rest_framework.urls', # ADD THIS URL
                                   namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

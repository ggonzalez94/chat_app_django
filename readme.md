Steps to make the project run:
1. mkdir chat_app
2. pip install Django
3. pip install djangorestframework
3. cd chat_app
4. git clone https://github.com/ggonzalez94/chat_app_django.git
5. cd message_app
6. python manage.py rumserver

Routes available:
For accessing de admin page localhost:8000/admin
To login as a user localhost:8000/auth/login
To GET messages available to the user currently logged in localhost:8000/listar_mensajes
To send a new message(Post) localhost:8000/mensajes
To GET a list of users localhost:8000/users

In order to perform most of this actions you have to be logged in, otherwise you will see a permission denied message
from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth import get_user_model


User = get_user_model()

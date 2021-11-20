from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user manager, email is unique
    """
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise

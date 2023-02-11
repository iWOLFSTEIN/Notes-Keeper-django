from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user with the given email and password.
        """
        if not email:
            raise ValueError('Users must have a valid email address.')

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a new superuser with the given email and password.
        """
        user = self.create_user(email, password=password, **extra_fields)
        
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

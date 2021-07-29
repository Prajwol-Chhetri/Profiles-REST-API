from django.db import models

# base classes required to overwrite default django user models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.db.models.deletion import CASCADE

class UserProfileManager(BaseUserManager):
    """Manager for User Profiles. Creating a manager to handle the model because as default Django
    requires Username and Password Field to create a user but we've changed this to Email field"""
    
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        # normalizing email for standarization
        email = self.normalize_email(email)  
        # creating user model that user manager is representing
        user = self.model(email=email, name=name)
        # Encrypting password using method of AbstractBaseUserClass
        user.set_password(password)
        # self._db to save to any database 
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """create and save new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    def ___str__(self):
        """Return string representation of our user"""
        return self.email

    
class ProfileFeedItem(models.Model):
    """Profile Status Update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # preventing hard coding of Foreign Key
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def ___str__(self):
        """Return string representation of our model"""
        return self.status_text 

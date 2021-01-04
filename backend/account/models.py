import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):

    # Everytime that a new user is created
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        if not username:
            raise ValueError("Users must have an username/nickname")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_superuser(self, email, username, password=None):

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)
        return user


# Create your models here.
class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    username = models.CharField(max_length=150, db_index=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True) 
    phone = models.CharField(max_length=16, blank=True, null=True)
    password = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Select wich field will be used to login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()
    
    def __str__(self):
        return self.username


    # When a new user is created
    def save(self, *args, **kwargs):

        # Always lowercase the email.
        self.email = self.email.lower()

        # Save the user
        super().save(*args, **kwargs)


    # Overrride functions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

# Following system
class Follower(models.Model):
    user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id','following_user_id'],  name="unique_followers")
        ]

        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user_id} -> follows -> {self.following_user_id }"
import uuid
from django.db import models
from account.models import User

class Wish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    id_wishlist = models.ForeignKey('WishList', on_delete=models.CASCADE)
    link = models.CharField(max_length=2083)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='wishes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('Wish')
        verbose_name_plural = ('Wishes')

    def __str__(self):
        return self.title   

    def save(self, *args, **kwargs):

        # Limit price for 2 decimal places
        self.price = round(self.price, 2)

        super(Wish, self).save(*args, **kwargs)


# Create your models here.
class WishList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    public = models.BooleanField(default=True)
    wishes = models.ManyToManyField(Wish, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = ('Wish List')
        verbose_name_plural = ('Wish Lists')

    def __str__(self):
        return self.title
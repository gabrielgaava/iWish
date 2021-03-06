# Generated by Django 3.1.4 on 2021-01-04 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wish', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('public', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wishes', models.ManyToManyField(to='wish.Wish')),
            ],
        ),
        migrations.AddField(
            model_name='wish',
            name='id_wishlist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wish.wishlist'),
            preserve_default=False,
        ),
    ]

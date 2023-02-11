# Generated by Django 4.1.6 on 2023-02-10 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=500)),
                ('mobile_no', models.CharField(max_length=12)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.FloatField(default=1)),
                ('total_cost', models.FloatField(default=1)),
                ('order_status', models.CharField(choices=[('pending', 'Pending'), ('cancelled', 'Cancelled'), ('confirm', 'Confirm'), ('on_the_way', 'On the way'), ('delivered', 'Delivered')], default='pending', max_length=50)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('cancelled', 'Cancelled'), ('confirm', 'Confirm')], default='pending', max_length=50)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cutomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cutomer', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='items.item')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0010_order_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cardealer",
            name="email",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="cardealer",
            name="username",
            field=models.CharField(max_length=50),
        ),
    ]

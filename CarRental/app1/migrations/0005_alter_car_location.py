# Generated by Django 4.1.7 on 2023-04-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0004_car"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="location",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]

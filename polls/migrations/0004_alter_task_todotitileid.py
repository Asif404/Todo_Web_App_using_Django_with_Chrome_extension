# Generated by Django 3.2.7 on 2021-09-19 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210918_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='todoTitileid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.todotitile'),
        ),
    ]

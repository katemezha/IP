# Generated by Django 3.1.6 on 2021-02-05 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_usersname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.DeleteModel(
            name='Errors',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
        migrations.DeleteModel(
            name='Otz',
        ),
        migrations.DeleteModel(
            name='Saleproduct',
        ),
        migrations.DeleteModel(
            name='Salesname',
        ),
        migrations.DeleteModel(
            name='Statistic',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.DeleteModel(
            name='Usersname',
        ),
    ]

# Generated by Django 4.0 on 2022-01-09 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_account_businesscategory_alter_account_role_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='businessName',
            new_name='county',
        ),
        migrations.RemoveField(
            model_name='account',
            name='businessDescription',
        ),
    ]

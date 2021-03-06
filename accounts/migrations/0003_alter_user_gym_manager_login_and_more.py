# Generated by Django 4.0.4 on 2022-05-26 19:27

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_reservations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gym_manager_login',
            field=encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gym_manager_password',
            field=encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True),
        ),
    ]

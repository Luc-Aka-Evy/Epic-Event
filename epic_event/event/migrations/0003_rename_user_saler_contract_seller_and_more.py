# Generated by Django 4.0.5 on 2022-06-09 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_contract_updated_time_alter_event_end_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='user_saler',
            new_name='seller',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='user_support',
            new_name='support',
        ),
    ]

# Generated by Django 2.0.2 on 2021-03-16 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sleepapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sleepcyclemodel',
            old_name='bedtime',
            new_name='sleepStruggle',
        ),
        migrations.RenameField(
            model_name='sleepcyclemodel',
            old_name='struggling',
            new_name='sleepTime',
        ),
        migrations.RenameField(
            model_name='sleepcyclemodel',
            old_name='wakeuptime',
            new_name='wakeUpTime',
        ),
    ]
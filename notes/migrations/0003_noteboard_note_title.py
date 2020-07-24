# Generated by Django 3.0.5 on 2020-07-10 19:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200708_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteboard',
            name='note_title',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='название заметки'),
            preserve_default=False,
        ),
    ]

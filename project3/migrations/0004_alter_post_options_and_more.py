# Generated by Django 5.1.3 on 2025-01-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project3', '0003_post_counted_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish',
            new_name='published_date',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

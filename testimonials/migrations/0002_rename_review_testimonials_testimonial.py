# Generated by Django 3.2.20 on 2023-10-11 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonials',
            old_name='review',
            new_name='testimonial',
        ),
    ]

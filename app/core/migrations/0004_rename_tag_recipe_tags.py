# Generated by Django 5.0.2 on 2024-03-08 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tag_recipe_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='tag',
            new_name='tags',
        ),
    ]
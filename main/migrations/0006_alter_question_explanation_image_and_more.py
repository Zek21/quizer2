# Generated by Django 4.2.6 on 2023-10-31 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_question_explanation_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='explanation_image',
            field=models.ImageField(blank=True, null=True, upload_to='explanations/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='questions/'),
        ),
    ]

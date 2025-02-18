# Generated by Django 4.2.14 on 2024-07-22 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_projetdev_outil_utilise_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetdev',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='devpdf/'),
        ),
        migrations.AddField(
            model_name='projetdl',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='dlpdf/'),
        ),
        migrations.AddField(
            model_name='projetml',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='mlpdf/'),
        ),
    ]

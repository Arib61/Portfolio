# Generated by Django 4.2.14 on 2024-07-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_projetdev_projetdl_projetml'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetdl',
            name='algorithmes_utilises',
            field=models.TextField(default='"#'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projetml',
            name='algorithmes_utilises',
            field=models.TextField(default='#'),
            preserve_default=False,
        ),
    ]

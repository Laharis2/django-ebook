# Generated by Django 4.0.4 on 2022-05-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kategori', models.CharField(max_length=100)),
            ],
        ),
    ]

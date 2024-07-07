# Generated by Django 5.0.3 on 2024-07-02 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowsite', '0013_alter_role_title_alter_specialization_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=20, verbose_name='Назва пункту')),
                ('slug', models.SlugField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Пункти меню',
                'verbose_name_plural': 'Пункти меню',
                'ordering': ['pk'],
            },
        ),
    ]
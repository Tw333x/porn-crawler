# Generated by Django 2.0.2 on 2018-12-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avgle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'db_table': 'Avgle',
            },
        ),
        migrations.CreateModel(
            name='Popjav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'db_table': 'Popjav',
            },
        ),
        migrations.CreateModel(
            name='Pornhub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'db_table': 'Pornhub',
            },
        ),
        migrations.CreateModel(
            name='Redtube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'db_table': 'Redtube',
            },
        ),
        migrations.CreateModel(
            name='Thisav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'db_table': 'Thisav',
            },
        ),
        migrations.CreateModel(
            name='Tube85',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'db_table': 'Tube85',
            },
        ),
        migrations.CreateModel(
            name='Xvideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'db_table': 'Xvideos',
            },
        ),
        migrations.CreateModel(
            name='Youporn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'db_table': 'Youporn',
            },
        ),
    ]
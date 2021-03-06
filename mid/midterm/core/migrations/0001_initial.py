# Generated by Django 2.2.5 on 2019-10-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField()),
                ('size', models.IntegerField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'DRESS'), (2, 'JEANS'), (3, 'SKIRT'), (4, 'BLOUSE')])),
                ('existence', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField()),
                ('approximate_duration', models.IntegerField()),
                ('service_type', models.PositiveSmallIntegerField(choices=[(1, 'SERVICE1'), (2, 'SERVICE2'), (3, 'SERVICE3')])),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Service',
            },
        ),
    ]

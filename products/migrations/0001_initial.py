# Generated by Django 4.2.2 on 2023-09-09 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('published_date', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('counted_views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='products.category')),
                ('colors', models.ManyToManyField(to='products.color')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]

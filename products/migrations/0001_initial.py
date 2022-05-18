# Generated by Django 3.1 on 2022-05-17 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('biography', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('language', models.CharField(blank=True, max_length=200, null=True)),
                ('publicationdate', models.CharField(blank=True, max_length=200, null=True)),
                ('numberofpage', models.DecimalField(decimal_places=0, max_digits=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.author')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryClothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('material', models.CharField(blank=True, max_length=200, null=True)),
                ('size', models.CharField(blank=True, max_length=200, null=True)),
                ('color', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryclothes')),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ram', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('battery', models.CharField(blank=True, max_length=200, null=True)),
                ('weight', models.CharField(blank=True, max_length=200, null=True)),
                ('material', models.CharField(blank=True, max_length=200, null=True)),
                ('warranty', models.CharField(blank=True, max_length=200, null=True)),
                ('size', models.CharField(blank=True, max_length=200, null=True)),
                ('operationSystem', models.CharField(blank=True, max_length=200, null=True)),
                ('CPU', models.CharField(blank=True, max_length=200, null=True)),
                ('VGA', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cpu', models.CharField(blank=True, max_length=200, null=True)),
                ('screen', models.CharField(blank=True, max_length=200, null=True)),
                ('ram', models.CharField(blank=True, max_length=200, null=True)),
                ('feature', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('operation_system', models.CharField(blank=True, max_length=200, null=True)),
                ('battery', models.CharField(blank=True, max_length=200, null=True)),
                ('warranty', models.CharField(blank=True, max_length=200, null=True)),
                ('backcamera', models.CharField(blank=True, max_length=200, null=True)),
                ('fontcamera', models.CharField(blank=True, max_length=200, null=True)),
                ('color', models.CharField(blank=True, max_length=200, null=True)),
                ('size', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MobilePhoneItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('discount', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='products/mobilephone/%Y/%m/%d')),
                ('mobile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.mobilephone')),
            ],
        ),
        migrations.CreateModel(
            name='LaptopItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('discount', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='products/laptop/%Y/%m/%d')),
                ('laptop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.laptop')),
            ],
        ),
        migrations.AddField(
            model_name='laptop',
            name='producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producer'),
        ),
        migrations.CreateModel(
            name='ClothesItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('discount', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='products/clothes/%Y/%m/%d')),
                ('clothes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.clothes')),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('discount', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='products/book/%Y/%m/%d')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.publisher'),
        ),
    ]

# Generated by Django 3.1 on 2022-05-18 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('techType', models.CharField(max_length=255, null=True)),
                ('typeCpu', models.CharField(max_length=255, null=True)),
                ('speed', models.CharField(max_length=255, null=True)),
                ('brand', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VGA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('vram', models.CharField(max_length=255, null=True)),
                ('tech', models.CharField(max_length=255, null=True)),
                ('brand', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bookitem',
            name='book',
        ),
        migrations.RemoveField(
            model_name='clothes',
            name='material',
        ),
        migrations.RemoveField(
            model_name='clothes',
            name='name',
        ),
        migrations.RemoveField(
            model_name='clothes',
            name='type',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='CPU',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='VGA',
        ),
        migrations.RemoveField(
            model_name='mobilephoneitem',
            name='mobile',
        ),
        migrations.AddField(
            model_name='bookitem',
            name='numAvailidInStock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookitem',
            name='numberSold',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clothes',
            name='countryOfOrigin',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clothes',
            name='importPrice',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='clothes',
            name='marterial',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clothes',
            name='productName',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clothesitem',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='clothesitem',
            name='numAvailidInStock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clothesitem',
            name='numberSold',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='laptopitem',
            name='numAvailidInStock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='laptopitem',
            name='numberSold',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mobilephoneitem',
            name='mobilePhone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.mobilephone'),
        ),
        migrations.AddField(
            model_name='mobilephoneitem',
            name='numAvailidInStock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mobilephoneitem',
            name='numberSold',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='discount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='brand',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='color',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='size',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clothesitem',
            name='clothes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.clothes'),
        ),
        migrations.AlterField(
            model_name='clothesitem',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clothesitem',
            name='discount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='clothesitem',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clothesitem',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='laptopitem',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='laptopitem',
            name='discount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='laptopitem',
            name='laptop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.laptop'),
        ),
        migrations.AlterField(
            model_name='laptopitem',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='laptopitem',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mobilephoneitem',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mobilephoneitem',
            name='discount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mobilephoneitem',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mobilephoneitem',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='laptop',
            name='cpu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.cpu'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='vga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.vga'),
        ),
    ]
# Generated by Django 3.1 on 2022-05-17 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
            ],
        ),
    ]

# Generated by Django 4.0 on 2021-12-25 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busno', models.CharField(max_length=10)),
                ('fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='place',
            fields=[
                ('placeid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('usn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=25)),
                ('saddress', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('branch', models.CharField(max_length=10)),
                ('sem', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('reciptno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date_of_pay', models.DateField()),
                ('validity', models.DateField()),
                ('busno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bus')),
                ('usn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='placeid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.place'),
        ),
        migrations.CreateModel(
            name='goes_to',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boarding_time', models.TimeField()),
                ('busno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bus')),
                ('placeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.place')),
            ],
            options={
                'unique_together': {('busno', 'placeid')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='bus',
            unique_together={('busno', 'placeid')},
        ),
    ]

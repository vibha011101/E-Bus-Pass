# Generated by Django 4.0 on 2021-12-26 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bus',
            options={'ordering': ('busno', 'placeid')},
        ),
        migrations.AlterModelOptions(
            name='goes_to',
            options={'ordering': ('busno', 'placeid')},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ('reciptno', 'date_of_pay')},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ('placeid', 'pname')},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('usn', 'sname')},
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Monthly'), (1, 'Yearly'), (2, 'Quarterly')], default=0),
        ),
    ]

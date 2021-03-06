# Generated by Django 2.2.3 on 2019-07-05 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('companies', '0001_initial'),
        ('locations', '0001_initial'),
        ('feedbacks', '0001_initial'),
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='companies',
            field=models.ManyToManyField(to='companies.Company'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='feedback',
            field=models.ManyToManyField(to='feedbacks.Feedback'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='location',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='locations.Location'),
        ),
    ]

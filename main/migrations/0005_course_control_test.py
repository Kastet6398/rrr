# Generated by Django 4.0.6 on 2023-11-29 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_question_tid'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='control_test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.test'),
        ),
    ]

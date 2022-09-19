# Generated by Django 4.1.1 on 2022-09-19 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("routine", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="routine",
            name="account_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="routineday",
            name="routine_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="routine.routine",
            ),
        ),
        migrations.AlterField(
            model_name="routineresult",
            name="result",
            field=models.CharField(
                choices=[("NOT", "NOT"), ("DONE", "DONE"), ("TRY", "TRY")],
                default="NOT",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="routineresult",
            name="routine_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="routine.routine",
            ),
        ),
    ]
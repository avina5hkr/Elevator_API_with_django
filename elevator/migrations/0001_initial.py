# Generated by Django 4.1.5 on 2023-01-21 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElevatorStatus',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('status', models.CharField(db_column='status', max_length=10)),
            ],
            options={
                'db_table': 'elevator_status',
            },
        ),
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('current_floor', models.IntegerField(db_column='current_floor')),
                ('destination_floor', models.IntegerField(db_column='destination_floor')),
                ('direction', models.BooleanField(db_column='direction', null=True)),
                ('working', models.BooleanField(db_column='working')),
                ('min_floor', models.IntegerField(db_column='min_floor')),
                ('max_floor', models.IntegerField(db_column='max_floor')),
                ('status', models.ForeignKey(db_column='status', on_delete=django.db.models.deletion.CASCADE, to='elevator.elevatorstatus')),
            ],
            options={
                'db_table': 'elevator',
            },
        ),
    ]
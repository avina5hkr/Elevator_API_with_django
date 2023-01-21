from django.db import models

# Create your models here.

class Elevator(models.Model):
    id = models.AutoField(db_column='id', primary_key=True) # primary key
    status = models.ForeignKey('ElevatorStatus', on_delete=models.CASCADE, db_column='status', null=False)
    current_floor = models.IntegerField(db_column='current_floor', null=False) 
    destination_floor = models.IntegerField(db_column='destination_floor', null=False)
    direction = models.BooleanField(db_column='direction', null=True) # True if going up, False if going down
    working = models.BooleanField(db_column='working', null=False) # True, False if elevator is working or not
    min_floor = models.IntegerField(db_column='min_floor', null=False) # min floor served by the elevator
    max_floor = models.IntegerField(db_column='max_floor', null=False) # max floor served by the elevator
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = 'elevator'

class ElevatorStatus(models.Model):
    id = models.AutoField(db_column='id', primary_key=True) # primary key
    status = models.CharField(db_column='status', max_length=10, null=False) # idle, moving, stopped

    def __str__(self):
        return str(self.status)
    class Meta:
        db_table = 'elevator_status'
    
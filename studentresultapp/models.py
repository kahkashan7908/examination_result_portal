from django.db import models

class tenthData(models.Model):
    name=models.CharField(max_length=50)
    hall_ticket=models.BigIntegerField()
    urdu=models.IntegerField()
    hindi=models.IntegerField()
    mathematics=models.IntegerField()
    science=models.IntegerField()
    social_science=models.IntegerField()

class interData(models.Model):
    name=models.CharField(max_length=50)
    hall_ticket=models.BigIntegerField()
    hindi=models.IntegerField()
    english=models.IntegerField()
    physics=models.IntegerField()
    chemistry=models.IntegerField()
    mathematics=models.IntegerField()

class degreeData(models.Model):
    name=models.CharField(max_length=50)
    hall_ticket=models.BigIntegerField()
    hindi=models.IntegerField()
    english=models.IntegerField()
    history=models.IntegerField()
    Political_Science=models.IntegerField()
    geography=models.IntegerField()

class btechData(models.Model):
    name=models.CharField(max_length=50)
    hall_ticket=models.BigIntegerField()
    english=models.IntegerField()
    chemistry=models.IntegerField()
    mathematics=models.IntegerField()
    machine=models.IntegerField()
    basic_electrical=models.IntegerField()




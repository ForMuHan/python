from django.db import models

class Student(models.Model):
    bname=models.CharField(max_length=20)
    bage=models.CharField(max_length=20)
    bdate=models.DateField()
    isDelete=models.BooleanField(default=False)

    class Meta:
        db_table='student'

    def __str__(self):
        return self.bname

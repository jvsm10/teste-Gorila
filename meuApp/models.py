from django.db import models

# Create your models here.
class CDB(models.Model):

    class Meta:

        db_table = 'cdb'

    investmentDate = models.DateField()
    cdbRate = models.FloatField()
    currentDate = models.DateField()

    def __str__(self):
        return self.cdbRate
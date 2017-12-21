from django.db import models

class Match(models.Model):
    hP = models.CharField(max_length = 20)
    aP = models.CharField(max_length = 20)

    def __str__(self):
        return self.hP + ' - ' + self.aP

class Result(models.Model):
    participants = models.ForeignKey(Match, on_delete=models.CASCADE)
    hS1 = models.IntegerField()
    aS1 = models.IntegerField()
    hS2 = models.IntegerField()
    aS2 = models.IntegerField()
    hS3 = models.IntegerField()
    aS3 = models.IntegerField()

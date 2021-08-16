from django.db import models

class customer(models.Model):
  Username = models.CharField(max_length=50)
  Phonenumber = models.IntegerField(default=0)

  def __str__(self):
    return self.Username
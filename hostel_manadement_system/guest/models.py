from django.db import models
from django.core.validators import MinLengthValidator
from selection.models import User


# Create your models here.

class Room(models.Model):
    room_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy')]
    no = models.CharField(validators=[MinLengthValidator(2)], max_length=5, unique=True)
    max_persons = models.IntegerField(default=2)
    room_type = models.CharField(choices=room_choice, max_length=1, default=None)
    price = models.IntegerField(default=500)

    def __str__(self):
        return 'Room no: %s price: %s' %(str(self.no), str(self.price))


class Reservation(models.Model):
    room = models.ForeignKey(to: 'Room')

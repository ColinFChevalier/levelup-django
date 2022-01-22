from django.db import models
from django.utils import tree
# from django.db.models.deletion import CASCADE
from .gamer import Gamer
from .game import Game

class Event(models.Model):

    game = models.ForeignKey(
        Game,
        related_name='events',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField()
    gamer = models.ForeignKey(
        Gamer,
        related_name='events',
        null=True,
        on_delete=models.CASCADE
    )
    attendees = models.ManyToManyField(
        Gamer,
        related_name="attending_events"
    )
    description = models.CharField(
        max_length=120,
        null=True
        )
    organizer = models.ForeignKey(
        Gamer,
        related_name="organizing_events",
        null=True,
        on_delete=models.CASCADE
    )
    time = models.TimeField(
        default="No time selected"
    )
    name = models.CharField(
        null=True,
        max_length=50
    )

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value

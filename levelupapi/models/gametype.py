from django.db import models

class GameType(models.Model):
    """"defines game type"""
    game_type = models.CharField(
        max_length=20,
        null=True)

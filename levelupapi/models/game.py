# from django.db import models
# # from levelupapi.models import Gamer, GameType
# from .gametype import GameType
# from .gamer import Gamer

# class Game(models.Model):
    
#     title = models.CharField(max_length=50, default="None")
#     maker = models.CharField(max_length=50, default="None")
#     gamer = models.ForeignKey(Gamer, related_name='games', on_delete=models.SET_NULL, null=True)
#     game_type = models.ForeignKey(GameType, related_name="games", on_delete=models.SET_NULL, null=True)
#     number_of_players = models.IntegerField(default=1)
#     skill_level = models.IntegerField(default=1)

from django.db import models
from .gametype import GameType
from .gamer import Gamer

class Game(models.Model):

    game_type = models.ForeignKey(
        GameType,
        verbose_name="Game Type",
        null=True,
        on_delete = models.SET_NULL
    )
    title = models.CharField(max_length=50, default='none')
    maker = models.CharField(max_length=50, default='none')
    gamer = models.ForeignKey(Gamer,
    verbose_name="Gamer",
    null=True,
    on_delete = models.SET_NULL
    )
    skill_level = models.IntegerField(default=1)
    number_of_players = models.IntegerField(default=1)
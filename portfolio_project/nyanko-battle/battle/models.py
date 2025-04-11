

from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    health = models.IntegerField(default=100)
    attack_power = models.IntegerField(default=10)

    def __str__(self):
        return self.name

class Battle(models.Model):
    attacker = models.ForeignKey(Character, related_name='attacker', on_delete=models.CASCADE)
    defender = models.ForeignKey(Character, related_name='defender', on_delete=models.CASCADE)
    winner = models.ForeignKey(Character, related_name='winner', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.attacker} vs {self.defender}"
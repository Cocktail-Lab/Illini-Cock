from django.db import models


# Create your models here.
class GPT(models.Model):
    liquor_choices = (
        ('whiskey', 'Whiskey'),
        ('rum', 'Rum'),
        ('gin', 'Gin'),
        ('vodka', 'Vodka'),
        ('brandy', 'Brandy'),
    )
    liquor = models.CharField(max_length=10, choices=liquor_choices)
    

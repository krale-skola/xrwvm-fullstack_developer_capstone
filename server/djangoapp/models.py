# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name + self.description

# Create CarMadel model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('VAN', 'van'),
        ('MINIVAN', 'Minivan'),
        ('HATCHBACK', 'Hatchback')
    ]
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2024),
            MinValueValidator(2000)
        ])
    COLORS_CHOICE = [
        ('BLACK', 'Black'),
        ('WHITE', 'White'),
        ('BLUE', 'Blue'),
        ('GREY', 'Grey'),
        ('RED', 'Red'),
        ('ORANGE', 'Orange'),
        ('YELLOW', 'Yellow'),

    ]
    colors = models.CharField(max_length=10, 
                                choices=COLORS_CHOICE, default='Black')
    CONDITION_CHOICE = [
        ('NEW', 'New'),
        ('DEMO', 'Demo'),
        ('USED', 'Used'),
    ]
    condition = models.CharField(max_length=10, 
                                choices=CONDITION_CHOICE, default='NEW')

    def __st__(self):
        return self.name

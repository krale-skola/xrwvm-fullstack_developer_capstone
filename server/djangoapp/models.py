# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


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

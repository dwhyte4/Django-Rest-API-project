from django.db import models
from django.conf import settings
from django.utils import timezone

class Users(models.Model):
	name = models.CharField(max_length = 40, null = False)
	email = models.CharField(max_length = 40, null = False)
	contact_number = models.CharField(max_length = 15, null = False)
	picture = models.ImageField(upload_to = 'images/users_img', blank = True)
	password = models.CharField(max_length = 20, null = False)
	address = models.CharField(max_length = 250, null = False)
	postcode = models.CharField(max_length = 30, null = False)
	terms_conditions = models.BooleanField(default = False, null = False)
	validation = models.BooleanField(default = False, null = False)
	company = models.BooleanField(default = False, null = False)

class Allergies(models.Model):
	allergic_ingredients = models.CharField(max_length = 30)

class Requests(models.Model):
	food = models.CharField(max_length = 50)
	picture = models.ForeignKey(Users,on_delete=models.CASCADE, related_name= 'Requests_picture')
	comment = models.TextField(blank = True, null = False)
	temperature = models.BooleanField(blank = False)
	time = models.TimeField(default=timezone.now)
	name = models.ForeignKey(Users, on_delete=models.CASCADE, related_name= 'Requests_name')
	contact_number = models.ForeignKey(Users, on_delete=models.CASCADE, related_name= 'Requests_contact_number')
	address = models.ForeignKey(Users, on_delete=models.CASCADE, related_name= 'Requests_address')
	postcode = models.ForeignKey(Users, on_delete=models.CASCADE, related_name= 'Requests_postcode')
	allergic_ingredients = models.ForeignKey(Allergies, on_delete=models.CASCADE, related_name= 'Requests_ingredient')

        # for future reference:
        # 'tempreture' should be spelt 'temperature', and could be changed to 'hot' or 'cold' if it is a boolean...
        #   - implies a numeric value, e.g. 64.2 degrees
        # no need for a city field - can be part of the address field
        # ingredient could be renamed to allergic_ingredients - since it references the allergies table


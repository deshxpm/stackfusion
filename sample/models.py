from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??)',
                             message="Ensure Phone number must be 10 digits: EX: '9999999999'.")




class SampleDetail(models.Model):
	name = models.CharField(max_length=250, blank=True, null=True)
	dob	= models.DateField(null=True, blank=True)
	email = models.EmailField(blank=True, null=True)
	phone = models.CharField(max_length=10, default='', validators=[phone_regex], unique=True)
	added_date = models.DateField(auto_now_add=True)
	active = models.BooleanField(default=True)	

	def __str__(self):
		return str(self.name)

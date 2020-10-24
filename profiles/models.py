from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class Company(models.Model):
    # I left 'company_' in front of the 'name' to make it easier to differ from
    # user's "full_name". The other one is left to keep consistency in names
    company_name = models.CharField(max_length=50, null=False)
    company_team = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class UserProfile(models.Model):
    """
    User profile to store basic information about user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    default_full_name = models.CharField(max_length=50, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label="Country", null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update user profile, just like the name describes"""

    if created:
        UserProfile.objects.create(user=instance)
        Company.objects.create()
    # Existing users: just save the profile
    instance.userprofile.save()
    # instance.company.save()

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    # User object must be passed in the class as a primary key

    user = models.OneToOneField(User,on_delete=models.CASCADE,)

    # Add other UserAttribute

    # It takes the URL link from user for other sites etc
    portfolio_site = models.URLField(blank=True)

    #create a profile folder inside the media folder..
    #.. which would store profile pcis from user
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # This function is to print the user instance of the User class..
    #..  & username attribute of the User
    def __str__(self):

        return self.user.username

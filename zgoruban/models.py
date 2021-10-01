from django.db import models
from djrichtextfield.models import RichTextField
class demo_images(models.Model):
    image = models.FileField(null=True)

class Go_Ruban_Motive(models.Model):
    motive = models.TextField(null=True)

class Camps(models.Model):
    camp_name = models.CharField(max_length=30,null=True)
    no_of_days = models.IntegerField( null=True)
    date = models.DateField(null=True)
    image = models.FileField(null=True)
    detail = models.TextField(null=True,max_length=300)
    content = RichTextField(null=True)

    def __str__(self):
        return self.camp_name

class CAMPparticipants(models.Model):
    imag = models.ForeignKey(Camps, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, null=True)
    designation = models.CharField(max_length=30,null=True)
    image1 = models.FileField(null=True)

class About(models.Model):
    heading = models.CharField(max_length=30,null=True)
    paragraph = models.TextField( null=True)
    image1 = models.FileField(null=True)

    def __str__(self):
        return self.heading

class Team(models.Model):
    name = models.CharField(max_length=30,null=True)
    designation = models.TextField( null=True)
    image1 = models.FileField(null=True)
    dob = models.DateField(null=True)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return self.name




class Year_categoryss(models.Model):
    Year = models.IntegerField(null=True)


class GALLERYSS(models.Model):
    years = models.ForeignKey(Year_categoryss, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(null=True)

class NEWSS(models.Model):
    years = models.ForeignKey(Year_categoryss, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(null=True)

class EVENTS(models.Model):
    years = models.ForeignKey(Year_categoryss, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(null=True)



class BLOGS(models.Model):
    Heading = models.TextField(max_length=150,null=True)
    image1 = models.FileField(null=True)
    Detail = models.TextField(max_length=200,null=True)
    Discription = RichTextField(null=True)
    date = models.DateTimeField(auto_now=True)



class TESTIMONY(models.Model):
    name = models.CharField(max_length=30, null=True)
    position = models.CharField(max_length=30,null=True)
    image = models.FileField(null=True)
    Detail = models.TextField(null=True)
    facebook = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    instagram = models.URLField(null=True)
    twitter = models.URLField(null=True)

    def __str__(self):
        return self.name

class BANNER_ABOUT(models.Model):
    Discription = RichTextField(null=True)

class BANNER_CAMPS(models.Model):
    Discription = RichTextField(null=True)

class BANNER_ANANTMANDI(models.Model):
    Discription = RichTextField(null=True)

class BANNER_STORE(models.Model):
    Discription = RichTextField(null=True)

class EMAIL_LETTERS(models.Model):
    mubmail = models.EmailField(null=True)

class EMIMG(models.Model):
    imagess = models.FileField()
   

class Oppurtunities(models.Model):
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    mob = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    role = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.fname

class Contact(models.Model):
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    mob = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.fname


class TERMS_CONDITIONSs(models.Model):
    cont = RichTextField(null=True)

class PRIVACY_POLICYs(models.Model):
    cont = RichTextField(null=True)

class PAYMENT_PROCEDUREs(models.Model):
    cont = RichTextField(null=True)
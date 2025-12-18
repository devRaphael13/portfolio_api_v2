from django.db import models
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    profile_img = CloudinaryField(resource_type="image", folder="portfolio/profile_images/", blank=True, null=True)
    about = models.TextField()
    resume = CloudinaryField(resource_type="auto", folder="portfolio/resumes/")
    years_of_exp = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Service(models.Model):
    name = models.CharField(max_length=120)
    tag_line = models.CharField(max_length=240)
    features = ArrayField(models.CharField(max_length=240), size=4)
    icon_name = models.CharField(max_length=50)
    icon_library = models.CharField(max_length=10)
    icon_colour = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name
    
class Technology(models.Model):
    name = models.CharField(max_length=120)
    icon_name = models.CharField(max_length=50)
    icon_library = models.CharField(max_length=10)
    icon_colour = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=120)
    link = models.URLField(blank=True, null=True)
    position = models.CharField(max_length=120)
    description = models.TextField()
    tech_used = models.ManyToManyField(Technology, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.company

class Project(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    thumbnail = CloudinaryField(resource_type="image", folder="portfolio/project_thumbnails/", blank=True, null=True)
    repo_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    tech_used = models.ManyToManyField(Technology, blank=True)
    featured = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-start_date"]



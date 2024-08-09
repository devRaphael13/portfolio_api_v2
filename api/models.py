from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=120)

class Experience(models.Model):
    company = models.CharField(max_length=120)
    position = models.CharField(max_length=120)
    description = models.TextField()
    tech_used = models.ManyToManyField(Technology, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

class Project(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    proj_type = models.CharField(max_length=20, choices=[["p", "Personal"], ["w", "Work"]])
    employer = models.ForeignKey(Experience, blank=True, null=True)
    link = models.URLField()
    tech_used = models.ManyToManyField(Technology, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()



from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=120)

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
    link = models.URLField(blank=True, null=True)
    tech_used = models.ManyToManyField(Technology, blank=True)
    featured = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-start_date"]



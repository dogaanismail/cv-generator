from django.db import models


class Interests(models.Model):
    interest = models.CharField(max_length=200)


class Education(models.Model):
    university = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    gpa = models.DecimalField(max_digits=5, decimal_places=2)


class WorkExperience(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    other_information = models.TextField(max_length=2000)


class Skills(models.Model):
    skills = models.CharField(max_length=200)


class CV_data(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    about_yourself = models.TextField(max_length=2000)

    skills = models.ManyToManyField(Skills)
    interests = models.ManyToManyField(Interests)
    education = models.ManyToManyField(Education)
    work_experience = models.ManyToManyField(WorkExperience)

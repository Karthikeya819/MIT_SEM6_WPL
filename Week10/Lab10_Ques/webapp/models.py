from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    visits = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Lives(models.Model):
    person_name = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.person_name


class Works(models.Model):
    person_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.person_name

class Institute(models.Model):
    institute_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    no_of_courses = models.IntegerField()

    def __str__(self):
        return self.name

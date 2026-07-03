from django.db import models

class Student(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField()
    gender = models.CharField(
        max_length=10,
        choices=gender_choices
    )
    age = models.IntegerField(null=True, blank=True)
    student_bio = models.TextField()
# Create your models here.
class Author(models.Model):
  author_name = models.CharField(max_length=50)

  def __str__(self):
    return self.author_name

class Book(models.Model):
  author = models.OneToOneField(Author ,on_delete=models.CASCADE) # author id is saved internally
  book_name = models.CharField(max_length=50)

class Brand(models.Model):
  brand_name = models.CharField(max_length=50)
  country_name = models.CharField(max_length=50 ,default="IN")

  def __str__(self):
    return self.brand_name

class Product(models.Model): 
  brand = models.ForeignKey(Brand,max_length=50, on_delete = models.CASCADE)
  product_name = models.CharField(max_length=50)

  def __str__(self):
    return self.product_name

class Studenttable(models.Model):
  name = models.CharField(max_length=50)
  phone = models.CharField(max_length=50)
  age = models.IntegerField()
  dob = models.DateField()

  def __str__(self):
    return self.name
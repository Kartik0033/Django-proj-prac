from django.db import models


class College(models.Model):
    college_name = models.CharField(max_length=50)
    college_address = models.CharField(max_length=60)


class Student(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE,blank=True, null=True)
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


class Skills(models.Model):
  skill_name = models.CharField(max_length=50)

  def __str__(self):
    return self.skill_name
  
class Person(models.Model):
  person_name = models.CharField(max_length=50)
  skill = models.ManyToManyField(Skills,blank=True)
  
  def __str__(self):
    return self.person_name  

class Studenttable(models.Model):
  name = models.CharField(max_length=50)
  phone = models.CharField(max_length=50)
  gender = models.CharField(max_length=50,blank=True,null=True)
  file = models.FileField(upload_to='files/',blank=True,null=True)
  
  def __str__(self):
    return self.name
  

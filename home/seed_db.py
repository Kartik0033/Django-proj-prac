from faker import Faker
from home.models import College, Student
import random

fake = Faker('en_IN')

def dbseeder(records = 10)-> None:
   
   students = Student.objects.all()
   for _ in range(records):
      college = random.choice(College.objects.all())
      name = fake.name()
      mobile_number = fake.phone_number()
      email = fake.email()
      gender = random.choice(['Male', 'Female'])
      age = random.randint(18, 30)
      student_bio = fake.text()

      Student.objects.create(
         college=college,
          name=name,
          mobile_number=mobile_number,
          email=email,
          gender=gender,
          age=age,
          student_bio=student_bio
      )
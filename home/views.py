from django.shortcuts import redirect, render
from django.http import HttpResponse
from home.forms import StudentForm, StudentModelForm
from home.models import Studenttable,Student  
from django.db.models import Q
#context = {
  #   # "form": StudentForm()
  #   "form": StudentModelForm()
  # }

  # if request.method == "POST":
  #   print("POst")
  #   form = StudentModelForm(request.POST)
    
  #   if form.is_valid():
  #     form = form.save()
  #     # d1 = form.cleaned_data
  #     # d1.save()
      
  #     # Studenttable.objects.create(
  #     #   name = d1['name'],
  #     #   phone = d1['phone'],
  #     #   age = d1['age'],
  #     #   dob = d1['dob']
  #     # )

# Create your views here.
def home(request):  # sourcery skip: extract-method, remove-unnecessary-else
  # data taken from the form by attribute name of the input field in html form
  if request.method == "POST":
    name = request.POST.get("name")
    phone = request.POST.get("mobilenumber")
    gender = request.POST.get("gender")
    file = request.FILES.get("file")

    Studenttable.objects.create(
      name=name,
      phone=phone,
      gender=gender,
      file=file
    )

    return redirect("thankyou/")
  
  else :
    print("GET")
    print(request)

  return  render(request,"home.html")

  
def contact(request):
  return render(request,"contact.html")

def DynamicResponse(request,number):  #the number is variable taken from url patterns

  count = {}

  for i in str(number):
    if i in count:
      count[i] += 1
    else:
      count[i] = 1

  print(count)
  
  return HttpResponse(f"this is response dynamic the number is {number}")

def thankyou(request):

  return render(request,"thank.html") 
# render function send the request obj to django then which is sent as messg to browser

def search(request):
  students = Student.objects.all()
  
  search = request.GET.get('search')
  age = request.GET.get('age')
  print(search)
  if search:
    students = students.filter(
    Q(name__icontains=search)|
    Q(college__college_name__icontains=search)|
    Q(email__endswith = search )|
    Q(gender__icontains = search)
    ) 

  if age:
    if age == "1":
      students = students.filter( age__gte = 18 , age__lte = 21 ).order_by("age")
    if age == "2":
      students = students.filter( age__gte = 21 , age__lte = 23).order_by("age")
    if age == "3":
      students = students.filter( age__gte = 23 , age__lte = 25).order_by("age")

  context = {
    "students":students,
    "search":search
  }

  return render(request, "search.html",context)


from django.shortcuts import redirect, render
from django.http import HttpResponse
from home.forms import StudentForm, StudentModelForm
from home.models import Studenttable,Student
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
# render function send the request obj to django in whic req obj contains the string of html  which is sent as messg to browser and reqeust nee
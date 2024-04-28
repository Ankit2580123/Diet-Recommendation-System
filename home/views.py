from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import signup as Signup,ContactsInformations,DietForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
def index(request):
#    return HttpResponse('this is Index pages')
   return render(request,'index.html')

def contact(request):
   if request.method=='POST':
              name=request.POST['name']
              email=request.POST['email']
              message=request.POST['message']
              my_user=ContactsInformations(name=name,email=email,message=message)
              my_user.save()
              messages.success(request,"Thanks For Contacts Us We have received your Quiry.")

   return render(request,'contact.html')

def dietform(request):
    
        
     return render(request,'form.html')

vegfoods=['Beans and lentils','Whole grains (whole-wheat oats brown rice and more)','Fruits (Apples Bananas Orange)'
          ,'Green Vegetables (Broccoli Spinach more)', 'Dairy (yogurt,cheese and milk)','Soy (tofu edamame tempeh)',
          'Nuts & Seeds (cashew almonds and Chia Seeds)'] 

nonveg=['Chicken','Eggs','Meat','Fish']

vegan=['Beans and lentils', 'Chicken','Whole grains (whole-wheat oats brown rice and etc)','Fruits (Apples Bananas Orange)'
          ,'Green Vegetables (Broccoli Spinach more)','Eggs' 'Dairy (yogurt,cheese and milk)','Soy (tofu edamame tempeh)',
          'Meat','Fish','Nuts & Seeds (cashew almonds and Chia Seeds)']

diabetesVegFoods=['Non-starchy vegetables','leafy greens','Whole Grains','Fruits','Nuts & Seeds',
               'Healthy fats Foods','Herbs and spices','Low fat Dairy']

diabetesNonVegFoods=['Lean Meat','Fish','Eggs']
diabetesVeganFoods=['Non-starchy vegetables','leafy greens','Lean Meat','Fish','Eggs', 'Whole Grains','Fruits','Nuts & Seeds',
               'Healthy fats Foods','Herbs and spices','Low fat Dairy']

def recommendation(request):
          if request.method=="POST":
                  name=request.POST['name']
                  gender=request.POST['gender']
                  age=request.POST['age']
                  bmi=request.POST['bmi']
                  diseases=request.POST['diseases']
                  foodtype=request.POST['foodtype']
                  user=DietForm(name=name,gender=gender,age=age,bmi=bmi,diseases=diseases,
                           foodType=foodtype)
                  user.save()
          if diseases =='No Diseases' and foodtype=='Veg':
                final=vegfoods
          elif diseases=='No Diseases' and foodtype=='Non Veg':
                final=nonveg
          elif diseases=='No Diseases' and foodtype=='Both(Veg and Non veg)':
                final=vegan
          elif diseases=='Obesity' and foodtype=='Veg':
                final= vegfoods   
                message='Avoid to Eat High Calories Foods'
          elif diseases=='Obesity' and foodtype=='Non Veg':
               #  nonveg=['Chicken','Only Eggs white','Fish']
                nonveg[1]="Only Eggs white"
                nonveg.remove("Meat")
                final=nonveg
                message='Avoid to Eat High Calories Foods'
          elif diseases=='Obesity' and foodtype=='Both(Veg and Non veg)':
               #  vegan=['Beans and lentils', 'Chicken','Whole grains (whole-wheat oats brown rice and more)','Fruits (Apples Bananas Orange)'
               #  ,'Green Vegetables (Broccoli Spinach more)','Eggs Whites','Low Fat Diary Products','Soy (tofu edamame tempeh)',
               #   'Fish','Nuts & Seeds (cashew almonds and Chia Seeds)']
                vegan[5]="Only eggs Whites"
                vegan[6]="Low Fat Diary Products"
                vegan.remove('Meat')
                message='Avoid to Eat High Calories Foods'
                final=vegan
          elif diseases=='Diabetes' and foodtype=='Veg':
                final=diabetesVegFoods
          elif diseases=='Diabetes' and foodtype=='Non Veg':
                final=diabetesNonVegFoods
          elif diseases=='Diabetes' and foodtype=='Both(Veg and Non veg)':
                final=diabetesVeganFoods
          
          return render(request,'recommendation.html',{'user':name,'gender':gender,'age':age,'bmi':bmi,
                                                       'diseases':diseases,'foodtype':foodtype,
                                                       'ans':final
                                                       })
                 
       

def login(request):
   if request.method=='POST':
              username=request.POST['username']
              password1=request.POST['password']
            #   user=authenticate(username=username,password=password1)
              user=Signup.objects.filter(username=username,password=password1).first()
              
              
            #   print(user)
              if user is not None:
                   messages.success(request,"Successfully Logged In!")
                   return render(request,'home.html',{'title':'You are Successfully Login','data': username})
                   
              else:
                   messages.error(request,"Bad Credentials You are Enter Wrong Password!")
                   return redirect('login')
        
   return render(request,'login.html')

def signup(request):
         if request.method=='POST':
              username=request.POST['username']
              mobile_no=request.POST['mobile_no']
              email=request.POST['email']
              password1=request.POST['password1']
              password2=request.POST['password2']
              my_user=Signup(username=username,mobile_no=mobile_no,email=email,password=password1)
              
              if password1!=password2:
                   messages.error(request,"Your Password are not Matched with Confirm Password!")
                   
              else:

                  if Signup.objects.filter(username=username).exists():
                        messages.error(request,"Username Already Taken")
                  elif Signup.objects.filter(email=email).exists():
                        messages.error(request,"Email Already Taken")
                  else:
                        my_user.save()
                        messages.success(request,"You are Successfully Registered!")
                        
                  

                  #Email Message
                        subject = 'welcome to techno fitness'
                        message = f'Hi {my_user.username}, Thank you for registering.'
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list =[my_user.email, ]
                        send_mail( subject, message, email_from, recipient_list) 
                        return redirect('login')
                        
                   
                   
                  #  return redirect('/login')  
         return render(request,'signup.html')
    
def user_list(request):
    # data=Register.objects.all()
    # data=Register.objects.filter(mobile_no=7903493441).values()
    # data=Register.objects.get(id=1)
    data=Signup.objects.all()
    return render(request,'userlist.html',{'title':'User List','data':data})

@login_required(login_url='/login')
def home(request):
   return render(request,'home.html') 

def bmi(request):
     return render(request,'bmi.html')

def handleLogout(request):
        logout(request)
        messages.success(request,"You are Successfully Logout")
        return redirect('index')
def delete_user(request,id):
    data=Signup.objects.get(id=id)
    data.delete()
    messages.success(request,"is Deleted!")
    return redirect('/userlist')

def editUser(request,id):
    data=Signup.objects.filter(id=id).first()
    return render(request,'editUser.html',{'data':data})


def update_user(request):
    username=request.POST['username']
    mobile_no=request.POST['mobile_no'] 
    email=request.POST['email'] 
    password=request.POST['password'] 
    editid=request.POST['editid'] 
    data=Signup.objects.get(id=editid)
    data.username=username
    data.mobile_no=mobile_no
    data.email=email
    data.password=password
    data.save()
    messages.success(request," Is Updated!")
    return redirect('/userlist',{'user':username})
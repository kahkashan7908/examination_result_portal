from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import re
import faker
fake=faker.Faker()
from.models import tenthData,interData,degreeData,btechData

def loginPage(request):
    if request.method=='POST':
        username1=request.POST['Name']
        passwords=request.POST['pass']
        user=authenticate(request,username=username1,password=passwords)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('mainPage')
        else:
            context={'msg':'Invalid username or password'}
            return render(request,'login.html',context)   
    return render(request,'login.html')

def signupPage(request):
    if request.method=='POST':
        username=request.POST['name']
        email=request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        password=re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",password1)
        if password is None:
            context={'massage1':'The password must contain at least one digit, one special character, one uppercase letter and minimum length shoud be 8 character.'}
            return render(request,'signup.html',context)
        else:
             if password1!=password2:
                 context={'massage2':'The password and confirm password do not match'}
                 return render(request,'signup.html',context)
             else:
               my_user=User.objects.create_user(username,email,password1)
               my_user.save()
               return redirect('loginPage')  
    return render(request,'signup.html')


def mainPage(request):
    return render(request,'main.html')

# fetching data for 10th result
def tenthPage(request):
    if request.method=='GET':
        return render(request,'resultCheck.html')
    else:
        hallTicket=request.POST['htk']
        data = tenthData.objects.filter(hall_ticket=hallTicket).first()
        #data=tenthData.objects.get(hall_ticket=hallTicket)
        if data is None:
            context={'tokenmsg':'Please enter a valid hall ticket'}
            return render(request,'resultCheck.html',context)
        s1=data.urdu
        s2=data.hindi
        s3=data.mathematics
        s4=data.science
        s5=data.social_science
        t=s1+s2+s3+s4+s5

        if s1>=30:
            result1='PASS'
        else:
            result1='FAIL'
        if s2>=30:
            result2='PASS'
        else:
            result2='FAIL'
        if s3>=30:
            result3='PASS'
        else:
            result3='FAIL'
        if s4>=30:
            result4='PASS'
        else:
            result4='FAIL'
        if s5>=30:
            result5='PASS'
        else:
            result5='FAIL'
        
        if t>400 and t<=500 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="A+"
            #status='PASS'
        elif t>=300 and t<=400 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="A"
        elif t>200 and t<300 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="B"
        elif t>150 and t<=200 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g='C'
        else:
            status='FAIL'
            g='D'
        return render(request,'tenthresult.html',{'data':data,'result':status,'grade':g,
                                                  'marks1':result1,'marks2':result2,'marks3':result3,
                                                  'marks4':result4,'marks5':result5,'total':t}) 

#adding data in database for 10th 
def addTenData(request):
    count=20010
    for i in range(200):
         count+=1
         tenthData(
            name=fake.name(),
            hall_ticket=count,
            urdu=fake.random_element(elements=range(30,100)),
            hindi=fake.random_element(elements=range(30,100)),
            mathematics=fake.random_element(elements=range(15,100)),
            science=fake.random_element(elements=range(25,100)),
            social_science=fake.random_element(elements=range(20,100)),
         ).save()
    return HttpResponse('Added 10th data successfully')

#fetching data for 12th result
def interPage(request):
    if request.method=='GET':
        return render(request,'resultCheck.html')
    else:
         hallTicket=request.POST['htk']
         data = interData.objects.filter(hall_ticket=hallTicket).first()
         if data is None:
            context={'tokenmsg':'Please enter a valid hall ticket'}
            return render(request,'resultCheck.html',context)
         #data=interData.objects.get(hall_ticket=hallTicket)
         s1=data.hindi
         s2=data.english
         s3=data.physics
         s4=data.chemistry
         s5=data.mathematics
         t=s1+s2+s3+s4+s5
         if s1>=30:
            result1='PASS'
         else:
            result1='FAIL'
         if s2>=30:
            result2='PASS'
         else:
            result2='FAIL'
         if s3>=30:
            result3='PASS'
         else:
            result3='FAIL'
         if s4>=30:
            result4='PASS'
         else:
            result4='FAIL'
         if s5>=30:
            result5='PASS'
         else:
            result5='FAIL'
         if t>400 and t<=500 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="A+"
            #status='PASS'
         elif t>=300 and t<=400 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="A"
         elif t>200 and t<300 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="B"
         elif t>150 and t<=200 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g='C'
         else:
            status='FAIL'
            g='D'
         return render(request,'interresult.html',{'data':data,'result':status,'grade':g,
                                                   'marks1':result1,'marks2':result2,'marks3':result3,
                                                   'marks4':result4,'marks5':result5,'total':t})


#adding data in database for 12th 
def addinterData(request):
    count=30010
    for i in range(200):
         count+=1
         interData(
            name=fake.name(),
            hall_ticket=count,
            hindi=fake.random_element(elements=range(30,100)),
            english=fake.random_element(elements=range(30,100)),
            physics=fake.random_element(elements=range(15,100)),
            chemistry=fake.random_element(elements=range(25,100)),
            mathematics=fake.random_element(elements=range(20,100)),
         ).save()
    return HttpResponse('Added 12th data successfully')


#fetching data for degree  result
def degrePage(request):
    if request.method=='GET':
        return render(request,'resultCheck.html')
    else:
         hallTicket=request.POST['htk']
         data = degreeData.objects.filter(hall_ticket=hallTicket).first()
         if data is None:
            context={'tokenmsg':'Please enter a valid hall ticket'}
            return render(request,'resultCheck.html',context)
         #data=degreeData.objects.get(hall_ticket=hallTicket)
         s1=data.hindi
         s2=data.english
         s3=data.history
         s4=data.Political_Science
         s5=data.geography
         t=s1+s2+s3+s4+s5
         if s1>=30:
            result1='PASS'
         else:
            result1='FAIL'
         if s2>=30:
            result2='PASS'
         else:
            result2='FAIL'
         if s3>=30:
            result3='PASS'
         else:
            result3='FAIL'
         if s4>=30:
            result4='PASS'
         else:
            result4='FAIL'
         if s5>=30:
            result5='PASS'
         else:
            result5='FAIL'
         if t>400 and t<=500 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="A+"
            #status='PASS'
         elif t>=300 and t<=400 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="A"
         elif t>200 and t<300 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="B"
         elif t>150 and t<=200 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g='C'
         else:
            status='FAIL'
            g='D'
         return render(request,'degreeresult.html',{'data':data,'result':status,
                                                    'grade':g,'marks1':result1,'marks2':result2,'marks3':result3,
                                                    'marks4':result4,'marks5':result5,'total':t})

#adding data in database for degree 
def adddegreeData(request):
    count=40010
    for i in range(200):
         count+=1
         degreeData(
            name=fake.name(),
            hall_ticket=count,
            hindi=fake.random_element(elements=range(30,100)),
            english=fake.random_element(elements=range(30,100)),
            history=fake.random_element(elements=range(15,100)),
            Political_Science=fake.random_element(elements=range(25,100)),
            geography=fake.random_element(elements=range(20,100)),
         ).save()
    return HttpResponse('Added degree data successfully')

#fetching data for btech result
def btechPage(request):
    if request.method=='GET':
        return render(request,'resultCheck.html')
    else:
         hallTicket=request.POST['htk']
         data = btechData.objects.filter(hall_ticket=hallTicket).first()
         #data=btechData.objects.get(hall_ticket=hallTicket)
         if data is None:
            context={'tokenmsg':'Please enter a valid hall ticket'}
            return render(request,'resultCheck.html',context)
         s1=data.english
         s2=data.chemistry
         s3=data.mathematics
         s4=data.machine
         s5=data.basic_electrical
         t=s1+s2+s3+s4+s5
         if s1>=30:
            result1='PASS'
         else:
            result1='FAIL'
         if s2>=30:
            result2='PASS'
         else:
            result2='FAIL'
         if s3>=30:
            result3='PASS'
         else:
            result3='FAIL'
         if s4>=30:
            result4='PASS'
         else:
            result4='FAIL'
         if s5>=30:
            result5='PASS'
         else:
            result5='FAIL'
         if t>400 and t<=500 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="A+"
            #status='PASS'
         elif t>=300 and t<=400 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="A"
         elif t>200 and t<300 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g="B"
         elif t>150 and t<=200 and s1>=30 and s2>=30 and s3>=30 and s4>=30 and s5>=30:
            status='PASS'
            g='C'
         else:
            status='FAIL'
            g='D'
         return render(request,'btechresult.html',{'data':data,'result':status,'grade':g,
                                                    'marks1':result1,'marks2':result2,'marks3':result3,
                                                    'marks4':result4,'marks5':result5,'total':t})



#adding data in database for btech
def adddbtechData(request):
    count=50010
    for i in range(200):
         count+=1
         btechData(
            name=fake.name(),
            hall_ticket=count,
            english=fake.random_element(elements=range(30,100)),
            chemistry=fake.random_element(elements=range(30,100)),
            mathematics=fake.random_element(elements=range(15,100)),
            machine=fake.random_element(elements=range(25,100)),
            basic_electrical=fake.random_element(elements=range(20,100)),
         ).save()
    return HttpResponse('Added degree btech successfully')
    



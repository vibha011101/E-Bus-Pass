from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect,csrf_exempt
# from django.utils.datastructures import MultiValueDictKeyError
from .models import student,place,bus,payment,goes_to
from django.contrib.auth.hashers import make_password
@csrf_exempt
def home(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        print(user)

        if user is not None:
            login(request,user)
            us=request.user.username
            det=student.objects.filter(usn=us).values().first()  
            lst=list(det.values())
            # pay=payment.objects.all()
            pay=payment.objects.filter(usn=us).values().first()  
            lst1=list(pay.values())
            # print(lst1)
            bus1=bus.objects.get(id=lst1[2])
            return render(request,'index.html',{'usn':lst[0],'name':lst[1],'branch':lst[4],'sem':lst[5],'image':lst[6],'reciptno':lst1[0],'pay':lst1[1],'validity':lst1[4],'busno':bus1})
        # else:
        #     messages.error(request,'ERROR in password/username')
        #     return render(request,'contact.html')

    else:
        return render(request,'home.html')

def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact.html')

def logout(request):
       try:
           del request.session['user']
           return render(request,'home.html')
       except:
           return render(request,'home.html')
        # return redirect('login')   

@csrf_exempt
def signup(request):
    if request.method == 'POST':

        usn= request.POST.get('usn')    
        if User.objects.filter(username = usn).first():
            messages.error(request, "This username is already taken")
            return redirect('/')        #put name in input of forms in the brackets
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        branch=request.POST.get('branch')
        sem=request.POST.get('sem')
        image=request.FILES.get('image')
        password=request.POST.get('password')

        user =User.objects.create(username=usn,email=email,password=make_password(password))
        user.save()
        stud = student.objects.create(usn=usn,sname=name,saddress=address,email=email,branch=branch,sem=sem,photo=image,password=password)
        stud.save()
        # det=student.objects.filter(usn=usn).values().first()  
        # lst=list(det.values())
        # cv2.imwrite(r'C:\Users\vibha\Desktop\back\epass\media\student',lst[6])   
        return render(request,'home.html')

    else:
        return render(request,'signup.html')    



from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

#from myproject import Service
from .forms import UsersForm
from service.models import Service
from django.core.paginator import Paginator
from django.core.mail import send_mail
def homepage(request):
    servicesData=Service.objects.all().order_by('service_title')[2:5]
   # for a in servicesData:
    #    print(a.service_icon)
   # print(Service)

    data={
        'servicesData':servicesData
    }
   

    return render(request,"index.html",data)


def aboutUs(request):
    return render(request,"aboutus.html") 

def aboutABC(request):
    return HttpResponse("<b>This is 2nd function in viwes<b>")
def aboutdetails(requsest,aboutID):
    return HttpResponse(aboutID) 

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2        
    
    except:
        c="Invalid opr...."  
        print(c)     
    return render(request,"calculator.html",{'c':c})


def UserForm(request):
    return render(request,"Userform.html",{'c':''}) 

def marksheet(request):
    if request.method == "POST":
        s1 = int(request.POST.get("subject1"))
        s2 = int(request.POST.get("subject2"))
        s3 = int(request.POST.get("subject3"))
        s4 = int(request.POST.get("subject4"))
        s5 = int(request.POST.get("subject5"))

        t = s1 + s2 + s3 + s4 + s5
        p = t * 100 / 500

        if p >= 60:
            d = "First Division"
        elif p >= 48:
            d = "Second Division"
        elif p >= 33:
            d = "Third Division"
        else:
            d = "Fail"            

        data = {
            'ss': s1,
            'total': t,
            'percentage': p,
            'Division': d,
        }

        return render(request, "marksheet.html", data)

    return render(request, "marksheet.html")

def saveevenodd(request):
    c=''
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request,"evenodd.html",{'error':True})


        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="even number"
        else:
            c="odd number"    
    return render(request,"evenodd.html",{'c':c})

from django.shortcuts import render

def UserForm(request):
    finalans = 0
    fn=UsersForm
   # fn=UserForm()
    data={'form':fn}
    if request.method == 'POST':
        try:
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1 + n2
            data={
                'form':fn,
                'output':finalans
            }
            return HttpResponseRedirect('/about-us/')
        except (TypeError, ValueError):
            pass
    return render(request, "Userform.html", data)



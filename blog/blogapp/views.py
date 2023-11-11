from django.shortcuts import render,HttpResponse,redirect
from blogapp.models import Blog,Student
import datetime
from blogapp.forms import StudentFormClass,StudentModelFormClass,UserRegister
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
# def homepage(request):
#     return HttpResponse("Hello from Home View")

def aboutpage(request):
    # return HttpResponse("Hello from About View")
    print("In about page")
    # return redirect('/contact')
    # return HttpResponse("In about page")
    return render(request,'about-us.html')
    # return redirect("/about-us.html")

def testpage(request):
    return HttpResponse("Test View")

def contactpage(request):
    # return HttpResponse("Hello from Contact View")
    return render(request,'about-us.html')

def edit(request,rid):
    # print("ID to be edited:",rid)
    if request.method=="GET":
        b=Blog.objects.filter(id=rid)
        context={}
        context['blog']=b
        # return HttpResponse("ID to be edited:"+rid)
        return render(request,'editblog.html',context)
    else:
        # Fetch new changes from Form
        utitle=request.POST['title']
        udetail=request.POST['detail']
        ucat=request.POST['cat']

        # print("Updated title:",utitle)
        # print("Updated detail:",udetail)
        # print("Updated Category:",ucat)
        # return HttpResponse("Updated details Fetched")

        b=Blog.objects.filter(id=rid)
        b.update(title=utitle,detail=udetail,cat=ucat)
        return redirect("/userdashboard")


def delete(request,rid):
    # print("ID to be deleted:",rid)
    b=Blog.objects.filter(id=rid)
    # print(b)
    b.delete() # to delete object or row from table
    # return HttpResponse("Object to be deleted is fetched:"+rid)
    return redirect('/userdashboard')
'''
def homepage(request,x,y):
    print("Value of x:",x)
    print("Value of y:",y)
    return HttpResponse("Value of x and y:"+x+" "+y)
'''
def helloview(request):
    context={}
    context['uname']="itvedant"
    context['x']=1000
    context['y']=200
    context['l']=[10,20,'Itvedant',90.8]
    return render(request,'hello.html',context)

# blog application view function start
def homepage(request):
    b=Blog.objects.filter(is_published=True)
    context={}
    context["blog"]=b
    return render(request,'home.html',context)

def user_dashboard(request):
    # print("Logged in user object:",request.user)
    # print("Logged in User ID:",request.user.id)
    # print("Logged in User First name:",request.user.first_name)
    # print("Logged in User Last name:",request.user.last_name)
    # b=Blog.objects.all() #select * frmo blogapp_blog
    b=Blog.objects.filter(uid=request.user.id)
    '''
    print(b)
    for x in b:
        print(x)
        print("ID:",x.id)
        print("Title:",x.title)
        print("Detail:",x.detail)
        print("Cat:",x.cat)
        print("Created_at:",x.created_at)
        print()
    '''
    context={}
    context['blogs']=b
    return render(request,'dashboard.html',context)


def create_blog(request):
    # print("Method Type:",request.method)
    if request.method=="GET":#GET==GET T | POST == GET F
        # print("IN GET section")
        return render(request,'create_blog.html')
    else:
        # print("In POST section")
        # Fetching data from Form request using POST dictionary
        btitle=request.POST['title']
        bdet=request.POST['detail']
        bcat=request.POST['cat']

        # print("Title:",btitle)
        # print("Detail:",bdet)
        # print("Category:",bcat)

        b=Blog.objects.create(title=btitle,detail=bdet,cat=bcat,uid=request.user.id,created_at=datetime.datetime.now())
        b.save()

        # return HttpResponse("Data Inserted Successfully")
        return redirect('/userdashboard')

def view_details(request,rid):
    # print("Id to be used for details: ",rid)
    b=Blog.objects.filter(id=rid)
    # print(b)
    # return HttpResponse("Id fetched "+rid)
    context={}
    context['blog']=b
    return render(request,'blog_details.html',context)

def is_published(request,status,rid):
    # print("Status is:",status)
    # print("Id to be edited:",rid)

    b=Blog.objects.filter(id=rid)
    # print(b)
    context={}
    context['blog']=b
    if status == "P":
        b.update(is_published=True)
        context['pmsg']="Blog has been Published Succesfully"
        # return HttpResponse("Blog has been Published Succesfully")
    else:
        b.update(is_published=False)
        context['umsg']="Blog has been Unpublished"
        # return HttpResponse("Blog has been Unpublished")
    return render(request,"blog_details.html",context)

def setcookies(request):
    res=render(request,"set_cookies.html")
    print("Response Object:",res)
    res.set_cookie("name","ITVEDANT")
    return res

def getcookies(request):
    cdata=request.COOKIES["name"]
    print("Data in the cookies:",cdata)
    context={}
    context['data']=cdata
    return render(request,'getcookies.html',context)

def setsession(request):
    request.session['learning']="Session and Cookies"
    return render(request,'set_session.html')

def getsession(request):
    sdata=request.session["learning"]
    print("Data in the session",sdata)
    context={}
    context['data']=sdata
    return render(request,'get_session.html',context)

def djangoForm(request):
    context={}
    if request.method=="GET":
        s=StudentFormClass()
        # print(s)
        context['fm']=s
        # return HttpResponse("forms object is fetched")
        return render(request,'studentform.html',context)
    else:
        n=request.POST['name']
        r=request.POST['roll_number']
        per=request.POST['percentage']

        print(n)
        print(r)
        print(per)
        s=Student.objects.create(name=n,rno=r,per=per)
        s.save()
        return HttpResponse("Data Instered")

def djangomodelform(request):
    context={}
    if request.method=="GET":
        mfm=StudentModelFormClass()
        print(mfm)
        context['mform']=mfm
        return render(request,'studentmodelform.html',context)
    else:
        pass

# Registration
def user_register(request):
    context={}
    if request.method=="GET":
        regfm=UserRegister()
        print("GET:")
        print(regfm)
        context['rfm']=regfm
        return render(request,"register.html",context)
    else:
        # print("request.POST")
        print("POST:")
        dregfm=UserRegister(request.POST)
        # print(dregfm)
        dregfm.save()
        # return HttpResponse("User register Successfully")
        return render(request,"register_success.html")

# Login
def user_login(request):
    context={}
    loginfm=AuthenticationForm()
    context["lgfm"]=loginfm

    if request.method=="GET":
        return render(request,"login.html",context)
    else:
        uname=request.POST['username']
        upass=request.POST['password']
        # print("username: ",uname)
        # print("password: ",upass)
        u=authenticate(username=uname,password=upass)
        print("Returned Value by authenticate: ",u)
        # print("ID: ",u.id)
        # print("Password: ",u.password)
        # print("Superuser: ",u.is_superuser)
        # print("Email: ",u.email)
        # return HttpResponse("Data Fetched")
        if u is not None: #firstuser is not None => True|None is not none
            login(request,u)
            return redirect('/userdashboard')
        else:
            context['errmsg']="Invalid username or password!!!"
            return render(request,'login.html',context)

def user_logout(request):
    logout(request)
    return redirect('/login')











'''
syntax:

def functionname(request):

     return response object

To give response there are two functions 
1) HttpResponse()
2) render() 
'''
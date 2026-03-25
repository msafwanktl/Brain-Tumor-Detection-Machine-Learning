from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

from myapp.classify import check
from myapp.models import login, doctor, user, review, appoinment, schedule, prescription



def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert("Log out");window.location='/myapp/login/'</script>''')


def Login(request):
    return render(request,'loginindex.html')
def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    lg=login.objects.filter(username=username,password=password)
    if lg.exists():
        lg1=login.objects.get(username=username,password=password)
        request.session['lid']=lg1.id
        if lg1.usertype=='admin':
            return HttpResponse('''<script>alert("logined successfull");window.location='/myapp/adminhome/'</script>''')
        elif lg1.usertype=='doctor':
            return HttpResponse('''<script>alert("logined successfull");window.location='/myapp/doctorhome/'</script>''')
        elif lg1.usertype=='user':
            return HttpResponse('''<script>alert("logined successfull");window.location='/myapp/userhome/'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid username or password");window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("Not found");window.location='/myapp/login/'</script>''')


# ----------------------------Admin---------------------------

def adminhome(request):
    return render(request,'admin/adminIndex.html')

def changepassword(request):
    return render(request,'admin/changepassword.html')
def changepassword_post(request):
    oldpassword=request.POST['textfield']
    newpassword=request.POST['textfield2']
    confirmpassword=request.POST['textfield3']
    obj=login.objects.filter(id=request.session['lid'],password=oldpassword)
    if obj.exists():
        login.objects.get(id=request.session['lid'],password=oldpassword)
        if newpassword==confirmpassword:
            obj1=login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert("Password changed successfully");window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("Password not changed");window.location='/myapp/changepassword/'</script>''')
    else:
        return HttpResponse('''<script>alert("please check your current password");window.location='/myapp/changepassword/</script>''')


def viewapproveddoctor(request):
    data=doctor.objects.filter(Status="Approved")
    return render(request,'admin/viewapproveddoctor.html',{"doc":data})
def viewapproveddoctor_post(request):
    search=request.POST['textfield']
    data = doctor.objects.filter(Status="Approved", name__icontains=search)
    return render(request,'admin/viewapproveddoctor.html',{"doc":data})

def viewdoctors(request):
    data=doctor.objects.filter(Status="pending")
    return render(request,'admin/viewdoctors.html',{"doc":data})
def viewdoctor_post(request):
    search=request.POST['textfield']
    data = doctor.objects.filter(Status="pending",name__icontains=search)
    return render(request,'admin/viewdoctors.html',{'doc':data})


def dctr_approve(request,id):

    doctor.objects.filter(id=id).update(Status="Approved")
    return HttpResponse('''<script>alert("Approved successfully");window.location='/myapp/viewdoctors/'</script>''')


def dctr_reject(request,id):

    doctor.objects.filter(id=id).update(Status="Rejected")
    return HttpResponse('''<script>alert("Rejected successfully");window.location='/myapp/viewdoctors/'</script>''')


def viewrejecteddoctor(request):
    data=doctor.objects.filter(Status="Rejected")
    return render(request,'admin/viewrejecteddoctor.html',{"doc":data})
def viewrejecteddoctor_post(request):
    search=request.POST['textfield']
    data = doctor.objects.filter(Status="Rejected",name__icontains=search)
    return render(request,'admin/viewrejecteddoctor.html',{'doc':data})

def viewreviews(request):
    data=review.objects.all()
    return render(request,'admin/viewreviews.html',{"doc":data})
def viewreviews_post(request):
    f=request.POST['textfield']
    t=request.POST['textfield2']
    data = review.objects.filter(date__range=[f,t])
    return render(request,'admin/viewreviews.html',{"doc":data})

def viewusers(request):
    data=user.objects.all()
    return render(request,'admin/viewusers.html',{"doc":data})
def viewuser_post(request):
    search=request.POST['textfield']
    data = user.objects.filter(name__icontains=search)
    return render(request,'admin/viewusers.html',{"doc":data})

# ----------------------------doctor---------------------------

def doctorhome(request):
    return render(request,'doctor/doctorindex.html')

def dr_signup(request):
    return render(request, 'doctor/signupindex.html')
def dr_signup_post(request):
    name=request.POST['textfield']
    gender=request.POST['RadioGroup1']
    dob=request.POST['textfield2']
    email=request.POST['textfield3']
    phone=request.POST['textfield4']
    housename=request.POST['textfield5']
    place=request.POST['textfield6']
    city=request.POST['textfield7']
    state=request.POST['textfield8']
    pincode=request.POST['textfield9']
    # photo=request.FILES['textfield10']
    Specialisation=request.POST['textfield13']
    HospitalName=request.POST['textfield14']
    About=request.POST['textfield15']
    Experience=request.POST['textfield16']
    qualification=request.POST['textfield17']
    password=request.POST['textfield11']

    from datetime import datetime

    fname = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"

    f = FileSystemStorage()
    # f.save(fname, photo)


    l=login()
    l.username=email
    l.password=password
    l.usertype="doctor"
    l.save()

    d=doctor()
    d.name=name
    d.gender=gender
    d.DOB=dob
    d.email=email
    d.phone=phone
    d.housename=housename
    d.place=place
    d.city=city
    d.state=state
    d.pincode=pincode
    # d.photo=f.url(fname)
    d.Specialisation=Specialisation
    d.HospitalName=HospitalName
    d.About=About
    d.Status="pending"
    d.Experience=Experience
    d.Qualification=qualification
    d.LOGIN=l
    d.save()
    return HttpResponse('''<script>alert("sign up successfully");window.location='/myapp/login/'</script>''')

def dr_addprescription(request,id):
    request.session['aid']=id
    return render(request,'doctor/addprescription.html')

def dr_addprescription_post(request):
    date=request.POST['textfield2']
    prescription1 = request.POST['textarea']


    p=prescription()
    p.APPOINMENT_id=request.session['aid']
    p.date=date
    p.prescription=prescription1
    # p.APPOINMENT_id=aid
    p.save()

    return HttpResponse('''<script>alert("prescription added successfully");window.location='/myapp/doctorhome/'</script>''')

def dr_addschedule(request):
    return render(request,'doctor/addschedule.html')
def addschedule_post(request):
    date=request.POST['textfield']
    start = request.POST['textfield2']
    end = request.POST['textfield3']

    s=schedule()
    s.date=date
    s.start=start
    s.end=end
    s.DOCTOR=doctor.objects.get(LOGIN=request.session['lid'])
    s.save()

    return HttpResponse('''<script>alert("Schedule added successfully");window.location='/myapp/doctorhome/'</script>''')

def dr_changepassword(request):
    return render(request,'doctor/changepassword.html')
def dr_changepassword_post(request):
    oldpassword=request.POST['textfield']
    newpassword=request.POST['textfield2']
    confirmpassword=request.POST['textfield3']
    obj = login.objects.filter(id=request.session['lid'], password=oldpassword)
    if obj.exists():
        login.objects.get(id=request.session['lid'], password=oldpassword)
        if newpassword == confirmpassword:
            obj1 = login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert("Password changed successfully");window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("Password not changed");window.location='/myapp/dr_changepassword/'</script>''')
    else:
        return HttpResponse('''<script>alert("please check your current password");window.location='/myapp/dr_changepassword/</script>''')

def dr_editprofile(request):
    data=doctor.objects.get(LOGIN=request.session['lid'])
    return render(request,'doctor/editprofile.html',{'doc':data})
def dr_editprofile_post(request):
    name = request.POST['textfield']
    gender = request.POST['gender']
    dob = request.POST['textfield2']
    email = request.POST['textfield3']
    phone = request.POST['textfield4']
    housename = request.POST['textfield5']
    place = request.POST['textfield6']
    city = request.POST['textfield7']
    state = request.POST['textfield8']
    pincode = request.POST['textfield9']
    Specialisation = request.POST['textfield13']
    HospitalName = request.POST['textfield14']
    About = request.POST['textfield15']
    Experience = request.POST['textfield16']
    Qualification = request.POST['textfield17']


    obj=doctor.objects.get(LOGIN=request.session['lid'])
    # if 'photo' in request.FILES:
    #     photo = request.FILES['textfield10']
    #     from datetime import datetime
    #     fname = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    #     f = FileSystemStorage()
    #     path=f.save(fname, photo)
    #     obj.photo=path
    #     obj.save()

    obj.name=name
    obj.gender=gender
    obj.DOB=dob
    obj.email=email
    obj.phone=phone
    obj.housename=housename
    obj.place=place
    obj.city=city
    obj.state=state
    obj.pincode=pincode
    obj.Specialisation=Specialisation
    obj.HospitalName=HospitalName
    obj.About=About
    obj.Experience=Experience
    obj.Qualification=Qualification
    obj.save()

    return HttpResponse('''<script>alert("Profile edited successfully");window.location='/myapp/dr_viewprofile/'</script>''')

def dr_editschedule(request,id):
    s=schedule.objects.get(id=id)
    return render(request,'doctor/editschedule.html',{"doc":s})
def dr_editschedule_post(request):
    id=request.POST['id']
    date=request.POST['textfield']
    start = request.POST['textfield2']
    end = request.POST['textfield3']


    s=schedule.objects.get(id=id)
    s.date=date
    s.start=start
    s.end=end
    s.save()

    return HttpResponse('''<script>alert("Schedule edited successfully");window.location='/myapp/doctorhome/'</script>''')

def delete_schedule(request,id):
    schedule.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('delete succesfully');window.location='/myapp/viewschedule/'</script>''')
def dr_viewappoinment(request):
    data=appoinment.objects.all()
    return render(request,'doctor/viewappoinment.html',{"doc":data})
def dr_viewappoinment_post(request):
    fromd=request.POST['textfield']
    tod=request.POST['textfield2']
    data=appoinment.objects.filter(registrationDate__range=[fromd,tod])
    return render(request, 'doctor/viewappoinment.html',{"doc":data})

def dr_viewprofile(request):
    data=doctor.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'doctor/viewprofile.html',{"doc":data})


def dr_viewschedule(request):
    data=schedule.objects.all()
    return render(request,'doctor/viewschedule.html',{"doc":data})
def dr_viewschedule_post(request):
    f=request.POST['textfield']
    t=request.POST['textfield2']
    data = schedule.objects.filter(date__range=[f,t])
    return render(request, 'doctor/viewschedule.html',{"doc":data})

def druploadimage(request):
    return render(request,'doctor/dr upload image.html')


def druploadimage_post(request):
    uploaded_file = request.FILES['image']
    date=datetime.now().strftime("%y%m%d-%H%M%S")+"jpg"
    fs = FileSystemStorage()
    filename = fs.save(date, uploaded_file)
    file_url = fs.url(filename)
    print(check("C:\\Users\\MSA\\PycharmProjects\\brain_tumor\\media\\"+date))
    result=check("C:\\Users\\MSA\\PycharmProjects\\brain_tumor\\media\\"+date)

    return render(request, 'doctor/dr upload image.html', {'file_url': file_url,"result":result})

#------------------------------user---------------------------------

def userhome(request):
    return render(request, 'user/userindex.html')

def us_changepassword(request):
    return render(request,'user/changepassword.html')
def us_changepassword_post(request):
    oldpassword=request.POST['textfield']
    newpassword=request.POST['textfield2']
    confirmpassword=request.POST['textfield3']
    obj = login.objects.filter(id=request.session['lid'], password=oldpassword)
    if obj.exists():
        login.objects.get(id=request.session['lid'], password=oldpassword)
        if newpassword == confirmpassword:
            obj1 = login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert("Password changed successfully");window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("Password not changed");window.location='/myapp/us_changepassword/'</script>''')
    else:
        return HttpResponse('''<script>alert("please check your current password");window.location='/myapp/us_changepassword/</script>''')

def us_editprofile(request):
    data=user.objects.get(LOGIN=request.session['lid'])
    return render(request,'user/editprofile.html',{'doc':data})
def us_editprofile_post(request):
    name=request.POST['textfield']
    gender=request.POST['RadioGroup1']
    DOB=request.POST['textfield2']
    email=request.POST['textfield3']
    phone=request.POST['textfield4']
    housename=request.POST['textfield5']
    place=request.POST['textfield6']
    city=request.POST['textfield7']
    state=request.POST['textfield8']
    pincode=request.POST['textfield9']


    obj = user.objects.get(LOGIN=request.session['lid'])
    # if 'photo' in request.FILES:
    #     photo = request.FILES['textfield10']
    #     from datetime import datetime
    #     fname = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    #     f = FileSystemStorage()
    #     path = f.save(fname, photo)
    #     obj.photo = path
    #     obj.save()

    obj.name=name
    obj.gender=gender
    obj.dob=DOB
    obj.email=email
    obj.phone=phone
    obj.housename=housename
    obj.place=place
    obj.city=city
    obj.state=state
    obj.pincode=pincode
    obj.save()


    return HttpResponse('''<script>alert("Profile edited successfully");window.location='/myapp/us_viewprofile/'</script>''')


def us_signup(request):
    return render(request,'user/ussignupindex.html')
def us_signup_post(request):
    name=request.POST['textfield']
    gender=request.POST['RadioGroup1']
    DOB=request.POST['textfield2']
    email=request.POST['textfield3']
    phone=request.POST['textfield4']
    housename=request.POST['textfield5']
    place=request.POST['textfield6']
    city=request.POST['textfield7']
    state=request.POST['textfield8']
    pincode=request.POST['textfield9']
    # photo=request.FILES['textfield10']
    password=request.POST['textfield11']



    from datetime import datetime

    fname= datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"

    f=FileSystemStorage()
    # f.save(fname,photo)






    l=login()
    l.username=email
    l.password=password
    l.usertype="user"
    l.save()


    u=user()
    u.name=name
    u.gender=gender
    u.dob=DOB
    u.email=email
    u.phone=phone
    u.housename=housename
    u.place=place
    u.city=city
    u.state=state
    u.pincode=pincode
    # u.photo=f.url(fname)
    u.LOGIN=l
    u.save()
    return HttpResponse('''<script>alert("sign up successfully");window.location='/myapp/login/'</script>''')

def us_viewdoctors(request):
    data=doctor.objects.filter(Status="Approved")
    return render(request,'user/viewdoctors.html',{"doc":data})
def us_viewdoctors_post(request):
    search=request.POST['textfield']
    data=doctor.objects.filter(Status="Approved",name__icontains=search)
    return render(request,'user/viewdoctors.html',{"doc":data})

def us_viewhistory(request):
    return render(request,'user/viewhistory.html')
def us_viewhistory_post(request):
    search=request.POST['search']
    return render(request,'user/viewhistory.html')

def us_viewprofile(request):
    data=user.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'user/viewprofile.html',{"doc":data})

def us_viewschedule(request,id):
    request.session['sid'] = id
    data=schedule.objects.filter(DOCTOR=id)
    return render(request,'user/viewschedule.html',{"doc":data})
def us_viewschedule_post(request):
    f = request.POST['textfield']
    t = request.POST['textfield2']
    doc = schedule.objects.filter(date__range=[f,t],DOCTOR=request.session['sid'])
    return render(request,'user/viewschedule.html',{"doc":doc})

def makeappointment(request,id):
    # id=request.POST['id']
    obj=appoinment()
    obj.registrationDate=datetime.now()
    obj.USER=user.objects.get(LOGIN_id=request.session['lid'])
    obj.status='appointment taken'
    obj.SCHEDULE_id=id
    obj.save()
    return HttpResponse('''<script>alert('appointment taken');window.location='/myapp/us_viewschedule/{request.session['sid']}'</script>''')


def uploadimage(request):
    return render(request,'user/upload image.html')


def uploadimage_post(request):
    uploaded_file = request.FILES['image']
    date=datetime.now().strftime("%y%m%d-%H%M%S")+"jpg"
    fs = FileSystemStorage()
    filename = fs.save(date, uploaded_file)
    file_url = fs.url(filename)
    print(check("C:\\Users\\MSA\\PycharmProjects\\brain_tumor\\media\\"+date))
    result=check("C:\\Users\\MSA\\PycharmProjects\\brain_tumor\\media\\"+date)

    return render(request, 'user/upload image.html', {'file_url': file_url,"result":result})



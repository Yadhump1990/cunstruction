from pprint import pprint

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
import random

# Create your views here.
from django.utils.datetime_safe import datetime

# from cunstruction.models import *
from cunstruction.models import *


def main(request):
    return render(request,'loginIndex.html')

def usr_registration(request):
    return render(request,'UserRegisterIndex.html')
def userReg(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    phone = request.POST['tel']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    gender = request.POST['radio']
    email = request.POST['email']
    username = request.POST['uname']
    password = request.POST['password']
    #to save login to database
    lob = login()
    lob.username = username
    lob.password = password
    lob.type = 'user'
    lob.save()
    #to save user to database
    uob = user()
    uob.fname = fname
    uob.lname = lname
    uob.gender = gender
    uob.phone = phone
    uob.place = place
    uob.post = post
    uob.pin = pin
    uob.email = email
    uob.lid = lob
    uob.save()
    return HttpResponse('''<script>alert("user registered successfully");window.location="/"</script>''')


def cntrct_registration(request):
    return render(request,'contractorRegisterIndex.html')
def cntrctorRegistration(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    phone = request.POST['tel']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    gender = request.POST['radio']
    email = request.POST['email']
    experiance = request.POST['exp']
    username = request.POST['uname']
    password = request.POST['password']
    #to save login to database
    lob = login()
    lob.username = username
    lob.password = password
    lob.type = 'pending'
    lob.save()
    cob = contractor()
    ##to save contractor
    cob.fname = fname
    cob.lname = lname
    cob.gender = gender
    cob.phone = phone
    cob.place = place
    cob.post = post
    cob.pin = pin
    cob.email = email
    cob.experience = experiance
    cob.lid = lob
    cob.save()
    return HttpResponse('''<script>alert("contractor registered successfully");window.location="/"</script>''')

def log(request):
    username = request.POST['uname']
    password = request.POST['password']
    try:
        logOb = login.objects.get(username=username,password=password)
        if logOb.type == 'admin':# to store the login session id
            ob1 = auth.authenticate(username='yadhu', password='admin')  # for login authentication
            auth.login(request, ob1)  # for login authentication
            return HttpResponse('''<script>alert("welcome admin");window.location='/adminHome'</script>''')
        elif logOb.type == 'user':
            request.session['lid'] = logOb.id  # to store the login session id
            ob1 = auth.authenticate(username='yadhu', password='admin')  # for login authentication
            auth.login(request, ob1)  # for login authentication
            return HttpResponse('''<script>alert("welcome user");window.location='/userHome'</script>''')
        elif logOb.type == 'contractor':
            request.session['lid'] = logOb.id  # to store the login session id
            ob1 = auth.authenticate(username='yadhu', password='admin')  # for login authentication
            auth.login(request, ob1)  # for login authentication
            return HttpResponse('''<script>alert("welcome contractor");window.location='/contractorHome'</script>''')
        elif logOb.type == 'worker':
            request.session['lid'] = logOb.id  # to store the login session id
            ob1 = auth.authenticate(username='yadhu', password='admin')  # for login authentication
            auth.login(request, ob1)  # for login authentication
            return HttpResponse('''<script>alert("welcome worker");window.location='/workerHome'</script>''')
        else:
            return HttpResponse('''<script>alert("invalid username or password ");window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert("invalid username or password ");window.location='/'</script>''')

def forgotPass(request):
    return render(request,'forgotPassword.html')

def forgot_password(request):

        uname=request.POST['uname']
        mail=request.POST['email']
        try:
            g=login.objects.get(username=uname)
            if g is not None:
                a=random.randint(0000,9999)
                g.password=(str(a))
                g.save()
                send_mail('forgot password ', "YOUR NEW PASSWORD IS  -" +str(a), 'yadhusample1998@gmail.com',[mail], fail_silently=False)
                return HttpResponse('''<script>alert("Password sent to your registered email address !!!");window.location='/'</script>''')
                # return redirect('/')
            else:
                print('error==========')
                return HttpResponse('''<script>alert("Invalid Username or Email Adress!!!");window.location='/forgotPass'</script>''')
                # return HttpResponse('''<script>alert("Invalid Username or Email Adress!!!")</script>''')
                # return redirect('forgotPass')
        except:
            return HttpResponse('''<script>alert("Invalid Username or Email Adress!!!");window.location='/forgotPass'</script>''')



#ADMIN
@login_required(login_url='/') #for login authentication
def adminHome(request):
    return render(request,'adminIndex.html')

@login_required(login_url='/') #for login authentication
def block_contractors(request):
    ob = contractor.objects.all()
    return render(request,'admin/BLOCK_CONTRACTOR.html',{'val':ob})

@login_required(login_url='/') #for login authentication
def blockContractor(request,id):
    ob = login.objects.get(id=id)
    ob.type = 'blocked'
    ob.save()
    return HttpResponse('''<script>alert("Contractor blocked");window.location='/block_contractors'</script>''')

@login_required(login_url='/') #for login authentication
def UnBlockContractor(request,id):
    ob = login.objects.get(id=id)
    ob.type = 'contractor'
    ob.save()
    return HttpResponse('''<script>alert("Contractor unblocked");window.location='/block_contractors'</script>''')

@login_required(login_url='/') #for login authentication
def block_worker(request):
    ob = worker.objects.all()
    return render(request,'admin/BLOCK_WORKER.html',{'val':ob})

@login_required(login_url='/') #for login authentication
def blockWorker(request,id):
    ob = login.objects.get(id=id)
    ob.type = 'blocked'
    ob.save()
    return HttpResponse('''<script>alert("Worker blocked");window.location='/block_worker'</script>''')

@login_required(login_url='/') #for login authentication
def UnBlockWorker(request,id):
    ob = login.objects.get(id=id)
    ob.type = 'worker'
    ob.save()
    return HttpResponse('''<script>alert("Worker unblocked");window.location='/block_worker'</script>''')

@login_required(login_url='/') #for login authentication
def viewUsrCompSentRep(request):
    ucob = usr_complaint.objects.all()
    return render(request,'admin/USR_COMP_SNT_REP.html',{'val':ucob})

@login_required(login_url='/') #for login authentication
def usrReply(request,id):
    request.session['rid'] = id
    return render(request,'admin/USR_REPLY.html')

@login_required(login_url='/') #for login authentication
def userCompReply(request):
    reply = request.POST['textarea']
    ob = usr_complaint.objects.get(id=request.session['rid'])
    ob.reply = reply
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert(" Reply Sent ");window.location='/viewUsrCompSentRep'</script>''')

@login_required(login_url='/') #for login authentication
def verifyContractor(request):
    cob= contractor.objects.all()
    return render(request,'admin/VERIFY_CONTRACTOR.html',{'val':cob})

@login_required(login_url='/') #for login authentication
def acceptContractor(request,id):
    ob = login.objects.get(id=id)
    ob.type = 'contractor'
    ob.save()
    return HttpResponse('''<script>alert(" CONTRACTOR ACCEPTED ");window.location='/verifyContractor'</script>''')

@login_required(login_url='/') #for login authentication
def rejectContractor(request,id):
    ob = login.objects.get(id=id)
    ob.type = 'rejected'
    ob.save()
    return HttpResponse('''<script>alert(" CONTRACTOR REJECTED ");window.location='/verifyContractor'</script>''')

@login_required(login_url='/') #for login authentication
def veiwCustomerRevRat(request):
    revOb = usr_review.objects.all()
    return render(request,'admin/VIEW_CUSTOMER_REVIEW_RATING.html',{'val':revOb})

@login_required(login_url='/') #for login authentication
def viewUser(request):
    uob = user.objects.all()
    return render(request,'admin/VIEW_USER.html',{'val':uob})

# @login_required(login_url='/') #for login authentication
# def viewWorkerDetail(request):
#     # wob = worker.objects.all()
#     return render(request,'admin/VIEW_WORKER_DETAILS.html',{'val':wob})

def viewWorkerDetail(request):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cunstruction_worker ORDER BY experience DESC")
    # workers = [worker(*row) for row in cursor.fetchall()]
    res = cursor.fetchall()
    pprint(res)
    return render(request, 'admin/VIEW_WORKER_DETAILS.html', {'val': res})



@login_required(login_url='/') #for login authentication

def viewWorkerRevRat(request):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select * from cunstruction_contractor")
    result = cursor.fetchall()
    # cob = contractor.objects.all()
    return render(request,'admin/VIEW_WORKER_REV_RAT.html',{'val': result})

@login_required(login_url='/') #for login authentication
def view_worker_rev_rat(request):
    from django.db import connection
    cursor = connection.cursor()
    cid = request.POST['select2']
    # cursor.execute(""" SELECT * FROM cunstruction_wkr_review INNER JOIN cunstruction_worker ON cunstruction_wkr_review.wid_id = cunstruction_worker.id WHERE cunstruction_wkr_review.cid_id = %s """, [cid])
    cursor.execute("""
            SELECT cunstruction_wkr_review.feedback, cunstruction_wkr_review.rating, 
                cunstruction_wkr_review.date, cunstruction_worker.fname, cunstruction_worker.lname
            FROM cunstruction_wkr_review
            JOIN cunstruction_worker ON cunstruction_wkr_review.wid_id = cunstruction_worker.id
            WHERE cunstruction_wkr_review.cid_id = %s 
        """, [cid])
    wrobRes = cursor.fetchall()
    pprint(wrobRes)
    # wrob = wkr_review.objects.select_related('wid').filter(cid=cid)

    cursor.execute("select * from cunstruction_contractor")
    result = cursor.fetchall()
    # cob = contractor.objects.all()
    return render(request,'admin/VIEW_WORKER_REV_RAT.html',{'val2':wrobRes,'val': result,'s':cid})

@login_required(login_url='/') #for login authentication
def view_Wrkr_Comp_Sent_rep(request):
    cob = contractor.objects.all()
    print(cob)
    return render(request, 'admin/WORKER_COM_SNT_REP.html', {'val': cob})

@login_required(login_url='/') #for login authentication
def viewWrkerCompSentRep(request):
    cid = request.POST['select']
    wcob = wkr_complaint.objects.select_related('wid').filter(cid=cid)
    cob = contractor.objects.all()
    return render(request,'admin/WORKER_COM_SNT_REP.html',{'val2':wcob,'val':cob,'s':cid})

@login_required(login_url='/') #for login authentication
def workerRep(request,id):
    request.session['wrep'] = id
    return render(request,'admin/WORKER_REPLY.html')

@login_required(login_url='/') #for login authentication
def workerReply(request):
    reply = request.POST['textarea']
    ob = wkr_complaint.objects.get(id=request.session['wrep'])
    ob.reply = reply
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("reply sent ");window.location='/view_Wrkr_Comp_Sent_rep'</script>''')

def manageVideo(request):
    vob = video.objects.all()
    return render(request,'admin/MANAGE_VIDEO.html',{'val':vob})

def addVideo(request):
    return render(request,'admin/ADD_VIDEO.html')

def add_video(request):
    videos = request.FILES['fileField']
    Fp = FileSystemStorage()
    Fs = Fp.save(videos.name, videos)
    description = request.POST['textarea']
    ob = video()
    ob.video = Fs
    ob.description = description
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("video added ");window.location='/manageVideo'</script>''')

    




#contractor
@login_required(login_url='/') #for login authentication
def contractorHome(request):
    return render(request,'contractorIndex.html')

@login_required(login_url='/') #for login authentication
def editContratorProfile(request):
    conOb = contractor.objects.get(lid__id=request.session['lid'])
    return render(request,'contractor/EDIT_PROFILE.html',{'val':conOb})

@login_required(login_url='/') #for login authentication
def update_con_prof(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    phone = request.POST['tel']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    gender = request.POST['radio']
    experience = request.POST['exp']
    conOb = contractor.objects.get(lid__id=request.session['lid'])
    conOb.fname = fname
    conOb.lname = lname
    conOb.email = email
    conOb.phone = phone
    conOb.place = place
    conOb.post = post
    conOb.pin = pin
    conOb.gender = gender
    conOb.experience = experience
    conOb.save()
    return HttpResponse('''<script>alert("Profile updated ");window.location='/updateContractorProfile'</script>''')

@login_required(login_url='/') #for login authentication
def updateContractorProfile(request):
    conOb = contractor.objects.get(lid__id=request.session['lid'])
    return render(request,'contractor/UPDATE_CONTRACTOR_PROFILE.html',{'val':conOb})

@login_required(login_url='/') #for login authentication
def viewWorker(request):
    wOb = worker.objects.all()
    return render(request,'contractor/VIEW_WORKER.html',{'val':wOb})

@login_required(login_url='/') #for login authentication
def addWorker(request):
    return render(request,'contractor/ADD_WORKER.html')

@login_required(login_url='/') #for login authentication
def add_Worker(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    phone = request.POST['tel']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    gender = request.POST['radio']
    experience = request.POST['exp']
    availability = request.POST['select']
    username = request.POST['uname']
    password = request.POST['password']
    probation_period = request.POST.get('radio2')  # get the value of the radio button
    probation_length = reque
    st.POST.get('probation_length')  # get the value of the input field
    lob = login()
    lob.username = username
    lob.password = password
    lob.type = 'worker'
    lob.save()
    wOb = worker()
    wOb.lid = lob
    wOb.cid = contractor.objects.get(lid__id=request.session['lid'])
    wOb.fname = fname
    wOb.lname = lname
    wOb.email = email
    wOb.phone = phone
    wOb.place = place
    wOb.post = post
    wOb.pin = pin
    wOb.gender = gender
    wOb.experience = experience
    wOb.availability = availability
    wOb.probation_period = probation_period  # set the value of the probation_period field
    wOb.probation_length = probation_length  # set the value of the probation_length field
    wOb.save()
    return HttpResponse('''<script>alert("worker added ");window.location='/viewWorker'</script>''')

@login_required(login_url='/') #for login authentication
def wrkrExistChk(request):
    username = request.GET['uname']
    data = {
        'is_taken': worker.objects.filter(lid__username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = "username already exists"
    return JsonResponse(data)

# def probatWrkrPeriod(request):
#     probPeriod = request.GET['radio2']


@login_required(login_url='/') #for login authentication
def assignWorkToWorker(request):
    wob = worker.objects.all()
    jOb = job.objects.all()
    job_assigned = assignJob.objects.all()
    return render(request,'contractor/ASSIGN_WRK_TO_WRKR.html',{ 'val': wob,'val2': jOb,'val3':job_assigned})

@login_required(login_url='/') #for login authentication
def assign_wrk_worker(request):
    if request.method == 'POST':
        worker_id = request.POST.get('select')  # get the selected worker ID from the form
        job_id = request.POST.get('select2')  # get the selected job ID from the form

        # Check if a job has already been assigned to this worker
        if assignJob.objects.filter(wid__id=worker_id, jid__id=job_id).exists():
            return HttpResponse('''<script>alert("Work already assigned ");window.location='/assignWorkToWorker'</script>''')

        # Create a new assignJob object and save it to the database
        ob = assignJob()
        ob.wid = worker.objects.get(id=worker_id)
        ob.cid = contractor.objects.get(lid__id=request.session['lid'])
        ob.jid = job.objects.get(id=job_id)
        ob.jobStatus = 'assigned'
        ob.date = datetime.today()
        ob.save()

        return HttpResponse('''<script>alert("Work assigned ");window.location='/assignWorkToWorker'</script>''')

    return HttpResponse("Method not allowed")

@login_required(login_url='/') #for login authentication
def manageJobs(request):
    jOb = job.objects.all()
    return render(request,'contractor/MANAGE_JOBS.html',{'val':jOb})

@login_required(login_url='/') #for login authentication
def editJobs(request,id):
    ejOB = job.objects.get(id=id)
    request.session['ejid'] = id
    return render(request,'contractor/editJobs.html',{'val':ejOB})

@login_required(login_url='/') #for login authentication
def updateJobs(request):
    jobName = request.POST['textfield']
    jobDetails = request.POST['textfield2']
    jOb = job.objects.get(id=request.session['ejid'])
    jOb.job = jobName
    jOb.cid = contractor.objects.get(lid__id=request.session['lid'])
    jOb.jobDetails = jobDetails
    jOb.date = datetime.today()
    jOb.save()
    return HttpResponse('''<script>alert("Job updated ");window.location='/manageJobs'</script>''')

@login_required(login_url='/') #for login authentication
def delJobs(request,id):
    djobOb = job.objects.get(id=id)
    djobOb.delete()
    return HttpResponse('''<script>alert("Job deleted ");window.location='/manageJobs'</script>''')


@login_required(login_url='/') #for login authentication
def addjobs(request):
    return render(request,'contractor/addJobs.html')

@login_required(login_url='/') #for login authentication
def add_jobs(request):
    jobName = request.POST['textfield']
    jobDetails = request.POST['textfield2']
    jOb = job()
    jOb.cid = contractor.objects.get(lid__id=request.session['lid'])
    jOb.job = jobName
    jOb.jobDetails = jobDetails
    jOb.date = datetime.today()
    jOb.save()
    return HttpResponse('''<script>alert("Job added ");window.location='/manageJobs'</script>''')

@login_required(login_url='/') #for login authentication
def viewCustomerReqApprvl(request):
    ob = usr_work_request.objects.all()
    return render(request,'contractor/VIEW_CUSTOMER_REQUEST_APPROVAL.html',{'val':ob})

@login_required(login_url='/') #for login authentication
def userReqAccept(request,id):
    ob = usr_work_request.objects.get(id=id)
    ob.status = "Accepted"
    ob.save()
    return HttpResponse('''<script>alert("Accepted ");window.location='/viewCustomerReqApprvl'</script>''')

@login_required(login_url='/') #for login authentication
def userReqReject(request,id):
    ob = usr_work_request.objects.get(id=id)
    ob.status = "Rejected"
    ob.save()
    return HttpResponse('''<script>alert("Rejected ");window.location='/viewCustomerReqApprvl'</script>''')

@login_required(login_url='/') #for login authentication
def view_contractor_work(request):
    # cob = contractor.objects.get(lid__id=request.session['lid'])
    work = contractorWorks.objects.filter(cid__lid__id=request.session['lid'])
    return render(request,'contractor/VIEW_CONTRACTOR_WORKS.html',{'val':work})

@login_required(login_url='/') #for login authentication
def post_contractor_work(request):
    return render(request,'contractor/POST_CONTRACTOR_WORK.html')

@login_required(login_url='/') #for login authentication
def postWorks(request):
    workName = request.POST['work']
    img = request.FILES['fileField']
    Fp = FileSystemStorage()
    Fs = Fp.save(img.name,img)
    description = request.POST['textarea']
    ob = contractorWorks()
    ob.cid = contractor.objects.get(lid__id=request.session['lid'])
    ob.work = workName
    ob.image = Fs
    ob.description = description
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("Work uploaded ");window.location='/view_contractor_work'</script>''')

def viewVideo(request):
    vob = video.objects.all()
    return render(request,'contractor/VIEW_VIDEO.html',{'val':vob})



#User
@login_required(login_url='/') #for login authentication
def userHome(request):
    return render(request,'userIndex.html')

@login_required(login_url='/') #for login authentication
def editUserProfile(request):
    uob = user.objects.get(lid__id=request.session['lid'])
    return render(request,'user/UPDATE_USER_PROFILE.html',{'val':uob})

@login_required(login_url='/') #for login authentication
def updateUserProfile(request):
    uob = user.objects.get(lid__id=request.session['lid'])
    return render(request,'user/EDIT_USR_PROFILE.html',{'val':uob})

@login_required(login_url='/') #for login authentication
def update_u_prof(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    phone = request.POST['tel']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    gender = request.POST['radio']
    email = request.POST['email']
    uob = user.objects.get(lid__id=request.session['lid'])
    uob.fname = fname
    uob.lname = lname
    uob.phone = phone
    uob.place = place
    uob.post = post
    uob.pin = pin
    uob.gender = gender
    uob.email = email
    uob.save()
    return HttpResponse('''<script>alert("Profile updated ");window.location='/editUserProfile'</script>''')

@login_required(login_url='/') #for login authentication
def sentUserFeedback(request):
    return render(request,'user/SENT_USR_FEEDBACK.html')

@login_required(login_url='/') #for login authentication
def sentFeedUser(request):
    feedback = request.POST['textarea']
    rating = request.POST['select']
    fob = usr_review()
    fob.uid = user.objects.get(lid__id=request.session['lid'])
    fob.feedback = feedback
    fob.rating = rating
    fob.date = datetime.today()
    fob.save()
    return HttpResponse('''<script>alert("feedback sent ");window.location='/sentUserFeedback'</script>''')

@login_required(login_url='/') #for login authentication
def sntUsrCompViewReply(request):
    uob = user.objects.get(lid__id=request.session['lid'])
    cob = usr_complaint.objects.select_related('uid').filter(uid=uob)
    return render(request,'user/SNT_USR_COMP_VIEW_REP.html',{'val':cob})

@login_required(login_url='/') #for login authentication
def addUserComp(request):

    return render(request,'user/ADD_USR_COMP.html')

@login_required(login_url='/') #for login authentication
def add_user_comp(request):
    complaint = request.POST['textarea']
    cob = usr_complaint()
    cob.uid = user.objects.get(lid__id=request.session['lid'])
    cob.complaint = complaint
    cob.reply = 'pending'
    cob.date = datetime.today()
    cob.save()
    return HttpResponse('''<script>alert("Complaint sent ");window.location='/sntUsrCompViewReply'</script>''')

@login_required(login_url='/') #for login authentication
def srchCntrctrSentWrkReq(request):
    cob = contractor.objects.all()
    return render(request,'user/SRCH_CONTRACTR_SENT_WRK_REQ.html',{'val':cob})

@login_required(login_url='/') #for login authentication
def srchAndViewCOntractor(request):
    # from django.db import connection
    # cursor = connection.cursor()
    contractorId = request.POST['select2']
    # cursor.execute("""
    #     SELECT DISTINCT cunstruction_contractorworks.*,
    #                     cunstruction_usr_work_request.status
    #     FROM cunstruction_contractorworks
    #     JOIN cunstruction_usr_work_request ON cunstruction_usr_work_request.cwid_id = cunstruction_contractorworks.id
    #     WHERE cunstruction_contractorworks.cid_id = %s
    # """, [contractorId])
    # ob = cursor.fetchall()
    # pprint(ob)
    ob=contractorWorks.objects.filter(cid__id=contractorId)
    cob = contractor.objects.all()
    #check if request already sent
    # request_sent = True #placeholder value for demonstration pupose

    return render(request, 'user/SRCH_CONTRACTR_SENT_WRK_REQ.html', {'val2': ob,'val':cob,'s':contractorId})

@login_required(login_url='/') #for login authentication
def sendWorkReqToCon(request,id):
    ob = usr_work_request()
    ob.cwid = contractorWorks.objects.get(id=id)
    ob.uid = user.objects.get(lid__id=request.session['lid'])
    ob.status = 'pending'
    ob.date = datetime.today()
    ob.save()
    obCW = contractorWorks.objects.get(id=id)
    obCW.status = "request sent"
    obCW.save()
    return HttpResponse('''<script>alert("request sent ");window.location='/srchCntrctrSentWrkReq'</script>''')

@login_required(login_url='/') #for login authentication
def viewContractorStatus(request):
    uob = user.objects.get(lid__id=request.session['lid'])
    status = usr_work_request.objects.select_related('cwid').filter(uid=uob)
    return render(request,'user/VIEW_CONTRACTOR_STATUS.html',{'val':status})


#worker
@login_required(login_url='/') #for login authentication
def workerHome(request):
    return render(request,'worker/WORKER_HOME.html')

@login_required(login_url='/') #for login authentication
def updateWorkerProfile(request):
    wob = worker.objects.get(lid__id=request.session['lid'])
    return render(request,'worker/update_worker_profile.html',{'val':wob})

@login_required(login_url='/') #for login authentication
def editWorkerProfile(request):
    wob = worker.objects.get(lid__id=request.session['lid'])
    return render(request,'worker/EDIT_WORKER_PROFILE.html',{'val':wob})

@login_required(login_url='/') #for login authentication
def update_worker_pro(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    phone = request.POST['tel']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    gender = request.POST['radio']
    experience = request.POST['exp']
    availability = request.POST['select']
    wob = worker.objects.get(lid__id=request.session['lid'])
    wob.fname = fname
    wob.lname = lname
    wob.email = email
    wob.phone = phone
    wob.place = place
    wob.post = post
    wob.pin = pin
    wob.gender= gender
    wob.experience = experience
    wob.availability =availability
    wob.save()
    return HttpResponse('''<script>alert("Profile updated ");window.location='/updateWorkerProfile'</script>''')

@login_required(login_url='/') #for login authentication
def postCompViewRep(request):
    comOb =  wkr_complaint.objects.all()
    return render(request,'worker/PST_COMP_VIEW_REP.html',{'val':comOb})

@login_required(login_url='/') #for login authentication
def postComplaint(request):
    cob = contractor.objects.all()
    return render(request,'worker/POST_COMP.html',{'val':cob})

@login_required(login_url='/') #for login authentication
def post_complaint_wrkr(request):
    contractorName = request.POST['select']
    complaint = request.POST['textarea']
    ob = wkr_complaint()
    ob.wid = worker.objects.get(lid__id=request.session['lid'])
    ob.cid = contractor.objects.get(id=contractorName)
    ob.complaint = complaint
    ob.reply = 'pending'
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("Complaint sent ");window.location='/postCompViewRep'</script>''')

@login_required(login_url='/') #for login authentication
def sendContractorFeedback(request):
    cob = contractor.objects.all()
    return render(request,'worker/SEND_FEEDBACK.html',{'val':cob})

@login_required(login_url='/') #for login authentication
def sendFeedbackCon(request):
    contractorName = request.POST['select']
    feedback = request.POST['textarea']
    rating = request.POST['select2']
    ob = wkr_review()
    ob.wid = worker.objects.get(lid__id=request.session['lid'])
    ob.cid = contractor.objects.get(id=contractorName)
    ob.feedback = feedback
    ob.rating = rating
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("Feedback sent ");window.location='/sendContractorFeedback'</script>''')


@login_required(login_url='/') #for login authentication
def viewAssignWork(request):
    wid = worker.objects.get(lid__id=request.session['lid'])
    assigned_work = assignJob.objects.select_related('jid','wid').filter(wid=wid)
    print(assigned_work)
    return render(request,'worker/VIEW_ASSIGN_WORK.html',{'val':assigned_work})

@login_required(login_url='/') #for login authentication
def viewVideoWorker(request):
    vob = video.objects.all()
    return render(request,'worker/VIEW_VIDEO_WORKER.html',{'val':vob})

def logout(request):
    auth.logout(request)
    return redirect('/')
from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=90, unique=True)
    password = models.CharField(max_length=90)
    type = models.CharField(max_length=90)

class contractor(models.Model):
    lid = models.ForeignKey(login,on_delete=models.CASCADE)
    fname = models.CharField(max_length=90)
    lname = models.CharField(max_length=90)
    gender = models.CharField(max_length=90)
    phone = models.BigIntegerField()
    place = models.CharField(max_length=150)
    post = models.CharField(max_length=90)
    pin = models.IntegerField()
    email = models.EmailField()
    experience = models.IntegerField()

class user(models.Model):
    lid = models.ForeignKey(login,on_delete=models.CASCADE)
    fname = models.CharField(max_length=90)
    lname = models.CharField(max_length=90)
    gender = models.CharField(max_length=90)
    phone = models.BigIntegerField()
    place = models.CharField(max_length=150)
    post = models.CharField(max_length=90)
    pin = models.IntegerField()
    email = models.EmailField()

class worker(models.Model):
    lid = models.ForeignKey(login,on_delete=models.CASCADE)
    cid = models.ForeignKey(contractor,on_delete=models.CASCADE)
    fname = models.CharField(max_length=90)
    lname = models.CharField(max_length=90)
    gender = models.CharField(max_length=90)
    phone = models.BigIntegerField()
    place = models.CharField(max_length=150)
    post = models.CharField(max_length=90)
    pin = models.IntegerField()
    email = models.EmailField()
    experience = models.IntegerField()
    availability = models.CharField(max_length=90)
    probation_period = models.CharField(max_length=90)
    probation_length = models.CharField(max_length=90)

class usr_complaint(models.Model):
    uid=models.ForeignKey(user,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=200)
    reply=models.CharField(max_length=200)
    date=models.DateField()

class usr_review(models.Model):
    uid = models.ForeignKey(user, on_delete=models.CASCADE)
    feedback=models.TextField()
    rating=models.IntegerField()
    date=models.DateField()

class wkr_complaint(models.Model):
    wid = models.ForeignKey(worker,on_delete=models.CASCADE)
    cid = models.ForeignKey(contractor,on_delete=models.CASCADE)
    complaint = models.CharField(max_length=200)
    reply = models.CharField(max_length=200)
    date = models.DateField()

class wkr_review(models.Model):
    wid = models.ForeignKey(worker, on_delete=models.CASCADE)
    cid = models.ForeignKey(contractor, on_delete=models.CASCADE)
    feedback = models.TextField()
    rating = models.IntegerField()
    date = models.DateField()

class job(models.Model):
    cid = models.ForeignKey(contractor, on_delete=models.CASCADE)
    job = models.CharField(max_length=90)
    jobDetails = models.CharField(max_length=200)
    date = models.DateField()

class contractorWorks(models.Model):
    cid = models.ForeignKey(contractor, on_delete=models.CASCADE)
    uid = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    work = models.CharField(max_length=150)
    image = models.FileField()
    description = models.TextField()
    status = models.CharField(max_length=90)
    date = models.DateField()

class usr_work_request(models.Model):
    uid = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    # cid = models.ForeignKey(contractor, on_delete=models.CASCADE)
    # work = models.CharField(max_length=200)
    cwid = models.ForeignKey(contractorWorks, on_delete=models.CASCADE)
    status = models.CharField(max_length=90)
    date = models.DateField()

class assignJob(models.Model):
    cid = models.ForeignKey(contractor, on_delete=models.CASCADE)
    wid = models.ForeignKey(worker, on_delete=models.CASCADE)
    jid = models.ForeignKey(job, on_delete=models.CASCADE)
    jobStatus = models.CharField(max_length=90)
    date = models.DateField()

class video(models.Model):
    video = models.FileField()
    description = models.TextField()
    date = models.DateField()





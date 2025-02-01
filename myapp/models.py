from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=128)
    u_type = models.CharField(max_length=10)

    def set_password(self, raw_password):
        self.passwd = make_password(raw_password)

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.passwd)

    def __str__(self):
        return self.uname


class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.fname

class type_master(models.Model):
    type_name = models.CharField(max_length=150)

class data_set(models.Model):
    keywords = models.CharField(max_length=500)
    type_id = models.IntegerField()

class question_pool(models.Model):
    question = models.CharField(max_length=350)
    level = models.CharField(max_length=10)

class user_exam(models.Model):
    user_id = models.IntegerField()
    question_id = models.IntegerField()
    answer = models.CharField(max_length=250)
    category = models.CharField(max_length=25)
    dt = models.CharField(max_length=25)
    tm = models.CharField(max_length=25)

class user_video_log(models.Model):
    user_id = models.IntegerField()
    file_path = models.CharField(max_length=350)
    result = models.CharField(max_length=350)
    dt = models.CharField(max_length=350)
    tm = models.CharField(max_length=350)
    result_caption = models.CharField(max_length=350)

    def __str__(self):
        return self.result

class user_notifications(models.Model):
    user_id = models.IntegerField()
    msg = models.CharField(max_length=25)
    dt = models.CharField(max_length=25)
    tm = models.CharField(max_length=25)

class user_login_log(models.Model):
    user_id = models.IntegerField()
    remarks = models.CharField(max_length=25)
    dt = models.CharField(max_length=25)
    tm = models.CharField(max_length=25)

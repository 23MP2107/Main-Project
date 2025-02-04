from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')

def webcam_test(request):
    return render(request, './myapp/webcam_test.html')

#################################################################
############################ ADMIN ################################
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)


from .models import type_master


def admin_type_master_add(request):
    if request.method == 'POST':
        type_name = request.POST.get('type_name')
        tm = type_master(type_name=type_name)
        tm.save()
        context = {'msg': 'Record Added'}
        return render(request, './myapp/admin_type_master_add.html', context)
    else:
        return render(request, './myapp/admin_type_master_add.html')


def admin_type_master_edit(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        type_name = request.POST.get('type_name')
        tm = type_master.objects.get(id=int(s_id))

        tm.type_name = type_name
        tm.save()
        msg = 'Record Updated'
        tm_l = type_master.objects.all()
        context = {'type_list': tm_l, 'msg': msg}
        return render(request, './myapp/admin_type_master_view.html', context)
    else:
        id = request.GET.get('id')
        tm = type_master.objects.get(id=int(id))
        context = {'type_name': tm.type_name, 's_id': tm.id}
        return render(request, './myapp/admin_type_master_edit.html',context)


def admin_type_master_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    tm = type_master.objects.get(id=int(id))
    tm.delete()
    msg = 'Record Deleted'
    tm_l = type_master.objects.all()
    context = {'type_list': tm_l, 'msg':msg}
    return render(request, './myapp/admin_type_master_view.html',context)


def admin_type_master_view(request):
    tm_l = type_master.objects.all()
    context = {'type_list':tm_l}
    return render(request, './myapp/admin_type_master_view.html',context)

from project.settings import BASE_DIR
import os
from .models import data_set

def admin_data_set_add(request):
    if request.method == 'POST':
        type_id = request.POST.get('type_id')
        tm = type_master.objects.get(id=int(type_id))

        data_path = request.POST.get('data_path')
        ds = data_set(type_id=tm.id,keywords=data_path)
        ds.save()

        tm_l = type_master.objects.all()
        context = {'msg': 'Record Added', 'type_list': tm_l}
        return render(request, './myapp/admin_data_set_add.html', context)
    else:
        tm_l = type_master.objects.all()
        context = {'msg': '', 'type_list': tm_l}
        return render(request, './myapp/admin_data_set_add.html',context)


def admin_data_set_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    ds = data_set.objects.get(id=int(id))
    ds.delete()
    msg = 'Record Deleted'
    ds_l = data_set.objects.all()
    tm_l = type_master.objects.all()
    context = {'data_list': ds_l, 'msg':msg,'type_list':tm_l}
    return render(request, './myapp/admin_data_set_view.html',context)


def admin_data_set_view(request):
    msg =''
    ds_l = data_set.objects.all()
    tm_l = type_master.objects.all()
    context = {'data_list': ds_l, 'msg': msg, 'type_list': tm_l}
    return render(request, './myapp/admin_data_set_view.html', context)


from .models import question_pool
def admin_question_pool_add(request):
    if request.method == 'POST':
        question = request.POST.get('question')


        level = request.POST.get('level')
        ds = question_pool(question=question,level=level)
        ds.save()

        context = {'msg': 'Record Added'}
        return render(request, './myapp/admin_question_pool_add.html', context)
    else:

        context = {'msg': ''}
        return render(request, './myapp/admin_question_pool_add.html',context)


def admin_question_pool_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    ds = question_pool.objects.get(id=int(id))
    ds.delete()
    msg = 'Record Deleted'
    question_list = question_pool.objects.all()
    context = {'question_list': question_list, 'msg':msg}
    return render(request, './myapp/admin_question_pool_view.html',context)


def admin_question_pool_view(request):
    msg =''

    question_list = question_pool.objects.all()
    context = {'question_list': question_list, 'msg': msg}
    return render(request, './myapp/admin_question_pool_view.html', context)

def admin_user_view(request):
    ul_l = user_login.objects.filter(u_type='user')

    tm_l = []
    for u in ul_l:
        ud = user_details.objects.get(user_id=u.id)
        tm_l.append(ud)

    context = {'user_list':tm_l,'type':'User Details'}
    return render(request, './myapp/admin_user_view.html',context)

def admin_user_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = user_details.objects.get(id=int(id))
    u_l = user_login.objects.get(id= nm.user_id)
    u_l.delete()

    nm.delete()

    ul_l = user_login.objects.filter(u_type='user')

    tm_l = []
    for u in ul_l:
        ud = user_details.objects.get(user_id=u.id)
        tm_l.append(ud)

    context = {'user_list': tm_l, 'type': 'User Details','msg':'User Removed'}
    return render(request, './myapp/admin_user_view.html', context)


def admin_user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, age=age,addr=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/admin_user_details_add.html',context)

    else:
        return render(request, 'myapp/admin_user_details_add.html')

#######################################################################
##################### USER ##################################
from django.contrib.auth.hashers import check_password, make_password
from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        try:
            ul = user_login.objects.get(uname=uname, u_type='user')
            if check_password(passwd, ul.passwd):  # Use check_password here
                # Retrieve user details
                user = user_details.objects.get(user_id=ul.id)
                
                # Store user info in session
                request.session['user_id'] = user.user_id
                request.session['user_name'] = user.fname  # You can also use 'uname' or 'fname'

                context = {'uname': request.session['user_name']}
                return render(request, 'myapp/user_home.html', context)
            else:
                context = {'msg': 'Invalid Credentials'}
                return render(request, 'myapp/user_login.html', context)

        except user_login.DoesNotExist:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html', context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname = email
        #status = "new"

        hashed_password = make_password(password)
        ul = user_login(uname=uname, passwd=hashed_password, u_type='user')
        ul.save()
        
         # Save the user details
        ud = user_details(
            user_id=ul.id,  # Use ul.id directly
            fname=fname,
            lname=lname,
            gender=gender,
            age=age,
            addr=addr,
            pin=pin,
            contact=contact,
            email=email
        )
        ud.save()
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html', context)

    else:
        return render(request, 'myapp/user_details_add.html')

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:
            # Retrieve user_login instance
            ul = user_login.objects.get(uname=uname)

            # Verify current password
            if check_password(current_password, ul.passwd):
                # Set and hash the new password
                ul.passwd = make_password(new_password)
                ul.save()
                context = {'msg': 'Password Changed Successfully'}
            else:
                context = {'msg': 'Incorrect current password'}

        except user_login.DoesNotExist:
            context = {'msg': 'User not found'}

        return render(request, 'myapp/user_changepassword.html', context)
    else:
        return render(request, 'myapp/user_changepassword.html')


def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)


from .models import user_exam
def user_user_exam1_add(request):
    if request.method == 'POST':
        question_id = request.POST.getlist('question_id[]')
        answer = request.POST.getlist('answer[]')
        count = len(question_id)
        user_id = request.session['user_id']
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        for i in range(count):
            

            ds = user_exam(user_id=int(user_id),question_id=int(question_id[i]),
                           answer=answer[i],category='category',dt=dt,tm=tm)
            ds.save()

        context = {'msg': 'Exam Added'}
        return render(request, './myapp/user_home.html', context)
    else:
        question_list = question_pool.objects.filter(level='1')

        context = {'msg': '','question_list':question_list}
        return render(request, './myapp/user_user_exam1_add.html',context)
from datetime import datetime

def user_user_exam1_view(request):
    msg =''
    user_id = request.session['user_id']
    question_list = question_pool.objects.filter(level='1')
    exam_list = user_exam.objects.filter(user_id=user_id)
    context = {'msg': '', 'question_list': question_list,'exam_list':exam_list}
    return render(request, './myapp/user_user_exam1_view.html', context)

def user_user_exam2_add(request):
    if request.method == 'POST':
        question_id = request.POST.getlist('question_id[]')
        answer = request.POST.getlist('answer[]')
        count = len(question_id)
        user_id = request.session['user_id']
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        for i in range(count):
            ds = user_exam(user_id=int(user_id),question_id=int(question_id[i]),
                           answer=answer[i],category='category',dt=dt,tm=tm)
            ds.save()

        context = {'msg': 'Exam Added'}
        return render(request, './myapp/user_home.html', context)
    else:
        question_list = question_pool.objects.filter(level='2')

        context = {'msg': '','question_list':question_list}
        return render(request, './myapp/user_user_exam2_add.html',context)

def user_user_exam2_view(request):
    msg =''
    user_id = request.session['user_id']
    question_list = question_pool.objects.filter(level='2')
    exam_list = user_exam.objects.filter(user_id=user_id)
    context = {'msg': '', 'question_list': question_list,'exam_list':exam_list}
    return render(request, './myapp/user_user_exam2_view.html', context)

def user_webcam_test(request):
    return render(request, './myapp/user_webcam_test.html')

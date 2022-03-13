from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from datetime import date


def index(request):
    return render(request, 'index.html')


def contractor_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        comp = request.POST['company']
        try:
            user = User.objects.create_user(
                first_name=f, last_name=l, username=e, password=p)
            ContractorUser.objects.create(
                user=user, mobile=con, image=i, company=comp, type="contractor")
            error = "no"
        except Exception as e:
            error = "yes"
            print(e)
    d = {'error': error}
    return render(request, 'cregister.html', d)


def contractor_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = ContractorUser.objects.get(user=user)
                if user1.type == "contractor":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'clogin.html', d)


def government_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        state = request.POST['state']
        try:
            user = User.objects.create_user(
                first_name=f, last_name=l, username=e, password=p)
            GovernmentUser.objects.create(
                user=user, mobile=con, image=i, state=state, type="government")
            error = "no"
        except Exception as e:
            error = "yes"
            print(e)
    d = {'error': error}
    return render(request, 'gregister.html', d)


def government_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = GovernmentUser.objects.get(user=user)
                if user1.type == "government":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'glogin.html', d)


def contractor_home(request):
    if not request.user.is_authenticated:
        return redirect('contractor_login')
    user = request.user
    contractor = ContractorUser.objects.get(user=user)
    d = {'contractor': contractor}
    return render(request, 'chome.html', d)


def government_home(request):
    if not request.user.is_authenticated:
        return redirect('government_login')
    user = request.user
    government = GovernmentUser.objects.get(user=user)
    d = {'government': government}
    return render(request, 'ghome.html', d)


def Logout(request):
    logout(request)
    return redirect('index')


# Government functions

def add_contract(request):
    if not request.user.is_authenticated:
        return redirect('government_login')
    error = ""
    if request.method == 'POST':
        ct = request.POST['contract_title']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        budg = request.POST['budget']
        cd = request.FILES['cd']
        loc = request.POST['location']
        des = request.POST['description']
        user = request.user
        govt = GovernmentUser.objects.get(user=user)
        try:
            Contract.objects.create(government=govt, start_date=sd, end_date=ed, title=ct, doc=cd,
                                    description=des, location=loc, creationdate=date.today(), type="contract")
            error = "no"
        except Exception as e:
            error = "yes"
            print(e)
    d = {'error': error}
    return render(request, 'gadd_contract.html', d)


def created_contracts_list(request):
    if not request.user.is_authenticated:
        return redirect('government_login')
    user = request.user
    govt = GovernmentUser.objects.get(user=user)
    cont = Contract.objects.filter(government=govt)
    d = {'contract': cont}
    return render(request, 'gcreated_contracts_list.html', d)


def edit_contract(request, pid):
    if not request.user.is_authenticated:
        return redirect('government_login')
    error = ""
    contract = Contract.objects.get(id=pid)
    if request.method == 'POST':
        jt = request.POST['contract_title']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        budg = request.POST['budget']
        loc = request.POST['location']
        des = request.POST['description']

        contract.title = jt
        contract.budget = budg
        contract.location = loc
        contract.description = des
        try:
            contract.save()
            error = "no"
        except:
            error = "yes"
        if sd:
            try:
                contract.start_date = sd
                contract.save()
            except:
                pass
        else:
            pass
        if ed:
            try:
                contract.end_date = ed
                contract.save()
            except:
                pass
        else:
            pass
    d = {'error': error, 'contract': contract}
    return render(request, 'gedit_contract.html', d)


def contractors_applied(request):
    if not request.user.is_authenticated:
        return redirect('government_login')
    contractor = ContractorUser.objects.all()
    contractors = []
    for i in contractor:
        if i.amount != None:
            contractors.append(i)
    d = {'contractor': contractors}
    return render(request, 'gcontractors_applied.html', d)


def delete_contract(request, pid):
    pass


def government_changepassword(request):
    if not request.user.is_authenticated:
        return redirect('government_login')
    error = ""
    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'gchangepassword.html', d)


# Contractors Functions
def contractor_changepassword(request):
    if not request.user.is_authenticated:
        return redirect('contractor_login')
    error = ""
    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'cchangepassword.html', d)


def contractor_contractslist(request):
    if not request.user.is_authenticated:
        return redirect('contractor_login')
    contract = Contract.objects.all()
    d = {'contract': contract}
    return render(request, 'cavailable_contracts.html', d)


def assigned_contractslist(request):
    pass


def apply_contract(request, pid):
    if not request.user.is_authenticated:
        return redirect('contractor_login')
    error = ""
    user = request.user
    contractor = ContractorUser.objects.get(user=user)
    if request.method == 'POST':
        amt = request.POST['amount']
        quot = request.FILES['test']
        contractor.amount = amt
        contractor.quot_doc = quot
        contractor.contr = pid
        try:
            contractor.save()
            error = "no"
        except:
            error = "yes"

    d = {'error': error, 'contractor': contractor}
    return render(request, 'capply_contract.html', d)

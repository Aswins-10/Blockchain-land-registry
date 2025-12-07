# Create your views here.
from hashlib import sha256
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import ureg
from donate.form import NewDonationCreate
from donate.models import Donate


def donates_all(request):
    uid = request.session['member_id']
    donates = Donate.objects.filter(username_id=uid)
    return render(request, 'alldonationsc.html', {'donates': donates})


def project_donated(request):
    uid = request.session['member_id']
    donates = Donate.objects.filter(username_id=uid).values('projectname').distinct()
    return render(request, 'alldonates.html', {'donates': donates})


def project_donated_dtls(request, product_id):
    uid = request.session['member_id']
    donates = Donate.objects.filter(projectname_id=product_id)
    return render(request, 'alldontions.html', {'donates': donates})


def upload(request):
    uploaditem = NewDonationCreate()
    frm_name = "Project Details"
    if request.method == 'POST':
        uploaditem = NewDonationCreate(request.POST, request.FILES)
        # uploaditem.data=uploaditem.data.copy()
        uid = request.session['member_id']
        una = ureg.objects.get(id=uid)
        # uploaditem.data['username']=una
        if uploaditem.is_valid():
            projectname = uploaditem.cleaned_data['projectname']
            allready_c = Donate.objects.filter(projectname_id=projectname).exists()
            if allready_c:
                prevproject = Donate.objects.filter(projectname_id=projectname).last()
                prevhash = prevproject.hash
            else:
                prevhash = ""
            ct = datetime.now()
            ts = ct.timestamp()
            hash1 = str(projectname.id) + str(uid) + str(ts)
            hash = sha256(hash1.encode()).hexdigest()
            remarks = uploaditem.cleaned_data['remarks']
            amount = uploaditem.cleaned_data['amount']
            frm = Donate(projectname=projectname, remarks=remarks, amount=amount, username=una, prevhash=prevhash,
                         hash=hash)
            frm.save()
            # uploaditem.save()
            return redirect('donates_all')
        else:
            return HttpResponse(""" Something went wrong click <a href= "{{url: 'donates_all'}}">Reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form': uploaditem, 'title': frm_name})  # need to change


def update_project_donates(request, product_id):
    donates_id = int(donates_id)
    try:
        donates_shelf = Donate.objects.get(projectname_id=product_id)
    except Donate.DoesNotExist:
        return redirect('donates_all')
    donates_form = NewDonationCreate(request.POST or None, instance=donates_shelf)
    if donates_form.is_valid():
        donates_form.save()
        return redirect('donates_all')
    frm_name = "Donation Details"
    return render(request, 'upload_form.html', {'upload_form': donates_form, 'title': frm_name})


def update_donates_uid(request, donates_id):
    donates_id = int(donates_id)
    try:
        donates_shelf = Donate.objects.get(id=donates_id)
    except Donate.DoesNotExist:
        return redirect('donates_all')
    donates_form = NewDonationCreate(request.POST or None, instance=donates_shelf)
    if donates_form.is_valid():
        donates_form.save()
        return redirect('donates_all')
    frm_name = "Donation Details"
    return render(request, 'upload_form.html', {'upload_form': donates_form, 'title': frm_name})


def update_donates(request, donates_id):
    donates_id = int(donates_id)
    try:
        donates_shelf = Donate.objects.get(id=donates_id)
    except Donate.DoesNotExist:
        return redirect('donates_all')
    donates_form = NewDonationCreate(request.POST or None, instance=donates_shelf)
    if donates_form.is_valid():
        donates_form.save()
        return redirect('donates_all')
    frm_name = "Donation Details"
    return render(request, 'upload_form.html', {'upload_form': donates_form, 'title': frm_name})


def delete_donates(request, donates_id):
    donates_id = int(donates_id)
    try:
        donates_shelf = Donate.objects.get(id=donates_id)
    except Donate.DoesNotExist:
        return redirect('donates_all')
    donates_shelf.delete()
    return redirect('donates_all')

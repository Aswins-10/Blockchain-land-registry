from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from hashlib import sha256
from datetime import datetime
# Create your views here.
from app.models import ureg
from donate.models import Block
from works.form import NewWorksCreate, NewExpenditureCreate, PropertyCreate
from works.models import NewWorks, WorkExpenditure, Property, PurchaseInterest


def works_all(request):
    works = Property.objects.all()
    return render(request, 'allworks.html', {'works': works,'title': 'Land Details'})


def Property_owner_all(request):
    sid = request.session['member_id']
    works = Property.objects.filter(Owner_id=sid, status=True)
    return render(request, 'allworks.html', {'works': works,'title': 'View Land Owned By You'})

def land_for_purchase(request):
    sid = request.session['member_id']
    works = Property.objects.filter(~Q(Owner_id =sid), status=True, Tosell=True)
    return render(request, 'allland.html', {'works': works, 'title': 'View Land For Sale'})

def land_more_details(request,land_id):
    land_id = int(land_id)
    try:
        property_shelf = Property.objects.get(id=land_id)
        if request.method =="POST":
            amt = request.POST.get('amount')
            sid = request.session['member_id']
            user = ureg.objects.filter(id=sid).first()
            PurchaseInterest(PropertyName=property_shelf,Interestee=user,Priceoffered=amt).save()
            return redirect('purchase_req')
    except Property.DoesNotExist:
        return redirect('Property_owner_all')
    return render(request, 'landdetails.html', {'works': property_shelf, 'title': 'View Land For Sale'})

def purchase_req(request):
    try:
        sid = request.session['member_id']
        user = ureg.objects.filter(id=sid).first()
        works = PurchaseInterest.objects.filter(Interestee=user)
    except Property.DoesNotExist:
        return redirect('Property_owner_all')
    return render(request, 'interested.html', {'works': works, 'title': 'Purchase Request Send'})


def land_purchase_request(request):
    sid = request.session['member_id']
    works = Property.objects.filter(Owner_id=sid, status=True)
    return render(request, 'landpurchaserequest.html', {'works': works, 'title': 'View Land You Want to Sale'})




def land_set_sell(request, land_id):
    land_id = int(land_id)
    try:
        property_shelf = Property.objects.get(id=land_id)
    except Property.DoesNotExist:
        return redirect('Property_owner_all')
    cid = str(property_shelf.id)
    property_shelf.Tosell = not property_shelf.Tosell
    property_shelf.save(update_fields=['Tosell'])
    return  redirect('Property_owner_all')


def land_set_approve(request, land_id):
    land_id = int(land_id)
    try:
        property_shelf = Property.objects.get(id=land_id)
    except Property.DoesNotExist:
        return redirect('works_all')
    cid = str(property_shelf.id)
    property_shelf.status = not property_shelf.status
    property_shelf.save(update_fields=['status'])

    allready_c = Block.objects.all()
    if allready_c:
        prevproject = Block.objects.all().last()
        prevhash = prevproject.hash
    else:
        prevhash = ""
    ct = datetime.now()
    ts = ct.timestamp()
    uid=property_shelf.Owner.id
    hash1 = str(property_shelf.id) + str(uid) + str(ts)
    hash = sha256(hash1.encode()).hexdigest()
    frm = Block(projectname=property_shelf,username =property_shelf.Owner, prevhash=prevhash,hash=hash)
    frm.save()

    return  redirect('works_all')

def land_p_interest(request,interest_id):
    interest_id = int(interest_id)
    property_shelf = Property.objects.get(id=interest_id)
    works = PurchaseInterest.objects.filter(PropertyName=property_shelf)
    return render(request, 'requestreceived.html', {'works': works, 'title': 'Purchase Request Received'})

def approve_sale(request):
    works = PurchaseInterest.objects.all()
    return render(request, 'approvesale.html', {'works': works, 'title': 'Purchase Requests'})




def changestatus_workexp(request, work_id):
    work_id = int(work_id)
    try:
        expenditure_shelf = WorkExpenditure.objects.get(id=work_id)
    except WorkExpenditure.DoesNotExist:
        return redirect('expenditure_all')
    expenditure_shelf.status = not expenditure_shelf.status
    expenditure_shelf.save(update_fields=['status'])
    return redirect('expenditure_all')

def request_accept(request, interest_id):
    interest_id = int(interest_id)
    try:
        works = PurchaseInterest.objects.get(id=interest_id)
        id=works.PropertyName.id
    except WorkExpenditure.DoesNotExist:
        return redirect('expenditure_all')
    works.status = "Accepted"
    works.save(update_fields=['status'])
    return redirect('land_p_interest',interest_id=id)

def request_approve(request, interest_id):
    interest_id = int(interest_id)
    try:
        works = PurchaseInterest.objects.get(id=interest_id)
        prjt = works.PropertyName
        Interestee = works.Interestee

        id = works.PropertyName.id
    except Exception as e:
        return redirect('expenditure_all')
    works.status = "Approved"
    works.save(update_fields=['status'])
    prjt.Owner = Interestee
    prjt.Tosell=False
    prjt.save(update_fields=['Owner','Tosell'])
    return redirect('approve_sale')



def upload(request):
    uploaditem = PropertyCreate()
    frm_name = "Land Details"
    if request.method == 'POST':
        uploaditem = PropertyCreate(request.POST, request.FILES)
        if uploaditem.is_valid():
            sid = request.session['member_id']
            Ld = uploaditem.cleaned_data['LocationDetails']
            District = uploaditem.cleaned_data['District']
            Place = uploaditem.cleaned_data['Place']
            sno = uploaditem.cleaned_data['Surveyno']
            PVal = uploaditem.cleaned_data['PriceValue']
            Owner=ureg.objects.filter(id=sid).first()
            Property(LocationDetails=Ld,District=District,Surveyno=sno,PriceValue=PVal, Place = Place, Owner=Owner).save()
            return redirect('Property_owner_all')
        else:
            return HttpResponse(""" Something went wrong click <a href= "{{url: 'works_all'}}">Reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form': uploaditem, 'title': frm_name})  # need to change


def update_works(request, works_id):
    works_id = int(works_id)
    try:
        works_shelf = Property.objects.get(id=works_id)
    except NewWorks.DoesNotExist:
        return redirect('works_all')
    works_form = PropertyCreate(request.POST or None, instance=works_shelf)
    if works_form.is_valid():
        works_form.save()
        return redirect('works_all')
    frm_name = "Project Details"
    return render(request, 'upload_form.html', {'upload_form': works_form, 'title': frm_name})


def delete_works(request, works_id):
    works_id = int(works_id)
    try:
        works_shelf = Property.objects.get(id=works_id)
    except Property.DoesNotExist:
        return redirect('expenditure_all')
    works_shelf.delete()
    return redirect('works_all')


def expenditure_all(request):
    expenditure = WorkExpenditure.objects.all()
    return render(request, 'allexpenditure.html', {'expenditure': expenditure})


def upload_expenditure(request):
    uploaditem = NewExpenditureCreate()
    frm_name = "Expenditure Details"
    if request.method == 'POST':
        uploaditem = NewExpenditureCreate(request.POST, request.FILES)
        if uploaditem.is_valid():
            uploaditem.save()
            return redirect('expenditure_all')
        else:
            return HttpResponse(""" Something went wrong click <a href= "{{url: 'expenditure_all'}}">Reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form': uploaditem, 'title': frm_name})  # need to change





def update_expenditure(request, expenditure_id):
    expenditure_id = int(expenditure_id)
    try:
        expenditure_shelf = WorkExpenditure.objects.get(id=expenditure_id)
    except Newexpenditure.DoesNotExist:
        return redirect('expenditure_all')
    expenditure_form = NewExpenditureCreate(request.POST or None, instance=expenditure_shelf)
    if expenditure_form.is_valid():
        expenditure_form.save()
        return redirect('expenditure_all')
    frm_name = "Expenditure Details"
    return render(request, 'upload_form.html', {'upload_form': expenditure_form, 'title': frm_name})


def delete_expenditure(request, expenditure_id):
    expenditure_id = int(expenditure_id)
    try:
        expenditure_shelf = WorkExpenditure.objects.get(id=expenditure_id)
    except WorkExpenditure.DoesNotExist:
        return redirect('expenditure_all')
    expenditure_shelf.delete()
    return redirect('expenditure_all')

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import ureg
from complaint.form import ComplaintCreate
from complaint.models import Complaint


def complaint_all(request):
    if 'member_type' in request.session and request.session['member_type']=='euser':
        uid = request.session['member_id']
        complaint = Complaint.objects.filter(username_id=uid)
        return render(request, 'allcomplaint.html', {'complaint': complaint})
    elif 'member_type' not in request.session:
        return redirect('function')

    complaint = Complaint.objects.all()
    return render(request, 'allcomplaint.html', {'complaint': complaint})


def cutomcomplaint_all(request, customer_id):
    complaint = Complaint.objects.filter(customer_id=customer_id)
    return render(request, 'allcomplaint.html', {'complaint': complaint})


def upload(request):
    uploaditem = ComplaintCreate()
    frm_name = "Complaint Details"
    if request.method == 'POST':
        uploaditem = ComplaintCreate(request.POST, request.FILES)
        if uploaditem.is_valid():
            uploaditem.save()
            return redirect('complaint_all')
        else:
            return HttpResponse(""" Something went wrong click <a href= "{{url: 'complaint_all'}}">Reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form': uploaditem, 'title': frm_name})  # need to change


def upload_custom(request):
    upload = ComplaintCreate()
    frm_name = "Complaint Details"
    if 'member_type' not in request.session:
        return redirect('function')
    uid = request.session['member_id']
    mtype = request.session['member_type']
    if request.method == 'POST':
        upload = ComplaintCreate(request.POST, request.FILES)
        if upload.is_valid():
            subject = upload.cleaned_data['subject']
            comtext = upload.cleaned_data['complainttext']
            pjtname = upload.cleaned_data['projectname']
            upload = upload.cleaned_data['upload']
            una = ureg.objects.get(id=uid)
            frm = Complaint(subject=subject, complainttext=comtext, username=una, projectname=pjtname, upload=upload)
            frm.save()
            return redirect('complaint_all')  # redirect to company list actually to user home
        else:
            return HttpResponse(""" Something went wrong click <a href= "{{url: 'complaint_all'}}">Reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form': upload, 'title': frm_name})  # need to change


def update_custom(request, complaint_id):
    upload = ComplaintCreate()
    complaints_id = int(complaint_id)
    frm_name = "Complaint Details"
    try:
        complaints_shelf = Complaint.objects.get(id=complaints_id)
    except Complaint.DoesNotExist:
        return redirect('complaint_all')
    complaints_form = ComplaintCreate(request.POST or None, instance=complaints_shelf)
    if complaints_form.is_valid():
        complaints_form.save()
        return redirect('complaint_all')
    return render(request, 'upload_form.html', {'upload_form': complaints_form, 'title': frm_name})


# def update_complaint(request, complaint_id):
#     complaint_id = int(complaint_id)
#     try:
#         complaint_shelf = Complaint.objects.get(id=complaint_id)
#     except Complaint.DoesNotExist:
#         return redirect('complaint_all')
#     complaint_form = ComplaintCreate(request.POST or None, instance=complaint_shelf)
#     if complaint_form.is_valid():
#         complaint_form.save()
#         return redirect('complaint_all')
#     frm_name = "Complaint Details"
#     return render(request, 'upload_form.html', {'upload_form': complaint_form, 'title': frm_name})
#
#
def delete_complaint(request, complaint_id):
    complaint_id = int(complaint_id)
    try:
        complaint_shelf = Complaint.objects.get(id=complaint_id)
    except Complaint.DoesNotExist:
        return redirect('complaint_all')
    complaint_shelf.delete()
    return redirect('complaint_all')

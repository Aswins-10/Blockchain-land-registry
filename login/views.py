from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.


# def company_login(request):
#     if request.method != 'POST':
#         # raise Http404('Only POSTs are allowed')
#         return render(request, 'companylogin.html')
#     try:
#         m = Company.objects.get(username=request.POST['username'])
#         if m.password == request.POST['password']:
#             request.session['member_id'] = m.id
#             request.session['member_type'] = 'company'
#             return render(request, 'companyhome.html')
#             # return HttpResponseRedirect('/you-are-logged-in/')
#         else:
#             return HttpResponse(
#                 "<div style='margin-left:15%;margin-top:15%' >Your username and password didn't match.<a href='' %}'>CLICK HERE TO GO BACK</a></div>")
#     except Company.DoesNotExist:
#         return HttpResponse("Your username and password didn't match.")


# def customer_login(request):
#     if request.method != 'POST':
#         # raise Http404('Only POSTs are allowed')
#         return render(request, 'customerlogin.html')
#     try:
#         m = Customer.objects.get(username=request.POST['username'])
#         if m.password == request.POST['password']:
#             request.session['member_id'] = m.id
#             request.session['member_type'] = 'customer'
#             return render(request, 'companyhome.html')
#             # return HttpResponseRedirect('/you-are-logged-in/')
#         else:
#             return HttpResponse(
#                 "<div style='margin-left:15%;margin-top:15%' >Your username and password didn't match.<a href='' %}'>CLICK HERE TO GO BACK</a></div>")
#     except Customer.DoesNotExist:
#         return HttpResponse("Your username and password didn't match.")


# def staff_login(request):
#     if request.method != 'POST':
#         # raise Http404('Only POSTs are allowed')
#         return render(request, 'stafflogin.html')
#     try:
#         m = Staff.objects.get(username=request.POST['username'])
#         if m.password == request.POST['password']:
#             request.session['member_id'] = m.id
#             request.session['member_type'] = 'staff'
#             request.session['com_id'] = m.company_id
#             return render(request, 'companyhome.html')
#             # return HttpResponseRedirect('/you-are-logged-in/')
#         else:
#             return HttpResponse(
#                 "<div style='margin-left:15%;margin-top:15%' >Your username and password didn't match.<a href='' %}'>CLICK HERE TO GO BACK</a></div>")
#     except Staff.DoesNotExist:
#         return HttpResponse("Your username and password didn't match.")


def logout(request):
    try:
        del request.session['member_id']
        del request.session['member_type']
        del request.session['name']
    except KeyError:
        pass
    return redirect('function')

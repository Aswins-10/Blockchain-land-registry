from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from app.models import ureg
from comment.form import CommentCreate
from comment.models import Comment
#from comment.sentiment import analizeComment
from works.models import NewWorks


def comment_all(request):
    if 'member_type' in request.session and request.session['member_type'] == 'euser':
        uid = request.session['member_id']
        comment = Comment.objects.filter(username_id=uid)
        return render(request, 'allcomment.html', {'comment': comment})
    elif 'member_type' not in request.session:
        return redirect('function')

    comment = Comment.objects.all()
    return render(request, 'allcomment.html', {'comment': comment})


def comment_list(request):
    if 'member_type' in request.session and request.session['member_type'] != 'euser':
        comment = Comment.objects.all()
        return render(request, 'prediction.html', {'comment': comment})
    else:
        return redirect('function')


# def cutomcomment_all(request, customer_id):
#     comment = Comment.objects.filter(customer_id=customer_id)
#     return render(request, 'allcomment.html', {'comment': comment})


# def upload(request):
#     uploaditem = CommentCreate()
#     frm_name = "Comment Details"
#     if request.method == 'POST':
#         uploaditem = CommentCreate(request.POST, request.FILES)
#         if uploaditem.is_valid():
#             uploaditem.save()
#             return redirect('comment_all')
#         else:
#             return HttpResponse(""" Something went wrong click <a href= "{{url: 'comment_all'}}">Reload</a>""")
#     else:
#         return render(request, 'upload_form.html', {'upload_form': uploaditem, 'title': frm_name})  # need to change


def upload_custom(request):
    upload = CommentCreate()
    frm_name = "Comment Details"
    if 'member_type' not in request.session:
        return redirect('function')
    uid = request.session['member_id']
    mtype = request.session['member_type']
    if request.method == 'POST':
        upload = CommentCreate(request.POST, request.FILES)
        if upload.is_valid():
            comtext = upload.cleaned_data['commenttext']
            pjtname = upload.cleaned_data['projectname']
            una = ureg.objects.get(id=uid)
            frm = Comment(commenttext=comtext, username=una, projectname=pjtname)
            frm.save()
            return redirect('comment_all')  # redirect to company list actually to user home
        else:
            return HttpResponse(""" Something went wrong click <a href= "{{url: 'comment_all'}}">Reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form': upload, 'title': frm_name})  # need to change


def update_custom(request, comment_id):
    upload = CommentCreate()
    comments_id = int(comment_id)
    frm_name = "Comment Details"
    try:
        comments_shelf = Comment.objects.get(id=comments_id)
    except Comment.DoesNotExist:
        return redirect('comment_all')
    comments_form = CommentCreate(request.POST or None, instance=comments_shelf)
    if comments_form.is_valid():
        comments_form.save()
        return redirect('comment_all')
    return render(request, 'upload_form.html', {'upload_form': comments_form, 'title': frm_name})


# def update_comment(request, comment_id):
#     comment_id = int(comment_id)
#     try:
#         comment_shelf = Comment.objects.get(id=comment_id)
#     except Comment.DoesNotExist:
#         return redirect('comment_all')
#     comment_form = CommentCreate(request.POST or None, instance=comment_shelf)
#     if comment_form.is_valid():
#         comment_form.save()
#         return redirect('comment_all')
#     frm_name = "Comment Details"
#     return render(request, 'upload_form.html', {'upload_form': comment_form, 'title': frm_name})
#
#
def delete_comment(request, comment_id):
    comment_id = int(comment_id)
    try:
        comment_shelf = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return redirect('comment_all')
    comment_shelf.delete()
    return redirect('comment_all')


def analyse_comment(request, pjt_id):
    project_id = int(pjt_id)
    lable_stat = []
    try:
        comment_shelf = Comment.objects.filter(projectname_id=project_id)
        # cmdtext = comment_shelf.commenttext
        #lable_stat = analizeComment(comment_shelf)
        lable_stat
        works_shelf = NewWorks.objects.filter(id=project_id).first()
        context = {
            'label': lable_stat["result"],
            'p': lable_stat["pcount"],
            'n': lable_stat["ncount"],
            'pname': works_shelf.ProjectDetails
        }
        # for lab in lable_stat:
        # if lab == 'Positive':
        # comment_shelf.status = True
        # else:
        # comment_shelf.status = False
        return render(request, 'commend_prediction.html', context)
        # return render(request, 'commend_prediction.html',
        #               {'label': lable_stat["result"], 'p': lable_stat["pcount"], 'n': lable_stat["ncount"]})
    except Comment.DoesNotExist:
        return redirect('comment_all')

from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from . import forms
from Stagaire.models import Stage, Stagaire
from django.contrib.auth.decorators import login_required
from Accounts.decorators import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .filters import stageFilter
# Create your views here.




def newStage(request):
    if request.method=='POST':
        form = forms.addStage(request.POST,request.FILES)
        if form.is_valid():
            form.save();
            return redirect('stage:stglist')
        else:
            return render(request,'stages/newStage.html',{'form':form})
    else:
        form = forms.addStage()
        dec = {'form':form}
        return render(request,'stages/newStage.html',dec)


@allowed_users(allowed_roles=['admins'])     
@login_required(login_url="/Accounts/loginUser/")
def stageslist(request):
    stagelst = Stage.objects.all()


    myFilter = stageFilter(request.GET, queryset=stagelst)
    stagelst = myFilter.qs
    



    dec= {'lst':stagelst,'SF':myFilter}
    return render(request,'stages/stageList.html',dec)

@allowed_users(allowed_roles=['admins'])     
@login_required(login_url="/Accounts/loginUser/")
def stageDetaile(request,slg):
    
    obj = Stage.objects.get(StageSlug=slg)
    objs = Stagaire.objects.filter(id=obj.stagaire_id).get()
    args = {'obj':obj, 'objs':objs}
    # return HttpResponse(objs.nom + '/' + objs.prenom) 
    return render(request, 'stages/stageDetail.html', args )

@allowed_users(allowed_roles=['admins'])     
@login_required(login_url="/Accounts/loginUser/")
def editStage(request, stg_id):
    stage = Stage.objects.get(id=stg_id)
    form = forms.addStage(instance=stage)
    
    if request.method == 'POST':
        form =  forms.addStage(request.POST,request.FILES,instance=stage)
        if form.is_valid():
            form.save()
            return redirect('stage:stglist')
        else:
            return render(request,'stages/StageUpdate.html',{'form':form})
    else:
        dec = {'form':form,'A':stage}
        return render(request,'stages/StageUpdate.html',dec)

@allowed_users(allowed_roles=['admins'])     
@login_required(login_url="/Accounts/loginUser/")  
def deleteStg(request,stg_id):
    stage = Stage.objects.get(id=stg_id)
    if request.method == 'POST':
        stage.delete()
        return redirect('stage:stglist')
    else:
        stage = Stage.objects.get(id=stg_id)
        args = {'item':stage}
        return render(request,'stages/deletestage.html',args)




def notifyStgr(request,stg_id):
    stage = Stage.objects.get(id=stg_id)
    stagaire = Stagaire.objects.get(id=stage.stagaire_id)
    if request.method == 'POST':
        subject = 'Training is Soon'
        Fmessage = "Hello {} {}, Your training will start on: {}   And shall ends on: {}.Be Prepared "
        message = Fmessage.format(stagaire.nom,stagaire.prenom,stage.DateDebut,stage.DateFin)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [stagaire.mail,]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('stage:stglist')
    else:
        stage = Stage.objects.get(id=stg_id)
        args = {'item':stage}
        return render(request,'stages/NotifyStagaire.html',args)



def viewRapport(request,rprt_link):
    filelink = 'media_fldr/'+rprt_link
    with open(filelink, 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=some_file.pdf'
        return response
    pdf.closed



    
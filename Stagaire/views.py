from django.shortcuts import render
from .models import Stagaire,Niveau,Filiere
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Accounts.decorators import *
from Accounts.forms import finishInfo
from .filters import stagaireFilter
# Create your views here.

@allowed_users(allowed_roles=['admins'])     
@login_required(login_url="/Accounts/loginUser/")
def stagairelist(request):
    listS = Stagaire.objects.all()


    myFilter = stagaireFilter(request.GET, queryset=listS)
    listS=myFilter.qs
    dec = {'lst':listS,'SF':myFilter}
    return render(request, 'Stagaire/listsgr.html',dec)

@allowed_users(allowed_roles=['admins'])     
@login_required(login_url="/Accounts/loginUser/")
def stagaireDetail(request, Slg):
       
        obj= Stagaire.objects.get(StagaireSlug=Slg)
        dec = {'stger':obj}
        return render(request, 'Stagaire/stgDetail.html',dec)

@allowed_users(allowed_roles=['users']) 

@login_required(login_url="/Accounts/loginUser/")

def stagaireProfile(request):
    currentuser = request.user
    
    currentTrainer = Stagaire.objects.filter(usern_id=currentuser.id).get()
    currentUserNiveau = Niveau.objects.filter(id=currentTrainer.niveau_id).get()
    CuurentUserFilliere = Filiere.objects.filter(id=currentTrainer.filiere_id).get()
    args = {'form':currentTrainer,'form2':currentUserNiveau,'form3':CuurentUserFilliere}
    return render(request, 'Stagaire/trainerProfile.html', args)





@allowed_users(allowed_roles=['admins'])     
@login_required(login_url="/Accounts/loginUser/")
def StagaireUpdate(request, stg_id):
    stage = Stagaire.objects.get(id=stg_id)
    form = finishInfo(instance=stage)
    
    if request.method == 'POST':
        form =  finishInfo(request.POST,instance=stage)
        if form.is_valid(): 
            form.save()
            return redirect('stagaire:liststg')
        else:
            return render(request,'Stagaire/StagaireUpdate.html',{'form':form})
    # else:
    dec = {'form':form,'A':stage}
    return render(request,'Stagaire/StagaireUpdate.html',dec)
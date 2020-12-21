from django.urls import path, re_path
from . import views

app_name = 'stage'

urlpatterns = [
    path('StageList/', views.stageslist, name='stglist'),
    path('newStage/', views.newStage, name='newstg'),
    path('<slug:slg>/', views.stageDetaile, name='stgDetaile'),
    path('edit/<int:stg_id>/', views.editStage, name='editstg'),
    path('delete/<int:stg_id>/', views.deleteStg, name='deletestg'),
    path('notify/<int:stg_id>/',views.notifyStgr,name='Notify'),
    path('Rapport/<str:rprt_link>/',views.viewRapport,name='ViewRapport')
    


    
    
]
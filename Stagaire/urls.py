from django.urls import path
from . import views

app_name = 'stagaire'

urlpatterns = [
    path('liststagaire/', views.stagairelist, name='liststg'),
    path('<slug:Slg>/', views.stagaireDetail, name='detail'),
    path('profile/trainerProfile/', views.stagaireProfile, name='STGProfile'),
    path('edit/<int:stg_id>/', views.StagaireUpdate, name='EditStagaire'),
]
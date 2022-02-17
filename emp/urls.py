from django.urls import path

from .views import TipoDocumentoView, TipoDocumentoNew, TipoDocumentoEdit, SocialSecView, SocialSecNew, SocialSecEdit, \
                   EpsNew, EpsView, EpsEdit, SexoView, SexoNew, SexoEdit, EstadoCivilView, EstadoCivilNew, \
                   EstadoCivilEdit, CiudadNew, CiudadView, CiudadEdit, ProfesionView, ProfesionNew, ProfesionEdit, \
                   NacionalidadView, NacionalidadEdit, NacionalidadNew, EmpleadoView, EmpleadoNew, EmpleadoEdit 

urlpatterns = [
 
    path('documentos/',TipoDocumentoView.as_view(), name='documento_list'),
    path('documentos/new',TipoDocumentoNew.as_view(), name='documento_new'),
    path('documentos/edit/<int:pk>',TipoDocumentoEdit.as_view(), name='documento_edit'),

    path('socials/',SocialSecView.as_view(), name='social_list'),
    path('socials/new',SocialSecNew.as_view(), name='social_new'),
    path('socials/edit/<int:pk>',SocialSecEdit.as_view(), name='social_edit'),

    path('eps/',EpsView.as_view(), name='eps_list'),
    path('eps/new',EpsNew.as_view(), name='eps_new'),
    path('eps/edit/<int:pk>',EpsEdit.as_view(), name='eps_edit'),

    path('estadocivil/',EstadoCivilView.as_view(), name='estadocivil_list'),
    path('estadocivil/new',EstadoCivilNew.as_view(), name='estadocivil_new'),
    path('estadocivil/edit/<int:pk>',EstadoCivilEdit.as_view(), name='estadocivil_edit'),

    path('genero/',SexoView.as_view(), name='genero_list'),
    path('genero/new',SexoNew.as_view(), name='genero_new'),
    path('genero/edit/<int:pk>',SexoEdit.as_view(), name='genero_edit'),

    path('ciudad/',CiudadView.as_view(), name='ciudad_list'),
    path('ciudad/new',CiudadNew.as_view(), name='ciudad_new'),
    path('ciudad/edit/<int:pk>',CiudadEdit.as_view(), name='ciudad_edit'),

    path('profesion/',ProfesionView.as_view(), name='profesion_list'),
    path('profesion/new',ProfesionNew.as_view(), name='profesion_new'),
    path('profesion/edit/<int:pk>',ProfesionEdit.as_view(), name='profesion_edit'),

    path('nacionalidad/',NacionalidadView.as_view(), name='nacionalidad_list'),
    path('nacionalidad/new',NacionalidadNew.as_view(), name='nacionalidad_new'),
    path('nacionalidad/edit/<int:pk>',NacionalidadEdit.as_view(), name='nacionalidad_edit'),

    path('empleado/',EmpleadoView.as_view(), name='empleado_list'),
    path('empleado/new',EmpleadoNew.as_view(), name='empleado_new'),
    path('empleado/edit/<int:pk>',EmpleadoEdit.as_view(), name='empleado_edit'),



]
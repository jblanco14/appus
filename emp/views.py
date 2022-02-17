from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages

from .models import TipoDocumento, SocialSec, Eps, EstadoCivil, Sexo, Ciudad, Profesion, Nacionalidad, Empleado
from .forms import TipoDocumentoForm, SocialSecForm, EpsForm, EstadoCivilForm, SexoForm, CiudadForm, \
                   ProfesionForm, NacionalidadForm, EmpleadoForm


class TipoDocumentoView(LoginRequiredMixin, generic.ListView):
    model = TipoDocumento
    template_name = "emp/documento_list.html" 
    context_object_name = "obj"
    login_url = 'bases:login'

class TipoDocumentoNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = TipoDocumento
    template_name = "emp/documento_form.html"
    context_object_name = "obj"
    form_class=TipoDocumentoForm
    success_url=reverse_lazy("emp:documento_list")
    login_url = 'bases:login'
    success_message="Documento Creado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class TipoDocumentoEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = TipoDocumento
    template_name = "emp/documento_form.html"
    context_object_name = "obj"
    form_class=TipoDocumentoForm
    success_url=reverse_lazy("emp:documento_list")
    login_url = 'bases:login'
    success_message="Documento editado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SocialSecView(LoginRequiredMixin, generic.ListView):
    model = SocialSec
    template_name = "emp/social_list.html" 
    context_object_name = "obj"
    login_url = 'bases:login'

class SocialSecNew(LoginRequiredMixin, generic.CreateView):
    model = SocialSec
    template_name = "emp/social_form.html"
    context_object_name = "obj"
    form_class=SocialSecForm
    success_url=reverse_lazy("emp:social_list")
    login_url = 'bases:login'
    success_message="Social Security Creado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SocialSecEdit(LoginRequiredMixin, generic.UpdateView):
    model = SocialSec
    template_name = "emp/social_form.html"
    context_object_name = "obj"
    form_class=SocialSecForm
    success_url=reverse_lazy("emp:social_list")
    login_url = 'bases:login'
    success_message="Social Security editado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class EpsView(LoginRequiredMixin, generic.ListView):
    model = Eps
    template_name = "emp/eps_list.html" 
    context_object_name = "obj"
    login_url = 'bases:login'

class EpsNew(LoginRequiredMixin, generic.CreateView):
    model = Eps
    template_name = "emp/eps_form.html"
    context_object_name = "obj"
    form_class=EpsForm
    success_url=reverse_lazy("emp:eps_list")
    login_url = 'bases:login'
    success_message="Eps Creada Satisfactoriamente"

    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class EpsEdit(LoginRequiredMixin, generic.UpdateView):
    model = Eps
    template_name = "emp/eps_form.html"
    context_object_name = "obj"
    form_class=EpsForm
    success_url=reverse_lazy("emp:eps_list")
    login_url = 'bases:login'
    success_message="Eps editado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class EstadoCivilView(LoginRequiredMixin, generic.ListView):
    model = EstadoCivil
    template_name = "emp/estadocivil_list.html" 
    context_object_name = "obj"
    login_url = 'bases:login'

    

class EstadoCivilNew(LoginRequiredMixin, generic.CreateView):
    model = EstadoCivil
    template_name = "emp/estadocivil_form.html"
    context_object_name = "obj"
    form_class=EstadoCivilForm
    success_url=reverse_lazy("emp:estadocivil_list")
    login_url = 'bases:login'
    success_message="Estado civil creada satisfactoriamente"
    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
        

class EstadoCivilEdit(LoginRequiredMixin, generic.UpdateView):
    model = EstadoCivil
    template_name = "emp/estadocivil_form.html"
    context_object_name = "obj"
    form_class=EstadoCivilForm
    success_url=reverse_lazy("emp:estadocivil_list")
    login_url = 'bases:login'
    success_message="Estado civil editado satisfactoriamente"

    def form_valid(self,form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SexoView(LoginRequiredMixin, generic.ListView):
    model = Sexo
    template_name = "emp/genero_list.html" 
    context_object_name = "obj"
    login_url = 'bases:login'

class SexoNew(LoginRequiredMixin, generic.CreateView):
    model = Sexo
    template_name = "emp/genero_form.html"
    context_object_name = "obj"
    form_class=SexoForm
    success_url=reverse_lazy("emp:genero_list")
    login_url = 'bases:login'
    success_message="Genero creado satisfactoriamente"

    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class SexoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Sexo
    template_name = "emp/genero_form.html"
    context_object_name = "obj"
    form_class=SexoForm
    success_url=reverse_lazy("emp:genero_list")
    login_url = 'bases:login'
    success_message="Genero editado satisfactoriamente"

    def form_valid(self,form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class CiudadView(LoginRequiredMixin, generic.ListView):
    model = Ciudad
    template_name = "emp/ciudad_list.html" 
    context_object_name = "obj"
    login_url = 'bases:login'

class CiudadNew(LoginRequiredMixin, generic.CreateView):
    model = Ciudad
    template_name = "emp/ciudad_form.html"
    context_object_name = "obj"
    form_class=CiudadForm
    success_url=reverse_lazy("emp:ciudad_list")
    login_url = 'bases:login'
    success_message="Ciudad creada satisfactoriamente"

    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class CiudadEdit(LoginRequiredMixin, generic.UpdateView):
    model = Ciudad
    template_name = "emp/ciudad_form.html"
    context_object_name = "obj"
    form_class=CiudadForm
    success_url=reverse_lazy("emp:ciudad_list")
    login_url = 'bases:login'
    success_message="Ciudad editada satisfactoriamente"

    def form_valid(self,form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)        


class ProfesionView(LoginRequiredMixin, generic.ListView):
    model = Profesion
    template_name = "emp/profesion_list.html" 
    context_object_name = "obj"
    login_url = 'bases:login'

class ProfesionNew(LoginRequiredMixin, generic.CreateView):
    model = Profesion
    template_name = "emp/profesion_form.html"
    context_object_name = "obj"
    form_class=ProfesionForm
    success_url=reverse_lazy("emp:profesion_list")
    login_url = 'bases:login'
    success_message="Registro Creado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProfesionEdit(LoginRequiredMixin, generic.UpdateView):
    model = Profesion
    template_name = "emp/profesion_form.html"
    context_object_name = "obj"
    form_class=ProfesionForm
    success_url=reverse_lazy("emp:profesion_list")
    login_url = 'bases:login'
    success_message="Registro editado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class NacionalidadView(LoginRequiredMixin, generic.ListView):
    model = Nacionalidad
    template_name = "emp/nacionalidad_list.html" 
    context_object_name = "obj"
    login_url = 'bases:login'

class NacionalidadNew(LoginRequiredMixin, generic.CreateView):
    model = Nacionalidad
    template_name = "emp/nacionalidad_form.html"
    context_object_name = "obj"
    form_class=NacionalidadForm
    success_url=reverse_lazy("emp:nacionalidad_list")
    login_url = 'bases:login'
    success_message="Registro Creada Satisfactoriamente"

    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class NacionalidadEdit(LoginRequiredMixin, generic.UpdateView):
    model = Nacionalidad
    template_name = "emp/nacionalidad_form.html"
    context_object_name = "obj"
    form_class=NacionalidadForm
    success_url=reverse_lazy("emp:nacionalidad_list")
    login_url = 'bases:login'
    success_message="Registro editado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class EmpleadoView(LoginRequiredMixin, generic.ListView):
    model = Empleado
    template_name = "emp/empleado_list.html" 
    context_object_name = "obj"
    login_url = 'bases:login'

class EmpleadoNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Empleado
    template_name = "emp/empleado_form.html"
    context_object_name = "obj"
    form_class= EmpleadoForm
    success_url=reverse_lazy("emp:empleado_list")
    login_url = 'bases:login'
    success_message="Registro Creado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class EmpleadoEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Empleado
    template_name = "emp/empleado_form.html"
    context_object_name = "obj"
    form_class=EmpleadoForm
    success_url=reverse_lazy("emp:empleado_list")
    login_url = 'bases:login'
    success_message="Registro Editado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)



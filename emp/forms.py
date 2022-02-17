from django import forms


from .models import TipoDocumento, SocialSec, Eps, EstadoCivil, Sexo, Ciudad, \
    Profesion, Nacionalidad, Empleado

class TipoDocumentoForm(forms.ModelForm):
    
    class Meta:
        model  = TipoDocumento
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripción tipo de documento",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields): 
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class SocialSecForm(forms.ModelForm):
    class Meta:
        model  = SocialSec
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripción Social",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class EpsForm(forms.ModelForm):
    class Meta:
        model  = Eps
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripción Eps",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class EstadoCivilForm(forms.ModelForm):
    class Meta:
        model  = EstadoCivil
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripción Estado civil",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
class SexoForm(forms.ModelForm):
    class Meta:
        model  = Sexo
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripción Genero",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
class CiudadForm(forms.ModelForm):
    class Meta: 
        model  = Ciudad
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripción Ciudades y Municipios",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ProfesionForm(forms.ModelForm):
    class Meta:
        model  = Profesion
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripción profesion de la persona",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class NacionalidadForm(forms.ModelForm):
    class Meta:
        model  = Nacionalidad
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripción Nacionalidad",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class EmpleadoForm(forms.ModelForm):
    fecha_vigencia_licencia = forms.DateInput()
    fecha_nacimiento = forms.DateInput()
    class Meta:
        model= Empleado
        fields=['numero_identificacion','nombres','apellidos','fecha_nacimiento', \
                'lugar_nacimiento','direccion_residencia','barrio','numero_telefonico', \
                'correo_electronico', 'estado', 'social_security', \
                'contacto_emergencia','numero_telefonico2','tipo_documento','ciudad_resident', \
                'eps','nacionalidad','profesion','estado_civil', 'cargo', \
                'sexo']

        exclude = ['um','fm','uc','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    # self.fields['fecha_vigencia_licencia'].widget.attrs['readonly'] = True
    # self.fields['fecha_nacimiento'].widget.attrs['readonly'] = True

       

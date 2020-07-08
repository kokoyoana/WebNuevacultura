from django.shortcuts import redirect,render
from django.views.generic import *
from .models import *
from django.http.response import HttpResponseRedirect
from .forms import Formulario
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.


class Index(ListView):
    model=Inicio
    template_name = 'app/index.html'
    context_object_name= 'ini' 
    queryset = Inicio.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
     
        context['ini'] = Inicio.objects.all()
        context['pro'] = Proyecto.objects.all()
        return context


class Asocia(ListView):
    model = Asociacion
    template_name = 'app/nuestra.html'
    context_object_name= 'aso' 
    queryset = Asociacion.objects.all()[0]


    def get_context_data(self,**kwargs):
        context=super(Asocia, self).get_context_data(**kwargs)

        context['aso'] = Asociacion.objects.all()[0]
        context['pro'] = Proyecto.objects.all()
        return context

class Proyectos(ListView):
    model = Proyecto
    template_name = 'app/proyectos.html'
    context_object_name= 'pro' 
    queryset = Proyecto.objects.all()

 
    def get_context_data(self,**kwargs):
        context=super(Proyectos, self).get_context_data(**kwargs)
        
        context['pro'] = Proyecto.objects.all()
    

        return context 

class Infoproyectos(DetailView):
    template_name = 'app/infoproyectos.html'
    model = Proyecto

    def get_context_data(self,**kwargs):
        context=super(Infoproyectos, self).get_context_data(**kwargs)
        idpro = self.kwargs.get('pk',None)
        context['infop']= Proyecto.objects.get(pk = idpro)
        context['pro'] = Proyecto.objects.all()
        return context


class Talleres(ListView):
    model = Tallere
    template_name = 'app/talleres.html'
    context_object_name= 'tall' 
    queryset = Tallere.objects.all()

 
    def get_context_data(self,**kwargs):
        context=super(Talleres, self).get_context_data(**kwargs)
        context['tall'] = Tallere.objects.all()
        context['contact_form'] =Formulario()
        context['datos'] = DatosContacto.objects.all()
        context['pro'] = Proyecto.objects.all()

        return context 


class Infotalleres(DetailView):
    template_name = 'app/infoproyectos.html'
    model = Tallere

    def get_context_data(self,**kwargs):
        context=super(Infotalleres, self).get_context_data(**kwargs)
        idpro = self.kwargs.get('pk',None)
        context['infop']= Tallere.objects.get(pk = idpro)
        context['tall'] = Tallere.objects.all()



        idtal = self.kwargs.get('pk',None)
        context['infot']= Tallere.objects.get(pk = idtal)
        context['tall'] = Tallere.objects.all()
        context['destacados']= EntradaBlog.objects.filter(destacados = True)[:4]
        context['contact_form'] =Formulario()
        context['pro'] = Proyecto.objects.all()
        context['template']= 'app:infotalleres'
        context['idTemp'] = idtal
        return context



class Contacto(TemplateView):
    template_name = 'app/formulario.html'
  

    def get_context_data(self,**kwargs):
        context=super(Contacto, self).get_context_data(**kwargs)
        context['contact_form'] =Formulario()
        context['pro'] = Proyecto.objects.all()
        return context

    def post(self, request,*args,**kwargs):
        nombre = request.POST.get('nombre')
        mensaje = request.POST.get('mensaje')
        email = request.POST.get('email')


        body= render_to_string(
            'app/email_content.html', {
                'nombre':nombre,
                'mensaje':mensaje,
                'email':email,
            },
        )

        print(nombre)

        email_message = EmailMessage(
            subject='mensaje de usuario',
            body=body,
            from_email=email,
            to=['koko-yoana@hotmail.es'],
        )
        email_message.content_subtype='html'
        email_message.send()
        return redirect('app:inicio')

class Blog(ListView):
    model =  EntradaBlog
    template_name = 'app/blog.html'
    paginate_by = 4
    context_object_name= 'blog' 
    queryset = EntradaBlog.objects.all()

    def get_context_data(self,**kwargs):
        context=super(Blog, self).get_context_data(**kwargs)
        context['destacados']= EntradaBlog.objects.filter(destacados = True)[:4]
        context['contact_form'] =Formulario()
        context['pro'] = Proyecto.objects.all()
        context['template']= 'app:blog'  
        return context       

class InfoBlog(DetailView):
    template_name = 'app/infoBlog.html'
    model =  EntradaBlog

    def get_context_data(self, **kwargs):
        context = super(InfoBlog, self).get_context_data(**kwargs)
        idblog = self.kwargs.get('pk',None)
        context['info'] = EntradaBlog.objects.get(pk = idblog)
        context['contact_form'] =Formulario()
        context['pro'] = Proyecto.objects.all()
        context['template']= 'app:infoblog'
        context['idTemp'] = idblog
        return context

class Datos(ListView):
    model = DatosContacto
    template_name = 'app/estatutos.html'
    context_object_name= 'datos' 
    queryset =DatosContacto.objects.all()[0]


    def get_context_data(self,**kwargs):
        context=super(Datos, self).get_context_data(**kwargs)
        context['contact_form'] =Formulario()
        context['datos'] = DatosContacto.objects.all()
        context['pro'] = Proyecto.objects.all()
        return context


class Datosd(ListView):
    model = DatosContacto
    template_name = 'app/legal.html'
    context_object_name= 'datos' 
    queryset =DatosContacto.objects.all()


    def get_context_data(self,**kwargs):
        context=super(Datosd, self).get_context_data(**kwargs)
        context['contact_form'] =Formulario()
        context['datos'] = DatosContacto.objects.all()
        context['pro'] = Proyecto.objects.all()
        return context


class Filo(ListView):
    model = DatosContacto
    template_name = 'app/filosofia.html'
    context_object_name= 'filo' 
    queryset =Filosofia.objects.all()


    def get_context_data(self,**kwargs):
        context=super(Filo, self).get_context_data(**kwargs)
        context['contact_form'] =Formulario()
        context['datos'] = DatosContacto.objects.all()
        context['pro'] = Proyecto.objects.all()
        return context




 











    
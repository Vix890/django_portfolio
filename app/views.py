from collections import defaultdict
from django.shortcuts import redirect, render
from app.forms import *
from app.models import *
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login

# ! vista de inicio
def home_view(request):
    
    habilidades = Habilidad.objects.all()
    
    page = request.GET.get('page')
    paginator = Paginator(habilidades, 3)
    
    if page == None:
        page = 1
        request.session["pagina"] = page
    else:
        request.session["pagina"] = page

    if "pagina" in request.session:
        page = request.session["pagina"]

    try:
        habilidades = paginator.get_page(page)
    except PageNotAnInteger:
        habilidades = paginator.page(1)
    except EmptyPage:
        habilidades = paginator.page(paginator.num_pages)
    
    context = {
        'habilidades': habilidades
    }
        
    return render(request, 'home.html', context=context)

# ! vista de información personal
def info_view(request):
    
    nombre = 'Víctor'
    ap1 = 'Domínguez'
    ap2 = 'Fernández'
    fecha_nacimiento = '20/09/2002'
    edad = '21'
    telefono = '666666666'
    email = 'victordominguez@centroculturalsalmantino.com'
    ciudad = 'Madrid'
    provincia = 'Madrid'
    pais = 'España'
    
    datos = {
        'nombre': nombre,
        'ap1': ap1,
        'ap2': ap2,
        'fecha_nacimiento': fecha_nacimiento,
        'edad': edad,
        'telefono': telefono,
        'email': email,
        'ciudad': ciudad,
        'provincia': provincia,
        'pais': pais,
    }
    
    context = {
        'datos': datos,
    }
    
    return render(request, 'info.html', context=context)

# ! vista de registro
class register_view(CreateView):
    
    template_name = 'register.html'
    
    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
        
        else:
            context = {
                'form': form,
            }
            
            return render(request, self.template_name, context=context)
                
        return redirect('home')

# ! vista de estudios
def estudios_view(request):
    estudios = Estudio.objects.order_by('fecha_inicio')
    estudios_por_anyo = defaultdict(list)
    anyo_actual = estudios[0].fecha_inicio.year if estudios else None

    for estudio in estudios:
        if estudio.fecha_inicio.year != anyo_actual:
            anyo_actual = estudio.fecha_inicio.year

        estudios_por_anyo[anyo_actual].append(estudio)

    paginators = {anyo: Paginator(estudios, 6 if anyo == 2022 else 8) for anyo, estudios in estudios_por_anyo.items()}
    page_number = request.GET.get('page')
    page_objs = {anyo: paginator.get_page(page_number) for anyo, paginator in paginators.items()}

    context = {
        'estudios_por_anyo': page_objs,
    }

    return render(request, 'estudios.html', context=context)


# ! vista de experiencias
def experiences_view(request):
    experiences = Experiencia.objects.all().filter(borrado=False)
    
    page = request.GET.get('page')
    paginator = Paginator(experiences, 3)
    
    if page == None:
        page = 1
        request.session["pagina"] = page
    else:
        request.session["pagina"] = page

    if "pagina" in request.session:
        page = request.session["pagina"]

    try:
        experiences = paginator.get_page(page)
    except PageNotAnInteger:
        experiences = paginator.page(1)
    except EmptyPage:
        experiences = paginator.page(paginator.num_pages)

    context = {
        'experiencias': experiences
    }

    return render(request, 'experiencias.html', context=context)

# ! vista de detalles de experiencia
def experience_details_view(request, pk):
    experiences = Experiencia.objects.get(pk=pk)

    context = {
        'experiencia': experiences
    }
    
    return render(request, 'experience_details.html', context=context)

# ! vista de borrar experiencia
def experience_delete_view(request, pk):
    experience = Experiencia.objects.get(pk=pk)
    
    experience.borrado = True
    experience.save()
    
    return redirect('experiencias')

# ! restaurar experiencias
def experience_restore_view(request):
    experiences = Experiencia.objects.all().filter(borrado=True)
    
    for experience in experiences:
        experience.borrado = False
        experience.save()
    
    return redirect('experiencias')

# ! vista de editar experiencia
class ExperienceEditView(UpdateView):
    
    template_name = 'experience_submit.html'
    
    def get(self, request, pk):
        experience = Experiencia.objects.get(pk=pk)
        form = ExperienceForm(instance=experience)
        
        context = {
                'form': form,
                'pk': pk,
            }
        
        return render(request, self.template_name, context=context)
    
    def post(self, request, pk):
        experience = Experiencia.objects.get(pk=pk)
        form = ExperienceForm(request.POST, instance=experience)
        
        if form.is_valid():
            form.save()
        else:
            context = {
                'form': form,
                'error': form.errors,
                'pk': pk,
            }
            return render(request, self.template_name, context=context)
                
        return redirect('experiencias')
    
# ! vista de crear experiencia
class ExperienceCreateView(CreateView):
    
    template_name = 'experience_submit.html'
    
    def get(self, request):
        form = ExperienceForm()
        
        context = {
                'form': form,
            }
        
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        form = ExperienceForm(request.POST)
        
        if form.is_valid():
            form.save()
            print('Valid')       
        else:
            context = {
                'form': form,
                'error': form.errors,
            }
            print(form.errors)
            return render(request, self.template_name, context=context)
                
        return redirect('experiencias')
    
def seguidores_view(request):
    
    seguidores = Seguidor.objects.filter(borrado=False, seguidor__startswith='A').order_by('-seguidor')    
    
    page = request.GET.get('page')
    paginator = Paginator(seguidores, 2)
    
    if page == None:
        page = 1
        request.session["pagina"] = page
    else:
        request.session["pagina"] = page

    if "pagina" in request.session:
        page = request.session["pagina"]

    try:
        seguidores = paginator.get_page(page)
    except PageNotAnInteger:
        seguidores = paginator.page(1)
    except EmptyPage:
        seguidores = paginator.page(paginator.num_pages)
    
    context = {
        'seguidores': seguidores
    }
        
    return render(request, 'seguidores.html', context=context)

# ! vista de borrar seguidor
def seguidor_delete_view(request, pk):
    
    usuario = request.user
    
    crear_notificacion('ha eliminado un seguidor', usuario)
    
    seguidor = Seguidor.objects.get(pk=pk)
    
    seguidor.borrado = True
    seguidor.save()
    
    return redirect('seguidores')

# ! restaurar seguidores
def seguidor_restore_view(request):
    
    usuario = request.user
    
    crear_notificacion('Se han restaurado los seguidores', usuario)
    
    seguidores = Seguidor.objects.all().filter(borrado=True)
    
    for seguidor in seguidores:
        seguidor.borrado = False
        seguidor.save()
    
    return redirect('seguidores')

# ! vista de detalles de seguidor
def seguidor_details_view(request, pk):
    
    usuario = request.user
    
    crear_notificacion('Se ha visto en detalle un seguidor', usuario)
    
    seguidor = Seguidor.objects.get(pk=pk)
    
    context = {
        'seguidor': seguidor
    }
    
    return render(request, 'seguidor_details.html', context=context)

# ! vista de editar seguidor
class SeguidorEditView(UpdateView):
    
    template_name = 'seguidores_submit.html'

    def get(self, request, pk):
        usuario = request.user
        
        crear_notificacion('Se ha ido a editar un seguidor', usuario)
        seguidor = Seguidor.objects.get(pk=pk)
        form = SeguidorForm(instance=seguidor)

        context = {
                'form': form,
                'pk': pk,
            }

        return render(request, self.template_name, context=context)
    
    def post(self, request, pk):
        seguidor = Seguidor.objects.get(pk=pk)
        form = SeguidorForm(request.POST, instance=seguidor)
        
        if form.is_valid():
            form.save()
        else:
            context = {
                'form': form,
                'error': form.errors,
                'pk': pk,
            }
            return render(request, self.template_name, context=context)
                
        return redirect('seguidores')

# ! vista de crear seguidor
class SeguidorCreateView(CreateView):
    
    
    template_name = 'seguidores_submit.html'
    
    def get(self, request):
        usuario = request.user
        
        crear_notificacion('Se ha ido a crear un seguidor', usuario)
        form = SeguidorForm()
        
        context = {
                'form': form,
            }
        
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        form = SeguidorForm(request.POST)
        
        if form.is_valid():
            form.save()
            print('Valid')       
        else:
            context = {
                'form': form,
                'error': form.errors,
            }
            print(form.errors)
            return render(request, self.template_name, context=context)
                
        return redirect('seguidores')

# ! vista de seguidos
def seguidos_view(request):
        
    seguidos = Seguidos.objects.filter(borrado=False).exclude(seguido__startswith='A').order_by('seguido')    
    
    page = request.GET.get('page')
    paginator = Paginator(seguidos, 2)
    
    if page == None:
        page = 1
        request.session["pagina"] = page
    else:
        request.session["pagina"] = page

    if "pagina" in request.session:
        page = request.session["pagina"]

    try:
        seguidos = paginator.get_page(page)
    except PageNotAnInteger:
        seguidos = paginator.page(1)
    except EmptyPage:
        seguidos = paginator.page(paginator.num_pages)
    
    context = {
        'seguidos': seguidos
    }
        
    return render(request, 'seguidos.html', context=context)

# ! vista de detalles de seguido
def seguido_details_view(request, pk):
    
    usuario = request.user
    
    crear_notificacion('Se ha visto en detalle un seguido', usuario)
    
    seguido = Seguidos.objects.get(pk=pk)
    
    context = {
        'seguido': seguido
    }
    
    return render(request, 'seguido_details.html', context=context)

# ! vista de borrar seguido
def seguido_delete_view(request, pk):
    
    usuario = request.user
    
    crear_notificacion('Se ha eliminado un seguido', usuario)
    
    seguido = Seguidos.objects.get(pk=pk)
    
    seguido.borrado = True
    seguido.save()
    
    return redirect('seguidos')

# ! restaurar seguidos
def seguidos_restore_view(request):
    
    usuario = request.user
    
    crear_notificacion('Se han restaurado los seguidos', usuario)
    
    seguidos = Seguidos.objects.all().filter(borrado=True)
    
    for seguido in seguidos:
        seguido.borrado = False
        seguido.save()
    
    return redirect('seguidos')

# ! vista de editar seguido
class SeguidoEditView(UpdateView):
    
    
    template_name = 'seguidos_submit.html'
    
    def get(self, request, pk):
        usuario = request.user
        
        crear_notificacion('Se ha ido a editar un seguido', usuario)
        seguido = Seguidos.objects.get(pk=pk)
        form = SeguidosForm(instance=seguido)
        
        context = {
                'form': form,
                'pk': pk,
            }
        
        return render(request, self.template_name, context=context)

    def post(self, request, pk):
        seguido = Seguidos.objects.get(pk=pk)
        form = SeguidosForm(request.POST, instance=seguido)
        
        if form.is_valid():
            form.save()
        else:
            context = {
                'form': form,
                'error': form.errors,
                'pk': pk,
            }
            return render(request, self.template_name, context=context)
                
        return redirect('seguidos')
    
# ! vista de crear seguido
class SeguidoCreateView(CreateView):
    
    
    template_name = 'seguidos_submit.html'
    
    def get(self, request):
        usuario = request.user
        
        crear_notificacion('Se ha ido a crear un seguido', usuario)
        form = SeguidosForm()
        
        context = {
                'form': form,
            }
        
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        form = SeguidosForm(request.POST)
        
        if form.is_valid():
            form.save()
            print('Valid')       
        else:
            context = {
                'form': form,
                'error': form.errors,
            }
            print(form.errors)
            return render(request, self.template_name, context=context)
                
        return redirect('seguidos')

# ! vista de notificaciones
def notificaciones_view(request):
    
    notificaciones = Notificacion.objects.all().filter(borrado=False).order_by('fecha')
    
    page = request.GET.get('page')
    paginator = Paginator(notificaciones, 10)
    
    if page == None:
        page = 1
        request.session["pagina"] = page
    else:
        request.session["pagina"] = page

    if "pagina" in request.session:
        page = request.session["pagina"]

    try:
        notificaciones = paginator.get_page(page)
    except PageNotAnInteger:
        notificaciones = paginator.page(1)
    except EmptyPage:
        notificaciones = paginator.page(paginator.num_pages)
    
    context = {
        'notificaciones': notificaciones
    }
    
    return render(request, 'notificaciones.html', context=context)

# ! vista de borrar notificaciones
def notificacion_delete_view(request, pk):
    
    notificacion = Notificacion.objects.get(pk=pk)
    
    notificacion.borrado = True
    notificacion.save()
    
    return redirect('notificaciones')

# ! restaurar notificaciones
def notificaciones_restore_view(request):
        
    notificaciones = Notificacion.objects.all()
    
    for notificacion in notificaciones:
        notificacion.borrado = False
        notificacion.save()
    
    return redirect('notificaciones')

# ! crear las notificaciones
def crear_notificacion(mensaje, usuario):
    notificacion = Notificacion.objects.create(
        notificacion = f'{usuario.username}: - {mensaje}',
        fecha = datetime.now(),
    )
    print(f'{usuario.username}: - {mensaje}')
    notificacion.save()
    
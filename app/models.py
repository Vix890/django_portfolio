from django.db import models
from django.conf import settings
from django.utils import timezone
from app.middleware import get_current_user

# ! Modelo base para campos comunes
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_creations', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='%(class)s_updates', on_delete=models.CASCADE)
    borrado = models.BooleanField(default=False)

    class Meta:
        abstract = True

# ! Modelo de HAHBILIDADES
class Habilidad(BaseModel):
    
    nombre_habilidad = models.CharField('Nombre', max_length=50)
    comentario = models.CharField('Descripcion', max_length=255)

    def __str__(self):
        return self.nombre_habilidad

    def __unicode__(self):
        return 
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            if not self.pk:
                self.created_by = user
            else:
                self.updated_by = user
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        

# ! Modelo de ESTUDIOS
class Estudio(BaseModel):
    
    titulacion = models.CharField('Nombre', max_length=50)
    nota_media = models.CharField('Nota media', max_length=255)
    fecha_inicio = models.DateField('Fecha de inicio')
    fecha_fin = models.DateField('Fecha de fin')

    def __str__(self):
        return self.titulacion

    def __unicode__(self):
        return 
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            if not self.pk:
                self.created_by = user
            else:
                self.updated_by = user
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Estudio"
        verbose_name_plural = "Estudios"

# ! Modelo de CATEGORIAS
class Categoria(BaseModel):
    nombre_categoria = models.CharField('Puesto de Trabajo',max_length=30,null=True, blank=True)
    descripcion_categoria = models.CharField('Descripcion', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Categoria' #puede ser otro nombre
        verbose_name_plural = 'Categorias'
        ordering = ['nombre_categoria']
        
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            if not self.pk:
                self.created_by = user
            else:
                self.updated_by = user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_categoria

# ! Modelo de EXPERIENCIAS
class Experiencia(BaseModel):
    empresa = models.CharField('Empresa',max_length=50,null=True, blank=True)
    fecha_inicio= models.DateField('Fecha de Inicio',null=True, blank=True)
    fecha_fin = models.DateField('Fecha de Finalización', null=True, blank=True)
    observaciones = models.CharField('Funciones', max_length=50, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, related_name='expe_categoria', null=True, blank=True, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            if not self.pk:
                self.created_by = user
            else:
                self.updated_by = user
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.empresa
    
    class Meta:
        verbose_name = 'Experiencia' #puede ser otro nombre
        verbose_name_plural = 'Experiencias'
        ordering = ['empresa']
        

# ! modelo de SEGUIDORES
class Seguidor(BaseModel):
    seguidor = models.CharField('Seguidor',max_length=50,null=True, blank=True)
    
    def __str__(self):
        return self.seguidor
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            if not self.pk:
                self.created_by = user
            else:
                self.updated_by = user
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Seguidor' #puede ser otro nombre
        verbose_name_plural = 'Seguidores'
        ordering = ['seguidor']

# ! Modelo de SEGUIDOS
class Seguidos(BaseModel):
    seguido = models.CharField('Seguidos',max_length=50,null=True, blank=True)
    
    def __str__(self):
        return self.seguidos
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            if not self.pk:
                self.created_by = user
            else:
                self.updated_by = user
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Seguidos' #puede ser otro nombre
        verbose_name_plural = 'Seguidos'
        ordering = ['seguido']
        

# ! modelo de NOTIFICACIONES
class Notificacion(BaseModel):
    notificacion = models.CharField('Notificacion',max_length=100,null=True, blank=True)
    fecha = models.DateField('Fecha',null=True, blank=True)
    
    def __str__(self):
        return self.notificacion
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            if not self.pk:
                self.created_by = user
            else:
                self.updated_by = user
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Notificacion' #puede ser otro nombre
        verbose_name_plural = 'Notificaciones'
        ordering = ['notificacion']
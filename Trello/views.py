
from .serializer import TableroSerializer, ComentarioSerializer, TareaSerializer, EtiquetaSerializer, UserSerializer
from .models import  Tablero, Comentario, Tarea, Etiqueta, User
from rest_framework import viewsets



class TableroViewSet(viewsets.ModelViewSet):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializer

class ComentarioViewSet(viewsets.ModelViewSet): 
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class EtiquetaViewSet(viewsets.ModelViewSet):    
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    


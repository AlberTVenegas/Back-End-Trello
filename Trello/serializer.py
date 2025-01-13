from rest_framework import serializers
from .models import   Tablero, Comentario, Tarea, Etiqueta



        
class TableroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablero
        fields = '__all__'
        
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__' 

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'

        

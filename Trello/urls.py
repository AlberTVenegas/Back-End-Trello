from django.urls import path, include
from rest_framework import routers
from Trello import views
router = routers.DefaultRouter()


router.register(r'tableros', views.TableroViewSet)
router.register(r'comentarios', views.ComentarioViewSet)
router.register(r'tareas', views.TareaViewSet)
router.register(r'etiquetas', views.EtiquetaViewSet)
# Wire up our API using automatic URL routing.

urlpatterns = [
    path('/api/v1/', include(router.urls)),
]

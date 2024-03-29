from rest_framework import routers

from apis.views import ToDoListViewSet

router = routers.DefaultRouter()

router.register("todo", ToDoListViewSet)

urlpatterns = router.urls

from django.urls import path, include
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter
# define the router

router = DefaultRouter()
router.register(r'student', StudentViewSet, basename = 'student')

urlpatterns = router.urls
    # path('student-list/', StudentViewSet.as_view({'get': 'list'})),
    # path('student-create/', StudentViewSet.as_view({'post': 'create'})),
    # path('student-detail/', StudentViewSet.as_view({'get': 'retrieve'})),
       

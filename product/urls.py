from django.urls import path, include

from product import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register('view', views.ProductViewSet, basename='user')
urlpatterns = [
    path('',views.Snippet_List.as_view(),name='index'),
    path('<pk>',views.SnippetDetail.as_view()),
    path('',include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
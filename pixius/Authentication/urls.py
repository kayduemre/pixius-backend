from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Authentication.views import ObtainTokenPairView, Token, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
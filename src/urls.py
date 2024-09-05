from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from payments.views import PaymentsView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from users.views import RegisterUserView, LoginUserView, ProfileView
from payments.views import PaymentCreateView

router = SimpleRouter()

router.register('payments', PaymentsView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/jwt/register/', RegisterUserView.as_view(), name="register"),
    path('api/auth/jwt/login/', LoginUserView.as_view(), name="login"),
    path('api/profile/', ProfileView.as_view(), name='user-profile'),
    path('api/pay/', PaymentCreateView.as_view(), name='payment_create')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

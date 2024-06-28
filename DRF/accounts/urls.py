from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework import routers


app_name = 'accounts'

urlpatterns = [
    path('register',views.UserRegisterView.as_view(),name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register('user',views.UserViewSet)
urlpatterns += router.urls

  #  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODI3OTc2NiwiaWF0IjoxNzE4MTkzMzY2LCJqdGkiOiJiOGY4OGZlODgyZTQ0OThiOWU0ZDQ0YzgxZWEyZDU5OCIsInVzZXJfaWQiOjF9.R2EdqLvpHiOxZaYnTHKYymLewMVcn02_kquB7A21QLs",
  #  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MTkzNjY2LCJpYXQiOjE3MTgxOTMzNjYsImp0aSI6IjMyZWUxMDQyYWVkNTQ5MzY5ZjdmM2IxYTQ0YzAxNmNkIiwidXNlcl9pZCI6MX0.obh4jgIXKJQSrIWELFfam1uTmYFhTduDd1gWugGJVhI"

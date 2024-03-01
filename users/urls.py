from . import views
from django.urls import path


urlpatterns = [
    path("register/", views.SignUpAPIView.as_view(), name="register"),
    path("login/", views.SignInAPIView.as_view(), name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path("verify/", views.VerifyAPIView.as_view(), name="verify"),
    path("get-new-code/", views.GetNewVerification.as_view(), name="get-new-code"),
    path("reset-password/", views.ResetPasswordAPIView.as_view(), name="reset-password"),
    path("reset-password-verify/", views.ResetPasswordVerifyAPIView.as_view(), name="reset-password-verify"),
    path('reset-password-confirm/', views.ResetPasswordConfirmAPIView.as_view(), name='reset-password-complete'),
    path("profile/", views.UserProfileRetrieveAPIView.as_view(), name="profile"),
    path('phone-user/', views.PhoneRetrieveAPIView.as_view(), name='phone-user'),
    path('change-password/', views.ChangePasswordAPIView.as_view(), name='change-password'),
    
]


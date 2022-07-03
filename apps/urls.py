from django.urls import path

from apps.views import IndexPage, SignUpPage, SignInPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('sign-in', SignInPage.as_view(), name='sign_in'),
    path('sign-up', SignUpPage.as_view(), name='sign_up')
]

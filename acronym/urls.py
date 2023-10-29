from django.urls import path

from . import views

urlpatterns = [
    path("signup", views.user_signup, name="signup"),
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("", views.index, name="index"),
    path("<str:name>/", views.acronyms_detail, name="acronyms_detail"),
    path("add", views.add_acronym, name="add_acronym"),
    # path("update/<str:name>/", views.update_acronym, name="update_acronym"),
    path("update", views.update_acronym, name="update_acronym"),
    path("delete/<str:name>/", views.delete_acronym, name="delete_acronym"),
    path("suggestions", views.get_suggestions, name="get_suggestions")
]
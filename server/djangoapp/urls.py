# Uncomment the imports before you add the code
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='registration', view=views.registration, name='register'),
    path(route='get_cars', view=views.get_cars, name ='getcars'),
    path('dealerships/', views.get_dealerships, name='dealerships'),

    # path for dealer reviews view
    path('dealer_reviews/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),

    # path for dealer details view
    path('dealer_details/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),

    # path for add a review view
    path('add_review/', views.add_review, name='add_review'),
    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

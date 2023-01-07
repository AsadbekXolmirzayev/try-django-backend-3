from django.urls import path
from .views import recipe_list, recipe_detail

app_name = 'recipes'

urlpatterns = [
    path('list/', recipe_list, name='list'),
    path('detail/<slug:slug>/', recipe_detail, name='detail')

]
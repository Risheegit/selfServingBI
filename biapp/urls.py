from django.urls import path
from .views import index, display_results

urlpatterns = [
    path('', index, name='index'),
    path('results/', display_results, name='results'),
    # path('filter-data/', filter_data, name='filter_data'),
    # path('store-form-data/', store_form_data, name='store_form_data'),
]

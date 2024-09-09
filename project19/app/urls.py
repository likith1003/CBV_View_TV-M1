from django.urls import path
from .views import *
urlpatterns = [
    path('fbv_string', fbv_string, name='fbv_string'),
    path('Cbv_String', Cbv_String.as_view(), name='Cbv_String'),
    path('insert_school_by_fbv', insert_school_by_fbv, name='insert_school_by_fbv'),
    path('insert_school_by_cbv', insert_school_by_cbv.as_view(), name='insert_school_by_cbv'), 
    path('TV', TV.as_view(), name='TV')
]

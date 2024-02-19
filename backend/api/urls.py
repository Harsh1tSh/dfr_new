from django.urls import path
from .views import index, import_students_from_excel, json_response_view
# here we map our view to the api endpoint
# what view will respond to a particular request or endpoint

urlpatterns = [
    path('',index, name="Index"),
    path('impot_data/', import_students_from_excel, name="Import Data"),
    path('return-json-response/', json_response_view, name="Json response"),
]


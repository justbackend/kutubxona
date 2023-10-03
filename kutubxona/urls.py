
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('muallif/', muallif),
    path('talaba/', talaba),
    path('all_books/', all_books),
    path('names_with_a/',names_with_a),
    path('records/', records),
    path('alive_writers/', alive_writers),
    path('<int:id>/', show_number),
    path('talaba/<int:talaba_id>/', delete_student),
    path('talabalar/', qidirish),
    path('muallif/<int:muallifning_idisi>/', delete_muallif),
    path('records/<int:record_id>/', delete_records),
    path('adminka/', adminn),
    path('talaba_edit/<int:pk>/', talaba_update),
    path('kitob/<int:pk>/', kitob),
    path('adminka/<int:pk>/', admin_edit),
    path('muallif_edit/<int:pk>/', muallif_edit),
    path('record_edit/<int:pk>/', record_edit),
    path('login/', login_view),
    path("logout/", logout_view),

]

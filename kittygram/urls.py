from django.urls import path

from cats.views import cat_list, hello, APICatCR, APICatRUD

urlpatterns = [
    path('cats/', cat_list),
    path('cats2/<int:id>/', APICatRUD.as_view()),
    path('cats2/', APICatCR.as_view()),
    path('', hello),
]

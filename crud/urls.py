from django.urls import path
from .views import DeleteProdutoView, IndexView , CreateProdutoView, UpdateProdutoView

urlpatterns = [
    path( '' , IndexView.as_view() , name='index') ,
    path('novoproduto/' , CreateProdutoView.as_view() , name='novoproduto'),
    path('alterarproduto/<int:pk>' , UpdateProdutoView.as_view() , name='alterarproduto' ) ,
    path('deletarproduto/<int:pk>' , DeleteProdutoView.as_view() , name='deletarproduto' ) ,
]
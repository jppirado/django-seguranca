
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import  CreateView, UpdateView, DeleteView 


from .models import Produto


# Create your views here.

class IndexView(LoginRequiredMixin , ListView):
    models = Produto
    template_name = 'index.html'
    paginate_by = 3
    ordering = 'id' 
    queryset = Produto.objects.all()
    

class CreateProdutoView(LoginRequiredMixin, CreateView):
    model= Produto
    template_name = 'produto_form.html'
    fields = ['nome' , 'preco' , 'descricao' , 'icon']
    success_url = reverse_lazy('index')

class UpdateProdutoView( LoginRequiredMixin , UpdateView):
    model = Produto 
    template_name = 'produto_form.html'
    fields = ['nome' , 'preco' , 'descricao' , 'icon']
    success_url = reverse_lazy('index')

class DeleteProdutoView( LoginRequiredMixin, DeleteView):
    model = Produto 
    template_name=  'produto_del.html'
    success_url = reverse_lazy('index')
from django.db import models
from stdimage.models import StdImageField
# Create your models here.


class Produto( models.Model ):
    nome = models.CharField('Nome' ,max_length=100)
    preco = models.DecimalField('Preço' , max_digits=8, decimal_places=2 )
    descricao = models.TextField('Descricao', max_length=10000 , null=True)
    icon =  StdImageField('Imagem' , upload_to="icon",  variations={'thumb':(124,124)} , null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

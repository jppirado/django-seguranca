from django.db import models

# Create your models here.


class Produto( models.Model ):
    nome = models.CharField('Nome' ,max_length=100)
    preco = models.DecimalField('Preço' , max_digits=8, decimal_places=2 )

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

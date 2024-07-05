from django.db import models

from .modelo import Modelo
from .cor import Cor
from .categoria import Categoria
from .marca import Marca
from .acessorio import Acessorio


class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos", null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos", null=True, blank=True)
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    acessorios = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name="veiculos", null=True, blank=True)

    def __str__(self):
        return f"{self.modelo} {self.ano} {self.cor}"

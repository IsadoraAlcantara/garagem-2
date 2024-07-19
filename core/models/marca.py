from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.nacionalidade:
            return f"{self.nome.upper()} {self.nacionalidade} - ({self.id})"
        else: 
            return f"{self.nome.upper()} ({self.id})"

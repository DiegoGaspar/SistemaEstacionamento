from django.db import models
import math
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)


    def __str__(self):
       return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()

    def __str__(self):
       return self.marca.nome + '-' + self.placa


class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits= 5, decimal_places=2)       
    valor_mes = models.DecimalField(max_digits= 6, decimal_places=2)       

    def __str__(self):
       return 'Parametros Gerais'

class MovRotativo(models.Model):
    entrada = models.DateTimeField(auto_now=False)
    saida = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits= 5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def horaTotal(self):
        return math.ceil((self.saida - self.entrada).total_seconds()/3600)

    def total(self):
        return self.valor_hora * self.horaTotal()

    def __str__(self):
        return self.veiculo.placa

class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits= 6, decimal_places=2)

    def __str__(self):
        return str(self.veiculo) + '-' + str(self.inicio)

class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)      

    def __str__(self):
        return str(self.mensalista) + '-' + str(self.total)  


from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls import reverse_lazy
from djmoney.models.fields import MoneyField
from moneyed.classes import BRL, FKP
from django.conf import settings
from PIL import Image
import os


class Tag(models.Model):
    tag = models.CharField(max_length=100, verbose_name='Tag')

    def __str__(self):
        return self.tag


class Categoria(models.Model):
    categoria = models.CharField(max_length=100, verbose_name='Categoria')

    def __str__(self):
        return self.categoria


class Produto(models.Model):
    nome_produto = models.CharField(
        max_length=255, unique=True, verbose_name='Nome do Produto')

    preco_real = MoneyField(
        max_digits=10, decimal_places=2, default_currency=BRL, verbose_name='Preço Real')
    preco_promocional = MoneyField(default=0,
                                   max_digits=10, decimal_places=2, default_currency=BRL, verbose_name='Preço Promocional')
    imagem_produto = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True,
                                       null=True, verbose_name='Imagem produto')

    descricao_curta = models.TextField(
        max_length=100, verbose_name='Descrição curta')
    descricao_media = models.TextField(
        max_length=255, verbose_name='Descrição media')
    descricao_longa = models.TextField(verbose_name='Descrição longa')

    peso = models.TextField(verbose_name='Peso')
    dimensões = models.TextField(verbose_name='Dimensões')
    tamanho = models.TextField(verbose_name='Tamanho')
    marca = models.TextField(verbose_name='Marca')
    tipo = models.TextField(verbose_name='Tipo')
    substancia = models.TextField(verbose_name='Substância ativa')
    uso = models.TextField(verbose_name='Uso')
    efeitos = models.TextField(verbose_name='Efeitos colaterais')
    estoque = models.IntegerField('estoque atual')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Tag')
    categoria = models.ManyToManyField(Categoria, verbose_name='Categoria')

    def __str__(self):
        return self.nome_produto

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem_produto:
            self.resize_image(self.imagem_produto.name, 650, 650)

    @staticmethod
    def resize_image(img_name, new_width, new_height):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size

        if width <= new_width:
            img.close()
            return

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(
            img_path,
            optimize=True,
            quality=60
        )
        new_img.close()

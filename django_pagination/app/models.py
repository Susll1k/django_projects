from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    class Genre(models.TextChoices):
        DRAMA = 'dr', 'Drama'
        ROMANCE = 'rm', 'Romance'
        MYSTERY = 'my', 'Mystery'
        HORROR = 'hr', 'Horror'
        HISTERY = 'hs', 'Histery'
        Science = 'sc', 'Science'

    title= models.CharField(max_length=100, verbose_name='Название')
    discription= models.TextField(verbose_name='Описание')
    author= models.CharField(max_length=100, verbose_name='Автор')
    published_year= models.IntegerField(verbose_name='Год выпуска', validators=[MaxValueValidator(2024), MinValueValidator(1700)])
    price= models.DecimalField(max_digits=7, decimal_places=1, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    genre = models.CharField(max_length=2, choices=Genre, verbose_name='Жанр')
    
    # def __str__(self):
    #     return f'{self.title}({self.author} - {self.published_year})'
    class Meta:
        verbose_name='Книга'
        verbose_name_plural='Книги'

    


# coding=utf-8
from django.db import models

# Create your models here.

class script(models.Model):

    script_name = models.CharField('Название программы', max_length= 40, unique = True, db_index = True, primary_key = True)
    script = models.TextField('Текст программы')

    def __str__(self):

        return self.script_name





"""""""""
IntegerField - Целое число
TextField - Поле для большого текста
DataTimeField - Поле дата-время
URLField - Поле для URL-адреса, максимум 200 символов 
FileField - Поле загружаемого файла
"""""""""
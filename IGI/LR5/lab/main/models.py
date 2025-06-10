from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta


class Vacationss(models.Model):
    name = models.CharField()
    title = models.CharField()
    money = models.IntegerField()


class QaA(models.Model):
    quation = models.CharField()
    answer = models.CharField()    


phone_regex = RegexValidator(
    regex=r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$',
    message="Формат: +375 (29) XXX-XX-XX"
)


class NativeCountry(models.Model):
    name=models.CharField()

    class Meta:
        verbose_name = 'Страна обитания'        


class Profile(models.Model):
    user=models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    age=models.DateField(null=False, blank=False)
    phone_regex = RegexValidator(
        regex=r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$',
        message="Формат: +375 (29) XXX-XX-XX"
    )
    phone_number = models.CharField(max_length=19, validators=[phone_regex])
    
    def __str__(self):
        return str(self.user.username)


class Staf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$',
        message="Формат: +375 (29) XXX-XX-XX"
    )
    phone_number = models.CharField(max_length=19, validators=[phone_regex])
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    animal = models.CharField()
    image = models.ImageField('animal.jpg', null=True, blank=True)
    def __str__(self):
        return (
            f"{self.user.get_full_name()}" 
            if self.user.first_name or self.user.last_name 
            else self.user.username
        )
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Animal(models.Model):
    species = models.CharField('Имя вида')
    number = models.SmallIntegerField('Количество особей')
    house = models.CharField('Номер вальера', default='Вальер')
    image = models.ImageField('animal.jpg', blank=True, default='lions.jpg')


    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'         


class Reviews(models.Model):
    review = models.TextField('Отзыв')
    mark = models.SmallIntegerField('Оценка', default=5)

    def __str__(self):
        return self.review

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'    


class News(models.Model):
    title = models.CharField('Название')
    anons = models.CharField('Анонс')
    full_text = models.TextField('Статья')
    image = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Sales(models.Model):
    title = models.CharField('Название')
    sale = models.SmallIntegerField('%')
    time = models.DateField('dd.mm.yyyy')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.utils.datetime_safe import datetime
from news.models import User
from django.dispatch import receiver


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    objects = None
    STATUS = [
        (0, 'Trong kho'),
        (1, "Đang mượn"),
        (2, 'Đã thanh lý'),
    ]
    SOURCE = [
        (0, 'Cấp phát'),
        (1, 'Mua'),
    ]
    CLASSIFY = [
        (0, 'Tự nhiên'),
        (1, 'Xã hội'),
    ]

    special_number = models.CharField(max_length=14, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=45, null=True, blank=True)
    company = models.CharField(max_length=45, null=True, blank=True)
    publishing_year = models.PositiveIntegerField(validators=[MinValueValidator(1900),
                                                              MaxValueValidator(datetime.now().year)])
    price = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True)
    subject_type = models.CharField(max_length=10, null=True, blank=True)
    general_number = models.CharField(max_length=10, null=True, blank=True)
    language = models.CharField(max_length=45, default='Tiếng Việt')
    source = models.IntegerField(choices=SOURCE, default=1)
    classify = models.IntegerField(choices=CLASSIFY, default=1)
    invoice_number = models.CharField(max_length=20, null=True, blank=True)
    date_entry = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    objects = None
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    borrowed_book = models.ForeignKey(Books, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=1)


@receiver(post_save, sender=Borrow, dispatch_uid='change_status_book')
def change_status_book(instance, created, **kwargs):
    if created:
        # b = Books.objects.get(id=instance.borrowed_book.id)
        b = instance.borrowed_book
        b.status = 1
    else:
        if instance.status == 1:
            b = instance.borrowed_book
            b.status = 1
        else:
            b = instance.borrowed_book
            b.status = 0
    return b.save()


@receiver(post_delete, sender=Borrow, dispatch_uid="change_status_book_on_delete_borrower")
def change_status_book_on_delete_borrower(instance, **kwargs):
    b = instance.borrowed_book
    b.status = 0
    b.save()

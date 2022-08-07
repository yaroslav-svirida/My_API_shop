from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models

# Create your models here.
from rest_framework.reverse import reverse


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        basket = Basket.objects.create(user=user)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        response = self._create_user(email, password, **extra_fields)

        # send_mail(subject="Account Approved",
        #           message="Hello we are TeachMeSkill Infocigans and we are "
        #                   "approved your account",
        #           from_email=DEFAULT_FROM_EMAIL,
        #           recipient_list=[email])
        return response

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=30, blank=True, default="")
    last_name = models.CharField(max_length=100, blank=True, default="")
    phone = models.EmailField(blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(blank=False, default=False)
    delete_at = models.DateTimeField(null=True, default=None)
    # user_products = models.ManyToManyField(to='myshop.Product',
    #                                        null=True, blank=True,
    #                                        related_name='selected_products')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Catalog(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Brends(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Collections(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Colors(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SocketsCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    article = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    catalog_name = models.ForeignKey(Catalog, on_delete=models.CASCADE, blank=True, null=True)
    brend_name = models.ForeignKey(Brends, on_delete=models.PROTECT, blank=True, null=True)
    collection_name = models.ForeignKey(Collections, on_delete=models.PROTECT, blank=True, null=True)
    colors_name = models.ForeignKey(Colors, on_delete=models.PROTECT, blank=True, null=True)
    socket_category_name = models.ForeignKey(SocketsCategory, on_delete=models.PROTECT, blank=True, null=True)
    to_basket = models.BooleanField(default=False, blank=True, null=True)
    amount_for_basket = models.IntegerField(default=0, blank=True, null=True)

    # def __str__(self):
    #     return f'{self.article} {self.name}'


class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    # order = models.IntegerField(default=1, blank=True, null=True)
    # products_to_basket = models.ManyToManyField(to='myshop.Product',
    #                                             null=True, blank=True,
    #                                             related_name='selected_products')


class ProductInBasket(models.Model):
    basket_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_article = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', blank=True, null=True)
    product_amount = models.IntegerField(blank=True, null=True, default=0)


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order_product = models.ManyToManyField(to='myshop.Product',
                                           null=True, blank=True,
                                           related_name='order_products')

    cost_price = models.IntegerField(blank=True, null=True)
    full_price = models.IntegerField(blank=True, null=True)
    profit = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def get_products(self):
        return "\n".join([p.name for p in self.order_product.all()])

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

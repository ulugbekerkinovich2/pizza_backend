from django.db import models
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):

        if not username:
            raise ValueError(_('Iltimos, foydalanuvchi nomini kiriting'))

        # username_validator = UnicodeUsernameValidator(min_length=5)
        # username_validator(username)
        # if len(username) < 5:
        #     raise ValueError(_('Ism 5 ta belgidan kam bo\'lmasligi kerak'))
        # if len(password) < 8:
        #     raise ValueError(_('Parol 8 ta belgidan kam bo\'lmasligi kerak'))
        if password:
            user = self.model(username=username, **extra_fields)
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, username, **extra_fields):

        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username=username, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Name'), max_length=50, unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


def __str__(self):
    return f'{self.username}'


class LogoName(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'logo_name'


class Home(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'home'
        verbose_name_plural = 'home'


class ContactLocation(models.Model):
    phone_number = models.CharField(max_length=20, null=True)
    description = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'contact_location'
        verbose_name_plural = 'contact_location'


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'about'
        verbose_name_plural = 'about'


class AboutProduct(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'about_product'
        verbose_name_plural = 'about_product'


class AboutPricing(models.Model):
    title = models.TextField()
    name = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'about_pricing'
        verbose_name_plural = 'about_pricing'


class ProductType(models.Model):
    name = models.CharField(max_length=512, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    cost = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.product_name


class Blog(models.Model):
    blog_images = models.ImageField(upload_to='blog_images/')

    class Meta:
        db_table = 'blog'
        verbose_name_plural = 'blog'

    def __str__(self):
        return str(self.blog_images)


class Award(models.Model):
    product_branches = models.IntegerField()
    number_of_awards = models.IntegerField()
    happy_customers = models.IntegerField()
    staff = models.IntegerField()

    def __str__(self):
        return str(self.number_of_awards)


class SecondBlog(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'second_blog'
        verbose_name_plural = 'second_blog'


class AboutProductDetail(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'about_product_detail'
        verbose_name_plural = 'about_product_detail'


class Form(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    message = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'form'
        verbose_name_plural = 'form'

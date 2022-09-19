from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name: 'category'
        verbose_name_plural: 'categories'


class PostModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    post_view = models.IntegerField(default=0)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class BannerModel(models.Model):
    title = models.TextField()
    button_text = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='banner/')
    post_url = models.URLField()


    def __str__(self):
        return f"{self.button_text}"

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

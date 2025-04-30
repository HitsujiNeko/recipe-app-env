from django.db import models

class Ingredient(models.Model):
    TYPE_CHOICES = [
        ('肉・魚・大豆・卵', '肉・魚・大豆・卵'),
        ('野菜', '野菜'),
        ('米・麺・パスタ', '米・麺・パスタ'),
        ('その他', 'その他'),
    ]
    name = models.CharField(max_length=100, unique=True, help_text="食材名を入力してください")  # 食材名
    reading = models.CharField(max_length=100, help_text="食材の読み方を入力してください")  # 読み方
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, help_text="食材の種類を選択してください")  # 種類

    def __str__(self):
        return self.name

# Generated by Django 5.2 on 2025-04-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="thumbnail",
            field=models.URLField(
                blank=True,
                help_text="画像URLを入力してください（入力無しの場合、サムネイル画像",
                null=True,
            ),
        ),
    ]

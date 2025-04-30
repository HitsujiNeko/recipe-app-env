import logging
import re
from .models import Recipe

logger = logging.getLogger('django')

# レシピ追加機能
def extract_youtube_thumbnail(url):
    """
    YouTubeのURLからサムネイル画像のURLを生成する関数。
    """
    logger.debug(f"Extracting thumbnail from URL: {url}")
    # 標準形式と短縮形式の両方に対応する正規表現
    video_id_match = re.search(r'(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})', url)
    if video_id_match:
        video_id = video_id_match.group(1)
        thumbnail_url = f'https://img.youtube.com/vi/{video_id}/sddefault.jpg'
        logger.debug(f"Generated thumbnail URL: {thumbnail_url}")
        return thumbnail_url
    logger.warning("Failed to extract video ID from URL.")
    return None

# レシピ提案機能
def filter_recipes_by_criteria(selected_ingredients, selected_category):
    """
    指定された食材とカテゴリに基づいてレシピをフィルタリングする関数。
    """
    recipes = Recipe.objects.all()

    if selected_ingredients:
        for ingredient_id in selected_ingredients:
            recipes = recipes.filter(ingredients__id=ingredient_id)

    if selected_category:
        recipes = recipes.filter(categories__id=selected_category)

    return recipes
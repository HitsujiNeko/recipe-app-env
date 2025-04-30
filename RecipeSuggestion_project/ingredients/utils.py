from ingredients.models import Ingredient

def add_sample_ingredients():
    sample_ingredients = [
        {"name": "にんじん", "reading": "にんじん", "type": "野菜"},
        {"name": "じゃがいも", "reading": "じゃがいも", "type": "野菜"},
        {"name": "オクラ", "reading": "おくら", "type": "野菜"},
        {"name": "玉ねぎ", "reading": "たまねぎ", "type": "野菜"},
        {"name": "カボチャ", "reading": "かぼちゃ", "type": "野菜"},
        {"name": "鶏ささみ", "reading": "とりささみ", "type": "肉・魚・大豆・卵"},
        {"name": "レタス", "reading": "れたす", "type": "野菜"},
        {"name": "もめん豆腐", "reading": "もめんとうふ", "type": "肉・魚・大豆・卵"},
        {"name": "絹豆腐", "reading": "きぬとうふ", "type": "肉・魚・大豆・卵"},
        {"name": "レタス", "reading": "れたす", "type": "野菜"},
        {"name": "トマト缶", "reading": "とまとかん", "type": "野菜"},
        {"name": "きゅうり", "reading": "きゅうり", "type": "野菜"},
        {"name": "トマト", "reading": "とまと", "type": "野菜"},
        {"name": "ピーマン", "reading": "ぴーまん", "type": "野菜"},
        {"name": "なす", "reading": "なす", "type": "野菜"},
        {"name": "ほうれん草", "reading": "ほうれんそう", "type": "野菜"},
        {"name": "小松菜", "reading": "こまつな", "type": "野菜"},
        {"name": "白菜", "reading": "はくさい", "type": "野菜"},
        {"name": "大根", "reading": "だいこん", "type": "野菜"},
        {"name": "ごぼう", "reading": "ごぼう", "type": "野菜"},
        {"name": "しいたけ", "reading": "しいたけ", "type": "野菜"},
        {"name": "しめじ", "reading": "しめじ", "type": "野菜"},
        {"name": "えのき", "reading": "えのき", "type": "野菜"},
        {"name": "米粉", "reading": "こめこ", "type": "米・麺・パスタ"},
        {"name": "米", "reading": "こめ", "type": "米・麺・パスタ"},
        {"name": "うどん", "reading": "うどん", "type": "米・麺・パスタ"},
        {"name": "そば", "reading": "そば", "type": "米・麺・パスタ"},
        {"name": "パスタ", "reading": "ぱすた", "type": "米・麺・パスタ"},
        {"name": "パン", "reading": "ぱん", "type": "米・麺・パスタ"},
        {"name": "チーズ", "reading": "ちーず", "type": "その他"},
        {"name": "牛乳", "reading": "ぎゅうにゅう", "type": "その他"},
    ]

    for ingredient in sample_ingredients:
        Ingredient.objects.get_or_create(
            name=ingredient["name"],
            reading=ingredient["reading"],
            type=ingredient["type"]
        )

    print("Sample ingredients added successfully!")
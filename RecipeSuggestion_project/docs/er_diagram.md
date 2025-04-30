## テーブルの説明

### 食材テーブル (`ingredients`)

- **id**: 主キー
- **name**: 食材名
- **reading**: 読み方
- **type**: 種類　選択肢からチョイス

### レシピテーブル (`recipes`)

- **id**: 主キー
- **name**: レシピ名
- **url**: YouTube の URL
- **thumbnail**: サムネイル画像 URL
- **notes**: 備考
- **created_at** : 作成日時
- **updated_at**: 更新日時

### レシピ-食材中間テーブル (`recipe_ingredients`)

- **id**: 主キー
- **recipe_id**: レシピ ID（外部キー）
- **ingredient_id**: 食材 ID（外部キー）

### カテゴリテーブル (`categories`)

- **id**: 主キー
- **name**: カテゴリ名 　以下から選択する
  （例: パン・麺類、スープ・汁物・カレー、主菜、副菜、お菓子・デザート）

### レシピ-カテゴリ中間テーブル (`recipe_categories`)

- **id**: 主キー
- **recipe_id**: レシピ ID（外部キー）
- **category_id**: カテゴリ ID（外部キー）

## E-R 図作成用コード db.diagram.io

Table ingredients {
id int [pk] // 主キー
name varchar(100) [unique, not null] // 食材名
reading varchar(100) [not null] // 読み方
type varchar(50) [not null] // 種類
}

Table recipes {
id int [pk] // 主キー
name varchar(100) [unique, not null] // レシピ名
url varchar(255) [unique, not null] // YouTube の URL
thumbnail varchar(255) [not null] // サムネイル画像 URL
notes text // 備考
created_at datetime [not null] // 作成日時
updated_at datetime [not null] // 更新日時
}

Table categories {
id int [pk] // 主キー
name varchar(50) [not null] // カテゴリ名
}

Table recipe_ingredients {
id int [pk] // 主キー
recipe_id int [not null, ref: > recipes.id] // レシピ ID（外部キー）
ingredient_id int [not null, ref: > ingredients.id] // 食材 ID（外部キー）
}

Table recipe_categories {
id int [pk] // 主キー
recipe_id int [not null, ref: > recipes.id] // レシピ ID（外部キー）
category_id int [not null, ref: > categories.id] // カテゴリ ID（外部キー）
}

Ref: recipe_ingredients.recipe_id > recipes.id
Ref: recipe_ingredients.ingredient_id > ingredients.id
Ref: recipe_categories.recipe_id > recipes.id
Ref: recipe_categories.category_id > categories.id

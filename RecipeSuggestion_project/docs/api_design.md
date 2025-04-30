# API 設計

## 概要

このアプリケーションで提供される API の設計を以下に示します。

## エンドポイント一覧

### 食材管理

- **GET /api/ingredients**  
  食材一覧を取得。

  - レスポンス:
    ```json
    [
      { "id": 1, "name": "鶏むね肉", "reading": "とりむねにく", "type": "肉" },
      { "id": 2, "name": "にんじん", "reading": "にんじん", "type": "野菜" }
    ]
    ```

- **POST /api/ingredients**  
  新しい食材を追加。
  - リクエストボディ:
    ```json
    { "name": "鶏むね肉", "reading": "とりむねにく", "type": "肉" }
    ```

### レシピ管理

- **GET /api/recipes**  
  レシピ一覧を取得。

  - クエリパラメータ:
    - `ingredients`: 食材 ID の配列（例: `?ingredients=1,2`）
    - `category`: カテゴリ ID（例: `?category=1`）
  - レスポンス:
    ```json
    [
      {
        "id": 1,
        "name": "鶏むね肉の照り焼き",
        "url": "https://youtube.com/example",
        "thumbnail": "https://img.youtube.com/example.jpg",
        "notes": "簡単なレシピです"
      }
    ]
    ```

- **POST /api/recipes**  
  新しいレシピを追加。
  - リクエストボディ:
    ```json
    {
      "name": "鶏むね肉の照り焼き",
      "url": "https://youtube.com/example",
      "thumbnail": "https://img.youtube.com/example.jpg",
      "notes": "簡単なレシピです",
      "ingredients": [1, 2],
      "categories": [1]
    }
    ```

### カテゴリ管理

- **GET /api/categories**  
  カテゴリ一覧を取得。
  - レスポンス:
    ```json
    [
      { "id": 1, "name": "主菜" },
      { "id": 2, "name": "副菜" }
    ]
    ```

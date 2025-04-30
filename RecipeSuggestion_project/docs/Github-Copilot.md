# プロジェクトテンプレート

## 概要

この文書の内容を把握したうえで、文書の一番下に記載する指示の内容を読んで
指示に従って行動してください

---

## プロジェクト構成

- **プロジェクト名**: [レシピ提案アプリ開発]
- **機能**: [同ディレクトリ(docs)の requirements.md に記載]

---

## 環境設定

Anaconda(Python3)

- **Python バージョン**: 3.12.7
- **開発環境**: Docker
- **ライブラリ**:
  environment.yml に記述　 Conda のデフォルトで入っているライブラリもある

- **データベース**: SQLite （現状）後に変更予定

---

## ディレクトリ構造

```
RecipeSuggestion_project

[プロジェクトルート]
├── manage.py
├── db.sqlite3
├── ingredients/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   ├── __pycache__/
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
├── media/
├── recipes/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   ├── __pycache__/
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
├── RecipeSuggestion_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── static/
├── templates/
│   ├── add_recipe.html
│   └── recipes_list.html
└── docs/
    ├── api_design.md
    ├── E-R.png
    ├── er_diagram.md
    ├── layout_proposal.md
    ├── requirements.md
    └── template.md
```

---

## 気を付けること

・urls.py や views.py,settings.py の対応関係を把握してファイルの編集を行うこと　
プロジェクト
/workspaces/python-env/django/RecipeSuggestion_project/recipes/urls.py
/workspaces/python-env/django/RecipeSuggestion_project/RecipeSuggestion_project/settings.py

レシピ
/workspaces/python-env/django/RecipeSuggestion_project/recipes/urls.py
/workspaces/python-env/django/RecipeSuggestion_project/recipes/views.py

・debug ログも参照する

##　進捗
必要最低限の機能をすべて実装完了
ここからは、デザインや、ユーザの扱いやすさ向上をメインに取り組む

## 指示

現状、レシピ追加機能およびレシピ提案機能、レシピ詳細ページの更新機能では
/workspaces/recipe-app-env/RecipeSuggestion_project/static/js/ingredient_search.js
を使用しており、食材の検索機能に扱いづらい点が課題です。
Choices.js の使用を検討しております。食材モデル
/workspaces/recipe-app-env/RecipeSuggestion_project/ingredients/models.py
では、読み方 reading を指定しており、reading と name を用いて検索を行いたいです。
Choices.js でこの検索条件に基づいて食材の検索、選択機能を設定してください。
また、スクリプトは URL で読み込み、Choices.js をレシピ追加機能およびレシピ提案機能、レシピ詳細ページの更新機能に適用し、/workspaces/recipe-app-env/RecipeSuggestion_project/static/js/ingredient_search.js を削除してください。またテンプレートファイルの編集を行い、不要な箇所を削除してください。

##　今後の予定
Django アプリをポートフォリオとして使用するには、以下の手順を実行することで、プロジェクトを魅力的かつプロフェッショナルに見せることができます。

---

### **1. プロジェクトの完成度を高める**

- **機能の完成度**:

  - すべての主要機能（レシピ提案、追加、削除、更新）が正常に動作することを確認します。
  - ユーザーインターフェースが直感的で使いやすいか確認します。

- **デザインの改善**:

  - Bootstrap や CSS を活用して、見た目を洗練させます。
  - レスポンシブデザインを適用し、モバイルデバイスでも見やすくします。

- **エラーハンドリング**:
  - ユーザーが誤った操作をした場合に適切なエラーメッセージを表示するようにします。

---

### **2. コードの品質を向上させる**

- **リファクタリング**:

  - 冗長なコードを削除し、再利用可能なコードをモジュール化します。
  - views.py や`utils.py`の関数を整理して、可読性を向上させます。

- **テストの追加**:

  - 単体テストや統合テストを作成し、アプリの信頼性を高めます。
  - 例: tests.py にレシピ追加や削除のテストを追加。

- **ドキュメントの整備**:
  - `README.md`を作成し、プロジェクトの概要、機能、セットアップ手順を記載します。
  - API 設計や ER 図などのドキュメントを整理し、GitHub リポジトリに含めます。

---

### **3. デプロイ**

- **デプロイ先の選定**:

  - **無料オプション**: [Render](https://render.com/), [Railway](https://railway.app/), [PythonAnywhere](https://www.pythonanywhere.com/)
  - **有料オプション**: AWS, Heroku, Azure, GCP

- **デプロイ手順**:
  1. **静的ファイルの収集**:
     ```bash
     python manage.py collectstatic
     ```
  2. **環境変数の設定**:
     - `.env`ファイルを使用して、`SECRET_KEY`やデータベース接続情報を管理します。
  3. **データベースの移行**:
     ```bash
     python manage.py migrate
     ```
  4. **Gunicorn や Nginx の設定**:
     - 本番環境でアプリを動作させるために設定します。

---

### **4. GitHub リポジトリの整備**

- **リポジトリの公開**:

  - コードを GitHub にアップロードし、ポートフォリオとして共有します。
  - .gitignore を確認し、不要なファイル（`db.sqlite3`や`__pycache__`など）が含まれないようにします。

- **README.md の記載例**:

  ````markdown
  # レシピ提案アプリ

  このアプリは、選択した食材やカテゴリに基づいてレシピを提案する Django アプリです。

  ## 主な機能

  - レシピ提案機能
  - レシピ追加・更新・削除機能
  - 食材検索機能

  ## 使用技術

  - Django
  - Bootstrap
  - SQLite

  ## セットアップ手順

  1. リポジトリをクローンします。
     ```bash
     git clone https://github.com/username/repository.git
     ```
  ````

  2. 必要なパッケージをインストールします。
     ```bash
     pip install -r requirements.txt
     ```
  3. サーバーを起動します。
     ```bash
     python manage.py runserver
     ```

  ```

  ```

---

### **5. ポートフォリオとしての見せ方**

- **デモサイトのリンク**:

  - デプロイしたアプリの URL を README や LinkedIn に記載します。

- **スクリーンショットや動画**:

  - アプリの主要機能を示すスクリーンショットや操作動画を用意します。

- **ブログや記事の執筆**:
  - アプリ開発の背景や技術的な課題を解決した方法をブログにまとめ、共有します。

---

これらの手順を実行することで、プロジェクトを魅力的なポートフォリオとして活用できます。---

### **5. ポートフォリオとしての見せ方**

- **デモサイトのリンク**:

  - デプロイしたアプリの URL を README や LinkedIn に記載します。

- **スクリーンショットや動画**:

  - アプリの主要機能を示すスクリーンショットや操作動画を用意します。

- **ブログや記事の執筆**:
  - アプリ開発の背景や技術的な課題を解決した方法をブログにまとめ、共有します。

---

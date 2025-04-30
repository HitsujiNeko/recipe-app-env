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

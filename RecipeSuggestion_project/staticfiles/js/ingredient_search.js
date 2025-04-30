document.addEventListener("DOMContentLoaded", function () {
  function setupChoices(ingredientSelectId, categorySelectId) {
    const ingredientSelect = document.getElementById(ingredientSelectId);
    const categorySelect = document.getElementById(categorySelectId);

    if (ingredientSelect) {
      new Choices(ingredientSelect, {
        removeItemButton: true,
        searchPlaceholderValue: "食材を検索",
      });
    }

    if (categorySelect) {
      new Choices(categorySelect, {
        removeItemButton: true,
        searchPlaceholderValue: "カテゴリを検索",
      });
    }
  }

  setupChoices("ingredients", "category");
});

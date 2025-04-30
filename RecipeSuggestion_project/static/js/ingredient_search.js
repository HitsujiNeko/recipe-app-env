document.addEventListener("DOMContentLoaded", function () {
  function setupIngredientSearch(ingredientSelectId, searchBoxId) {
    const ingredientSelect = document.getElementById(ingredientSelectId);
    const searchBox = document.getElementById(searchBoxId);

    if (!ingredientSelect || !searchBox) return;

    searchBox.addEventListener("input", function () {
      const filter = searchBox.value;
      const options = ingredientSelect.options;

      for (let i = 0; i < options.length; i++) {
        const option = options[i];
        const text = option.textContent;
        const reading = option.getAttribute("data-reading") || "";
        option.style.display =
          text.includes(filter) || reading.includes(filter) ? "" : "none";
      }
    });
  }

  function setupSelectionDisplay(
    ingredientSelectId,
    selectedIngredientsDivId,
    categorySelectId,
    selectedCategoryDivId
  ) {
    const ingredientSelect = document.getElementById(ingredientSelectId);
    const selectedIngredientsDiv = document.getElementById(
      selectedIngredientsDivId
    );
    const categorySelect = document.getElementById(categorySelectId);
    const selectedCategoryDiv = document.getElementById(selectedCategoryDivId);

    if (ingredientSelect && selectedIngredientsDiv) {
      ingredientSelect.addEventListener("change", function () {
        const selectedOptions = Array.from(
          ingredientSelect.selectedOptions
        ).map((option) => option.textContent);
        selectedIngredientsDiv.textContent = `選択された食材: ${selectedOptions.join(
          ", "
        )}`;
      });
    }

    if (categorySelect && selectedCategoryDiv) {
      categorySelect.addEventListener("change", function () {
        const selectedOption =
          categorySelect.options[categorySelect.selectedIndex];
        selectedCategoryDiv.textContent = `選択されたカテゴリ: ${selectedOption.textContent}`;
      });
    }
  }

  setupIngredientSearch("ingredients", "ingredient-search");
  setupSelectionDisplay(
    "ingredients",
    "selected-ingredients",
    "category",
    "selected-category"
  );
});

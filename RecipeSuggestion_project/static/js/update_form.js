document.addEventListener("DOMContentLoaded", function () {
  const updateForm = document.querySelector(".update-recipe-form");

  updateForm.addEventListener("submit", function (event) {
    event.preventDefault(); // ページの再読み込みを防ぐ

    const formData = new FormData(updateForm);
    const url = updateForm.getAttribute("action") || window.location.href;

    fetch(url, {
      method: "POST",
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          alert("更新が成功しました！");
          location.reload(); // 必要に応じてページをリロード
        } else {
          const errorContainer = document.querySelector(".form-errors");
          errorContainer.innerHTML = ""; // エラーをクリア
          for (const [field, errors] of Object.entries(data.errors)) {
            const errorList = document.createElement("ul");
            errors.forEach((error) => {
              const listItem = document.createElement("li");
              listItem.textContent = error;
              errorList.appendChild(listItem);
            });
            errorContainer.appendChild(errorList);
          }
        }
      })
      .catch((error) => {
        console.error("エラーが発生しました:", error);
        alert("エラーが発生しました。コンソールを確認してください。");
      });
  });
});

$(document).ready(function () {
  $("#ingredients").select2({
    matcher: function (params, data) {
      if ($.trim(params.term) === "") {
        return data;
      }

      if (typeof data.text === "undefined") {
        return null;
      }

      // 検索文字列がnameまたはreadingに一致するか確認
      var searchTerm = params.term.toLowerCase();
      var text = data.text.toLowerCase();
      var subSearch = $(data.element).data("sub-search").toLowerCase();

      if (text.indexOf(searchTerm) > -1 || subSearch.indexOf(searchTerm) > -1) {
        return data;
      }

      return null;
    },
  });
});

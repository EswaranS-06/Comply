// REX theme toggle. Stored choice > OS preference > dark. The pre-paint snippet in <head> applies a stored choice.
(function () {
  var root = document.documentElement;
  var button = document.querySelector("[data-theme-toggle]");
  var media = window.matchMedia("(prefers-color-scheme: light)");

  function currentTheme() {
    var explicit = root.getAttribute("data-theme");
    if (explicit === "light" || explicit === "dark") return explicit;
    return media.matches ? "light" : "dark";
  }

  function syncUi() {
    var theme = currentTheme();
    var next = theme === "dark" ? "light" : "dark";
    if (button) {
      button.setAttribute("aria-label", "Switch to " + next + " theme");
      button.setAttribute("title", "Switch to " + next + " theme");
    }
    var bg = getComputedStyle(root).getPropertyValue("--theme-color").trim();
    document.querySelectorAll('meta[name="theme-color"]').forEach(function (m) {
      if (bg) m.setAttribute("content", bg);
    });
  }

  if (button) {
    button.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("rex-theme", next); } catch (e) {}
      syncUi();
    });
  }

  media.addEventListener("change", syncUi);
  syncUi();
})();

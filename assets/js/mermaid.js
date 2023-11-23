
$(document).ready(function () {
    var skin = "dark"
    var theme = {
      "air": "default",
      "aqua": "default",
      "contrast": "default",
      "dark": "dark",
      "default": "default",
      "dirt": "default",
      "mint": "mint",
      "neon": "dark",
      "plum": "dark",
      "sunrise": "default"
    }[skin]
    var config = {
      startOnLoad:true,
      theme: theme,
    }
    mermaid.initialize(config)
    window.mermaid.init(config, document.querySelectorAll('.language-mermaid'));
  });
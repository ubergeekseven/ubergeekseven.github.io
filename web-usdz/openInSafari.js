document.getElementById("foz").addEventListener("click", function(evt) {
    var a = document.createElement('a');
    a.setAttribute("href", this.getAttribute("data-href"));
    a.setAttribute("target", "_blank");

    var dispatch = document.createEvent("HTMLEvents");
    dispatch.initEvent("click", true, true);
    a.dispatchEvent(dispatch);
}, false);
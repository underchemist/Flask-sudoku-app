$(function() {
    var el = document.getElementById("clear-btn")
    if (el) {
            el.addEventListener("click", function() {
            for (i = 0; i < 82; i++) {
            var $inputBox = $('.def-txt-input[name="cell-input[' + (i) + ']"]');
                $inputBox.val("")
            }
        });
    }
});
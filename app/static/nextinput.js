$(function() {
    $(".def-txt-input").keyup (function () {
        var $this = $(this);
        if (this.value.length >= $(this).attr('maxlength')) {
            var curr_el_index = parseInt(this.name.split('[').pop().split(']').shift());
            var $inputBox = $('.def-txt-input[name="cell-input[' + (curr_el_index + 1) + ']"]');
            $inputBox.focus();
            $inputBox.val("");
        }
        // else if (this.value.length == 0 && $this.which == 8) {
        //     var curr_el_index = parseInt(this.name.split('[').pop().split(']').shift());
        //     var $inputBox = $('.def-txt-input[name="cell-input[' + (curr_el_index - 1) + ']"]');
        //     $inputBox.focus();
        //     $inputBox.val("");
        //}
    });
});
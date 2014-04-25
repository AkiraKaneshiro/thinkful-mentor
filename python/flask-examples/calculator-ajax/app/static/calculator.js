(function(N) {
    var $theForm;

    function handleFormSubmit() {
        var a = $theForm.find("input[name=a]").val();
        var b = $theForm.find("input[name=b]").val();
        var op = $theForm.find("input[name=op]:checked").val();
        console.log("a: " + a + "\nb: " + b + "\nop: " + op)
        $.ajax({
            url:"/calculate",
            data: {"a":a, "b":b, "op":op},
            success: handleResponse,
            error: handleError,
            method:"POST"
        })
        return false;
    }

    function handleResponse(data) {
        $("#error").hide();
        $("#answer").show();
        $("#answer-val").html(data);
    }

    function handleError(jqxhr, textstatus, errorthrown) {
        $("#error #msg").html(jqxhr.responseText);
        $("#error").show();
    }

    N.subtracterForm = function() {
        this.init = function(jqelem) {
            $theForm = jqelem;
            $theForm.on("submit", handleFormSubmit);
        };
    }

})(window);

$(document).ready(function() {
    subtracterForm = new subtracterForm();
    subtracterForm.init($("form#calculator"));
});
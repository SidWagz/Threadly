/* Javascript file for threadly project */

$(document).ready(function() {
    $("form[name='comment-form']").submit(function() {
        var message = $("input#input-box").val();
        var element = $("<li>");
        element.html(message);
        element.addClass("list-comment")
        $("ul#comments").prepend(element);
        return false;
    });
});

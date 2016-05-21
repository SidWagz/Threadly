/* Javascript file for threadly project */

$(document).ready(function() {
    $("form[name='comment-form']").submit(function() {
        var message = $("input#input-box").val().trim();

        if(!message)
            return false;

        $.post(
            $(this).attr('action'),
            $(this).serialize(),
            function (data) {
                if (data['user.name'])
                    message = message + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;->&nbsp;" + data['user.name'];
                var element = $("<li>");
                element.html(message);
                element.addClass("list-comment")
                $("ul#comments").prepend(element);
            }, 'json');

        return false;
    });
});

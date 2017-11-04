$(document).ready(function() {
    $('#logindiv form.auth-form').on('submit', function(e) {
        e.preventDefault();

        var actionUrl = $(this).attr('action');
        var p = $(this).find('p.message');
        var passInput = $(this).find('input[name="psw"]');
        var params = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: actionUrl,
            data: params,

            success: function(data) {
                if (!data) {
                    window.location.replace("/");
                } else {
                    $(passInput).val('');
                    $(p).html(data);
                }
            },

            failure: function() {
                alert('Error');
            }
        });
    });


    $('#registerdiv form input').on('change', function() {
        var form = $(this).closest("form");
        var params = form.serialize();

        $.ajax({
            type: 'POST',
            url: form.attr("data-validate-url"),
            data: params,

            success: function(data) {
                var data = JSON.parse(data);
                var p = $(form).find('p.message');

                $(p).html(data['message']);

                $(form).find('input').css('background-color', 'white');

                data.fields.forEach(function(field) {
                    var id = 'id_' + field;
                    var input = $(form).find('input#' + id);
                    input.css('background-color', 'rgba(255, 0, 0, 0.7)');
                });

            },

            failure: function() {
                alert('Error');
            }
        });
    });


    $('#registerdiv input').on('focus', function() {
        $(this).css('background-color', 'white');
    });
});
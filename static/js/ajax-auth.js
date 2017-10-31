function AuthAjax(e) {

}


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


    $('#registerdiv form.auth-form').on('submit', function(e) {
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
                    window.location.replace("/auth/activation/");
                } else {
                    $(p).html(data);
                }
            },

            failure: function() {
                alert('Error');
            }
        });
    });
});
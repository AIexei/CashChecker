function AuthAjax(e) {
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
                $(p).html(data);
            }
        },

        failure: function() {
            alert('Error');
        }
    });
}


$(document).ready(function() {
    $('#logindiv form.auth-form').on('submit', AuthAjax);
    $('#registerdiv form.auth-form').on('submit', AuthAjax);
});
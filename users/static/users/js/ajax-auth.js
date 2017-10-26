$(document).ready(function() {
    $('#logindiv form.auth-form').on('submit', function(e) {
        e.preventDefault();
        actionUrl = $(this).attr('action');
        params = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: actionUrl,
            data: params,

            success: function(data) {
                if (!data) {
                    window.location.replace("/");
                } else {
                    $('p.message').html(data);
                }
            },

            failure: function() {
                alert('Error');
            }
        });
    });
});
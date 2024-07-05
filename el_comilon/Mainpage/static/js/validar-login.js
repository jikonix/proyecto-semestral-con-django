$(document).ready(function() {
    $('#loginForm').on('submit', function(event) {
        event.preventDefault();
        var errores = [];

        var email = $('#email').val();
        if (!email || !isValidEmail(email)) {
            errores.push("Por favor, ingresa un correo electrónico válido.");
            $('#email').addClass('error-input');
        } else {
            $('#email').removeClass('error-input');
        }

        var password = $('#password').val();
        if (!password || !CaracterValid(password)) {
            errores.push("La contraseña debe contener un minimo de 8 caracteres, estructurado de una mayúscula, un número y un carácter especial.");
            $('#password').addClass('error-input');
        } else {
            $('#password').removeClass('error-input');
        }

        if (errores.length > 0) {
            var erroresHTML = '';
            errores.forEach(function(error) {
                erroresHTML += '<div class="alert alert-danger" role="alert">' + error + '</div>';
            });
            $('#errors-container').html(erroresHTML);
        } else {
            $('#errors-container').empty();
            alert("Inicio de sesión logrado con exitoso");
            limpiarFormulario();
            window.location.href = 'index.html';
        }
    });

    function limpiarFormulario() {
        $('#email').val('');
        $('#password').val('');
    }

    function ExistEmail(email) {
        var emailRegex = /\S+@\S+\.\S+/;
        return emailRegex.test(email);
    }
    
    function CaracterValid(password) {
        var passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{8,}$/;
        return passwordRegex.test(password);
    }
});
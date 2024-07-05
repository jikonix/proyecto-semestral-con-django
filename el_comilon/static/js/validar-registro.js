$(document).ready(function() {
    $('#registroForm').on('submit', function(event) {
        event.preventDefault();
        var errores = [];

        var nombre = $('#nombre').val();
        var apellidos = $('#apellidos').val();
        if (!nombre || !apellidos) {
            errores.push("Favor de ingresar su nombre y su apellido");
            $('#nombre').addClass('error-input');
            $('#apellidos').addClass('error-input');
        } else {
            $('#nombre').removeClass('error-input');
            $('#apellidos').removeClass('error-input');
        }

        var email = $('#email').val();
        if (!email || !isValidEmail(email)) {
            errores.push("El email no es valido, Por favor ingresar un correo valido y que contenga un dominio (.com, .hotmail, .outlook, etc) ");
            $('#email').addClass('error-input');
        } else {
            $('#email').removeClass('error-input');
        }

        var password = $('#password').val();
        if (!password || !isValidPassword(password)) {
            errores.push("La contraseña debe contener un minimo de 8 caracteres, estructurado de una mayúscula, un número y un carácter especial.");
            $('#password').addClass('error-input');
        } else {
            $('#password').removeClass('error-input');
        }

        var telefono = $('#telefono').val();
        if (!telefono || !isValidPhoneNumber(telefono)) {
            errores.push("Favor de ingresar un numero veridico y perteneciente al país");
            $('#telefono').addClass('error-input');
        } else {
            $('#telefono').removeClass('error-input');
        }

        if (errores.length > 0) {
            var erroresHTML = '';
            errores.forEach(function(error) {
                erroresHTML += '<div class="alert alert-danger" role="alert">' + error + '</div>';
            });
            $('#errors-container').html(erroresHTML);
        } else {
            $('#errors-container').empty();
            alert("Formulario archivado correctamente");
            limpiarFormulario();
        }
    });

    function limpiarFormulario() {
        $('#nombre').val('');
        $('#apellidos').val('');
        $('#email').val('');
        $('#password').val('');
        $('#telefono').val('');
        $('#direccion').val('');
        $('#departamento').val('');
    }

    function isValidEmail(email) {
        var emailRegex = /\S+@\S+\.\S+/;
        return emailRegex.test(email);
    }

    function isValidPhoneNumber(phoneNumber) {
        var phoneRegex = /^\d{9}$/;
        return phoneRegex.test(phoneNumber);
    }

    function isValidPassword(password) {
        var passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{8,}$/;
        return passwordRegex.test(password);
    }
    
});
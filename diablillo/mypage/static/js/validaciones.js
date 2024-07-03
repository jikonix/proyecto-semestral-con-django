const nombre = document.getElementById("name")
const user = document.getElementById("user")
const email = document.getElementById("email")
const pass = document.getElementById("password")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
    parrafo.innerHTML = ""
    if(nombre.value.length <2){
        warnings += `El nombre no es valido <br>`
        entrar = true
    }
    if(user.value.length <=4){
        warnings += `El nombre de usuario debe ser mayor a 4 digitos <br>`
        entrar = true
    }
    if(!regexEmail.test(email.value)){
        warnings += `El email no es valido, debe poner el dominio (.com, .hotmail, .outlook, etc)  <br>`
        entrar = true
    }
    if(pass.value.length < 8){
        warnings += `La contraseña debe ser mayor a 8 digitos <br>`
        entrar = true
    }

    if(entrar){
        parrafo.innerHTML = warnings
    }else{
        parrafo.innerHTML = "Enviado"
    }
})
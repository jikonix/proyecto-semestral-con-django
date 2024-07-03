const dire = document.getElementById("calle")
const num_dire = document.getElementById("numcalle")
const tele = document.getElementById("telefono")
const adicional = document.getElementById("indicaciones")
const parrafo = document.getElementById("warnings")
const form = document.getElementById("form")

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let vari1 = /^\d{3,6}$/
    parrafo.innerHTML = ""
    
    if(dire.value.length < 3 ){
        warnings += `La direccion no es valida <br>`
        entrar = true
    }
    
    if(!vari1.test(num_dire.value)){
        warnings += `El numero de vivienda no es valida <br>`
        entrar = true
    }
    
    if(tele.value.length == 9 ){
        warnings += `El numero telefonico no es valido <br>`
        entrar = true
    }

    if(adicional.value.length < 40 ){
        warnings += `Las indicaciones superan el maximo de 40 letras <br>`
        entrar = true
    }

    if(entrar){
        parrafo.innerHTML = warnings
    }else{
        parrafo.innerHTML = "Enviado"
    }
    
})
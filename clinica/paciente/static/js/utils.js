//metodo para obtener codigo en general. Este es obligatorio
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//metodos para obtener codigo de Equipo
function PasarValor(valor1, valor2, codigo, URL){
        let letra1 = document.getElementById(valor1).value.charAt(0);
        let letra2 = document.getElementById(valor2).value.charAt(0);
        console.log(letra1);
        console.log(letra2);
        ObtenerCodigo(letra1, letra2, codigo, URL)
}
function ObtenerCodigo(letra1, letra2, codigo, URL) {
    const csrftoken = getCookie('csrftoken');
    console.log('llego a obtener codigo');
    console.log(URL);
    if (letra1!="" &&  letra2!="" && letra2!="-") {
        let letras = letra1 + '' + letra2;
        let data ={
                    'csrfmiddlewaretoken':csrftoken,
                    'letras':letras,
                    };
        $.post(URL, data, function(response){ 
                document.getElementById(codigo).value = response
        });
    }
}

//metodos para obtener codigo de Equipo y Mantenimiento
function SelectPasarValorEquipo(valor1, valor2, valor3, codigo, URL) {

    var combo1 = document.getElementById(valor1);
    var selected1 = combo1.options[combo1.selectedIndex].text.charAt(0);
    var combo2 = document.getElementById(valor2);
    var selected2 = combo2.options[combo2.selectedIndex].text.charAt(0);
    var combo3 = document.getElementById(valor3);
    var selected3 = combo3.options[combo3.selectedIndex].text.charAt(0);

    if (combo1.value!=0 && combo2.value!=0 && combo3.value!=0) {

        ObtenerCodigoSelected(selected1, selected2, selected3, codigo, URL)   

    }
    
}
function ObtenerCodigoSelected(letra1, letra2, letra3, codigo, URL) {
    const csrftoken = getCookie('csrftoken');
    console.log('llego a obtener codigo select');
    if (letra1!="" &&  letra2!="" &&  letra3!="") {
        let letras = letra1 + letra2 + letra3;
        let data ={
                    'csrfmiddlewaretoken':csrftoken,
                    'letras':letras,
                    };
        console.log(URL)
        $.post(URL, data, function(response){ 
                document.getElementById(codigo).value = response
        });
    }
}

//metodos para obtener codigo de Equipo
function PasarValorBodega(valor1, valor2, codigo, URL){
    let letra1 = document.getElementById(valor1).value.charAt(0);
    var combo2 = document.getElementById(valor2);
    var letra2 = combo2.options[combo2.selectedIndex].text.charAt(0);
    
    console.log(letra1);
    console.log(letra2);
    ObtenerCodigo(letra1, letra2, codigo, URL)
}
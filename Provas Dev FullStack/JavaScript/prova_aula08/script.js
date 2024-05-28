function converter(unidade) {
    var metros = parseFloat(document.getElementById('metros').value);
    var resultado = 0;

    if (isNaN(metros) || metros < 0) {
        document.getElementById('resultado').innerText = 'Por favor, insira um valor válido em metros.';
        return;
    }

    switch (unidade) {
        case 'jarda':
            resultado = (metros * 1.09361).toFixed(3);
            break;
        case 'pe':
            resultado = (metros * 3.28084).toFixed(3);
            break;
        case 'polegada':
            resultado = (metros * 39.3701).toFixed(2);
            break;
        case 'milha':
            resultado = (metros * 0.000621371).toFixed(6);
            break;
        default:
            resultado = 0;
    }

    document.getElementById('resultado').innerText = 'Resultado: ' + resultado + ' ' + unidade + (unidade === 'milha' ? 's' : 's');
}

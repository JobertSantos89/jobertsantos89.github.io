let saldo = 1000;

function realizarOperacao() {
    const operacao = document.getElementById('operacao').value;
    const valorInput = document.getElementById('valor');
    const resultado = document.getElementById('resultado');
    let valor = parseFloat(valorInput.value);

    if (operacao !== 'saldo' && (isNaN(valor) || valor <= 0)) {
        resultado.textContent = 'Por favor, insira um valor válido.';
        resultado.style.color = 'red';
        return;
    }

    switch (operacao) {
        case 'saldo':
            resultado.textContent = `Seu saldo é R$ ${saldo.toFixed(2)}`;
            resultado.style.color = 'green';
            break;
        case 'sacar':
            if (valor > saldo) {
                resultado.textContent = 'Saldo insuficiente para realizar o saque.';
                resultado.style.color = 'red';
            } else {
                saldo -= valor;
                resultado.textContent = `Saque de R$ ${valor.toFixed(2)} realizado com sucesso. Seu novo saldo é R$ ${saldo.toFixed(2)}`;
                resultado.style.color = 'green';
            }
            break;
        case 'depositar':
            saldo += valor;
            resultado.textContent = `Depósito de R$ ${valor.toFixed(2)} realizado com sucesso. Seu novo saldo é R$ ${saldo.toFixed(2)}`;
            resultado.style.color = 'green';
            break;
        default:
            resultado.textContent = 'Operação inválida.';
            resultado.style.color = 'red';
    }

    valorInput.value = '';
}

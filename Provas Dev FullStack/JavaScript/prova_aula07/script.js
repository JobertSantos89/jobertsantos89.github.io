document.getElementById('calculateTip').addEventListener('click', () => {
    const totalAmount = parseFloat(document.getElementById('totalAmount').value);
    const serviceQuality = parseFloat(document.getElementById('serviceQuality').value);
    
    if (isNaN(totalAmount) || totalAmount <= 0) {
        alert('Por favor, insira um valor total válido.');
        return;
    }
    
    if (serviceQuality === 0) {
        alert('Por favor, selecione a qualidade do serviço.');
        return;
    }
    
    const calculateTip = (amount, quality, callback) => {
        const tip = amount * quality;
        callback(tip);
    };
    
    const displayTip = (tip) => {
        document.getElementById('tipAmount').innerText = `$${tip.toFixed(2)}`;
    };
    
    calculateTip(totalAmount, serviceQuality, displayTip);
});

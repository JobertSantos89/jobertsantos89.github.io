let packages = JSON.parse(localStorage.getItem('packages')) || [];

document.getElementById('registerPackage').addEventListener('click', function() {
    const packageId = document.getElementById('packageId').value;
    if (packageId === '') {
        alert('Por favor, insira o ID do pacote.');
        return;
    }

    const newPackage = {
        id: packageId,
        status: 'Em Trânsito',
        date: new Date().toISOString()
    };

    packages.push(newPackage);
    localStorage.setItem('packages', JSON.stringify(packages));

    addPackageToTable(newPackage);
    document.getElementById('packageId').value = '';
});

document.getElementById('checkStatus').addEventListener('click', function() {
    const packageId = document.getElementById('checkPackageId').value;
    const pkg = packages.find(p => p.id === packageId);

    if (pkg) {
        document.getElementById('statusMessage').textContent = `Status: ${pkg.status}`;
    } else {
        document.getElementById('statusMessage').textContent = 'Pacote não encontrado.';
    }
});

document.getElementById('updatePackage').addEventListener('click', function() {
    const packageId = document.getElementById('updatePackageId').value;
    const newStatus = document.getElementById('updateStatus').value;
    const pkg = packages.find(p => p.id === packageId);

    if (pkg) {
        pkg.status = newStatus;
        pkg.updateDate = new Date().toISOString();
        localStorage.setItem('packages', JSON.stringify(packages));
        updatePackageTable();
        document.getElementById('updatePackageId').value = '';
        document.getElementById('updateStatus').value = 'Em Trânsito';
    } else {
        alert('Pacote não encontrado.');
    }
});

function addPackageToTable(pkg) {
    const table = document.getElementById('packagesTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    const cellId = newRow.insertCell(0);
    const cellStatus = newRow.insertCell(1);
    const cellDate = newRow.insertCell(2);

    cellId.textContent = pkg.id;
    cellStatus.textContent = pkg.status;
    cellDate.textContent = new Date(pkg.date).toLocaleString();
}

function updatePackageTable() {
    const tableBody = document.getElementById('packagesTable').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = '';
    packages.forEach(pkg => addPackageToTable(pkg));
    calculateAverageDeliveryTime();
}

function loadPackages() {
    packages.forEach(pkg => addPackageToTable(pkg));
    calculateAverageDeliveryTime();
}

function calculateAverageDeliveryTime() {
    const deliveredPackages = packages.filter(p => p.status === 'Entregue');
    if (deliveredPackages.length === 0) {
        document.getElementById('averageDeliveryTime').textContent = 'Nenhum pacote entregue ainda.';
        return;
    }

    let totalDeliveryTime = 0;
    deliveredPackages.forEach(pkg => {
        const registrationDate = new Date(pkg.date);
        const deliveryDate = new Date(pkg.updateDate);
        totalDeliveryTime += (deliveryDate - registrationDate);
    });

    const averageDeliveryTime = totalDeliveryTime / deliveredPackages.length;
    const averageDays = Math.floor(averageDeliveryTime / (1000 * 60 * 60 * 24));
    document.getElementById('averageDeliveryTime').textContent = `Tempo médio de entrega: ${averageDays} dias`;
}

loadPackages();

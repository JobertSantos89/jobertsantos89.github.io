    document.getElementById('formularioNota').addEventListener('submit', function(event) {
        event.preventDefault(); // Impede o comportamento padrão do formulário
        var nota = document.getElementById('entradaNota').value.trim();
        if (nota) { // Verifica se a nota não está vazia
            var tbody = document.querySelector('#tabelaNotas tbody');
            var row = document.createElement('tr');

            var numCol = document.createElement('td');
            numCol.textContent = tbody.rows.length + 1; // Número da nota

            var notaCol = document.createElement('td');
            notaCol.textContent = nota;

            var actionsCol = document.createElement('td');
            var deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Excluir';
            deleteBtn.addEventListener('click', function() {
                row.remove(); // Remove a nota da tabela
            });
            actionsCol.appendChild(deleteBtn);

            row.appendChild(numCol);
            row.appendChild(notaCol);
            row.appendChild(actionsCol);

            tbody.appendChild(row); // Adiciona a nota à tabela

            document.getElementById('entradaNota').value = ''; // Limpa o campo de entrada
        }
    });

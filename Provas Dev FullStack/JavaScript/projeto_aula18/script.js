// Funções para Cadastro e Login de Usuários
function registerUser(username, password) {
    let users = JSON.parse(localStorage.getItem('users')) || [];
    users.push({ username, password });
    localStorage.setItem('users', JSON.stringify(users));
}

function loginUser(username, password) {
    let users = JSON.parse(localStorage.getItem('users')) || [];
    let user = users.find(u => u.username === username && u.password === password);
    if (user) {
        localStorage.setItem('loggedInUser', username);
        return true;
    }
    return false;
}

function login() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    if (loginUser(username, password)) {
        alert('Login successful!');
        window.location.href = 'index.html';
    } else {
        alert('Invalid username or password.');
    }

    return false; // Impede o envio do formulário
}

function registerPrompt() {
    let username = prompt('Enter a username:');
    let password = prompt('Enter a password:');
    registerUser(username, password);
    alert('Registration successful! You can now login.');
}

// Funções para Exibição de Produtos
function loadProducts() {
    fetch('https://fakestoreapi.com/products')
        .then(res => res.json())
        .then(products => {
            let productContainer = document.getElementById('product-list');
            productContainer.innerHTML = ''; // Limpa o container antes de adicionar novos produtos
            products.forEach(product => {
                let productElement = document.createElement('div');
                productElement.className = 'product-item';
                productElement.innerHTML = `
                    <h2>${product.title}</h2>
                    <img src="${product.image}" alt="${product.title}" />
                    <p>${product.description}</p>
                    <p>Price: $${product.price}</p>
                    <a href="product.html?id=${product.id}">View Details</a>
                    <button onclick="addToCart(${product.id})">Add to Cart</button>
                `;
                productContainer.appendChild(productElement);
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}

// Função para Exibir Detalhes de um Produto
function getProductDetails(productId) {
    fetch(`https://fakestoreapi.com/products/${productId}`)
        .then(res => res.json())
        .then(product => {
            document.getElementById('product-title').innerText = product.title;
            document.getElementById('product-image').src = product.image;
            document.getElementById('product-description').innerText = product.description;
            document.getElementById('product-price').innerText = `$${product.price}`;
            document.getElementById('add-to-cart').setAttribute('onclick', `addToCart(${product.id})`);
        })
        .catch(error => console.error('Error fetching product details:', error));
}

// Funções do Carrinho de Compras
function addToCart(productId) {
    fetch(`https://fakestoreapi.com/products/${productId}`)
        .then(res => res.json())
        .then(product => {
            let cart = JSON.parse(localStorage.getItem('cart')) || [];
            let existingProduct = cart.find(p => p.id === productId);

            if (existingProduct) {
                existingProduct.quantity += 1;
            } else {
                product.quantity = 1;
                cart.push(product);
            }

            localStorage.setItem('cart', JSON.stringify(cart));
            alert('Product added to cart!');
        })
        .catch(error => console.error('Error adding product to cart:', error));
}

function loadCart() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let cartSummary = document.getElementById('cart-summary');
    let cartItemsContainer = document.getElementById('cart-items');
    cartItemsContainer.innerHTML = ''; // Limpa o container antes de adicionar novos itens

    if (cart.length === 0) {
        cartItemsContainer.innerHTML = '<p>Your cart is empty.</p>';
        return;
    }

    let total = 0;
    cart.forEach(product => {
        let cartItem = document.createElement('div');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `
            <input type="checkbox" class="cart-item-checkbox" data-price="${product.price}" checked>
            <img src="${product.image}" alt="${product.title}">
            <div class="cart-item-info">
                <h2>${product.title}</h2>
                <p>Quantity: ${product.quantity}</p>
                <p>Price: $${product.price}</p>
                <p>Total: $${(product.price * product.quantity).toFixed(2)}</p>
            </div>
        `;
        cartItemsContainer.appendChild(cartItem);
        total += product.price * product.quantity;
    });

    updateTotal(total);

    // Atualiza o total ao clicar nos checkboxes
    document.querySelectorAll('.cart-item-checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', updateTotalOnCheck);
    });
}

function updateTotalOnCheck() {
    let total = 0;
    document.querySelectorAll('.cart-item-checkbox:checked').forEach(checkbox => {
        let price = parseFloat(checkbox.getAttribute('data-price'));
        let quantity = parseInt(checkbox.parentElement.querySelector('.cart-item-info p').innerText.split(': ')[1]);
        total += price * quantity;
    });
    updateTotal(total);
}

function updateTotal(total) {
    document.getElementById('cart-total').innerText = `Total: $${total.toFixed(2)}`;
}

window.onload = function() {
    loadCart();


    let totalElement = document.createElement('p');
    totalElement.innerText = `Total Price: $${total.toFixed(2)}`;
    cartSummary.appendChild(totalElement);
}

function finalizePurchase() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let orderDetails = {
        order_id: 'ORDER12345',
        user_email: 'user@example.com',
        items: cart,
        total_price: calculateTotalPrice(cart)
    };

    sendOrderConfirmation(orderDetails);

    localStorage.removeItem('cart');
    alert('Purchase completed! A confirmation has been sent to your email.');
    window.location.href = 'index.html';
}

function calculateTotalPrice(cart) {
    return cart.reduce((total, item) => total + (item.price * item.quantity), 0);
}

// Função para Enviar Notificação de Confirmação de Pedido (AfterShip)
function sendOrderConfirmation(orderDetails) {
    fetch('https://api.aftership.com/v4/notifications', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'aftership-api-key': 'YOUR_API_KEY'  // Substitua por sua chave de API real
        },
        body: JSON.stringify({
            order_id: orderDetails.order_id,
            email: orderDetails.user_email,
            tracking_info: {
                items: orderDetails.items,
                total_price: orderDetails.total_price
            }
        })
    }).then(response => response.json())
      .then(data => console.log('Order confirmation sent:', data))
      .catch(error => console.error('Error sending order confirmation:', error));
}

// Função para Verificar Autenticação
function checkAuthentication() {
    let loggedInUser = localStorage.getItem('loggedInUser');
    if (!loggedInUser) {
        alert('You must be logged in to access this page.');
        window.location.href = 'login.html'; // Redireciona para a página de login
    }
}

// Inicialização da Página de Produtos
if (document.title === 'Product Catalog') {
    loadProducts();
}

// Inicialização da Página de Detalhes do Produto
if (document.title === 'Product Details') {
    const urlParams = new URLSearchParams(window.location.search);
    const productId = urlParams.get('id');
    if (productId) {
        getProductDetails(productId);
    }
}

// Inicialização da Página do Carrinho
if (document.title === 'Your Cart') {
    loadCart();
    checkAuthentication();
}

// Inicialização da Página de Checkout
if (document.title === 'Checkout') {
    checkAuthentication();
}

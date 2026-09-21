/*Ejercicio práctico #2:
Crear un carrito de compras dinámico con productos de una API
Enunciado: Vas a crear un carrito de compras dinámico que permite agregar
productos al carrito utilizando datos obtenidos de una API externa. Los pasos
específicos son:
1. Utilizá fetch() para obtener una lista de productos desde una API (puede ser la
misma API de productos del Ejercicio 1).
2. Mostrá los productos en la página en forma de tarjetas o lista.
3. Agregá un botón &quot;Añadir al carrito&quot; para cada producto. Al hacer clic en el
botón, el producto debe añadirse al carrito.
4. Usá LocalStorage para almacenar los productos que se agreguen al carrito,
de manera que si recarga la página, los productos sigan allí.
5. Mostrá la cantidad de productos que hay en el carrito en todo momento,
actualizándose cada vez que se añada un nuevo producto. */

document.addEventListener('DOMContentLoaded', () => {
    fetchProd();
    actCart();
});

function fetchProd() {
    fetch('https://fakestoreapi.com/products')
    .then(res => res.json())
    .then(data => {
        let div = document.getElementById('prod');
        div.innerHTML = '';
        data.forEach(p => {
            div.innerHTML += `
                <div class="card">
                    <img src="${p.image}" width="80">
                    <h3>${p.title}</h3>
                    <p>$${p.price}</p>
                    <button onclick="addCart('${p.title}', ${p.price})">Anadir</button>
                </div>
            `;
        });
    })
    .catch(err => console.log('Error'));
}

function addCart(nom, pre) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push({ nom, pre });
    localStorage.setItem('cart', JSON.stringify(cart));
    actCart();
}

function actCart() {
    let lst = document.getElementById('lst');
    let cnt = document.getElementById('cnt');
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    
    if(lst) {
        lst.innerHTML = '';
        cart.forEach(item => {
            let li = document.createElement('li');
            li.textContent = `${item.nom} - $${item.pre}`;
            lst.appendChild(li);
        });
    }
    if(cnt) {
        cnt.textContent = cart.length;
    }
}
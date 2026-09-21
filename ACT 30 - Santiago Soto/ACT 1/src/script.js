/*Ejercicio práctico #1:
Aplicar el consumo de API Fetch en tu proyecto personal
Enunciado: En este ejercicio, vas a integrar el consumo de una API REST utilizando
fetch() en tu proyecto personal de e-commerce o cualquier otro proyecto que estés
desarrollando. Los pasos a seguir son:
1. Elige una API pública (como Fake Store API) que te proporcione datos de
productos, usuarios y usuarias o cualquier otro recurso que quieras mostrar en
tu proyecto.
2. Usa fetch() para hacer una solicitud a la API y obtener los datos.
3. Muestra los datos obtenidos en tu proyecto, ya sea en forma de lista de
productos, usuarias o usuarios o lo que elijas.
4. Asegúrate de manejar los posibles errores utilizando .catch() y mostrá un
mensaje si algo falla.
5. Opcional: Integra los datos obtenidos con alguna funcionalidad de tu proyecto,
como un carrito de compras o una lista de productos favoritos. */

document.addEventListener('DOMContentLoaded', () => {
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
                </div>
            `;
        });
    })
    .catch(err => {
        let div = document.getElementById('prod');
        div.innerHTML = '<p>Error al cargar</p>';
    });
});

document.addEventListener('DOMContentLoaded', () => {
    fetch('../cervezas.json')
        .then(response => response.json())
        .then(data => {
            window.cervezas = data;
            mostrarTodas();
        });
});

function mostrarTodas() {
    mostrarResultados(window.cervezas);
}

function buscar() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const resultados = window.cervezas.filter(cerveza => 
        cerveza.nombre.toLowerCase().includes(query)
    );
    mostrarResultados(resultados);
}

function mostrarResultados(cervezas) {
    const contenedor = document.getElementById('resultados');
    contenedor.innerHTML = '';

    if (cervezas.length === 0) {
        contenedor.innerHTML = '<div class="cerveza-item">No hay resultados 😢</div>';
        return;
    }

    cervezas.forEach(cerveza => {
        const div = document.createElement('div');
        div.className = 'cerveza-item';
        div.innerHTML = `
            <strong>${cerveza.nombre}</strong>
            <div class="precio">${cerveza.precio}</div>
        `;
        contenedor.appendChild(div);
    });
}

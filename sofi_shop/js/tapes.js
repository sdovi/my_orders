

// Функция для получения данных из API и создания карточек
async function fetchAndDisplayProducts() {
    try {
        const response = await fetch('http://localhost:3000/products');
        const products = await response.json();
        const container = document.getElementById('ads-section');

        products.forEach(product => {
            const card = createProductCard(product);
            container.appendChild(card);
        });
    } catch (error) {
        console.error('Error fetching and displaying products:', error);
    }
}



function createProductCard(product) {
    const isFavorite = isProductInFavorites(product.id);

    const card = document.createElement('div');
    card.classList.add('col-6', 'sect_card', 'product-card');
    card.setAttribute('id', `product-${product.id}`);
    card.innerHTML = `
      <img src="${product.photo}" alt="" class="product-image">
      <h5>${product.name}</h5>
      <p>${product.desk}</p>
      <div class="sect__card-price">
        <div class="sect__card-price-txt">
          <h5>Цена</h5>
          <h5>${product.price} сум</h5>
        </div>
        <div class="sect__card-like">
          <div class="favorite-button">
            ${isFavorite ?
            `<img src="./Img/Sect1_img/Vector (1).svg" alt="Удалить из избранного" class="remove-from-favorite" onclick="removeFromFavorites(${product.id})">` :
            `<img src="./Img/Sect1_img/Vector (2).svg" alt="Добавить в избранное" class="add-to-favorite" onclick="addToFavorites(${product.id})">`}
          </div>
        </div>
      </div>
    `;

    // Добавление обработчика клика на изображение
    const productImage = card.querySelector('.product-image');
    productImage.addEventListener('click', () => {
        window.location.href = `select_card.html?id=${product.id}`;
    });

    return card;
}


// Функция для добавления продукта в избранное
function addToFavorites(productId) {
    let favorites = localStorage.getItem('favorites') ? JSON.parse(localStorage.getItem('favorites')) : [];
    if (!favorites.includes(productId)) {
        favorites.push(productId);
        localStorage.setItem('favorites', JSON.stringify(favorites));
        updateProductCard(productId); // Обновляем карточку после добавления в избранное
        updateProductImage(productId); // Обновляем изображение продукта
    }
}

// Функция для удаления продукта из избранного
function removeFromFavorites(productId) {
    let favorites = localStorage.getItem('favorites') ? JSON.parse(localStorage.getItem('favorites')) : [];
    favorites = favorites.filter(id => id !== productId);
    localStorage.setItem('favorites', JSON.stringify(favorites));
    updateProductCard(productId); // Обновляем карточку после удаления из избранного
    updateProductImage(productId); // Обновляем изображение продукта
}

// Функция для обновления карточки продукта
function updateProductCard(productId) {
    const isFavorite = isProductInFavorites(productId);
    const productCard = document.getElementById(`product-${productId}`);

    if (productCard) {
        const favoriteButton = productCard.querySelector('.favorite-button');
        if (favoriteButton) {
            favoriteButton.innerHTML = isFavorite ?
                `<img src="./Img/Sect1_img/Vector (1).svg" alt="Удалить из избранного" class="remove-from-favorite" onclick="removeFromFavorites(${productId})">` :
                `<img src="./Img/Sect1_img/Vector (2).svg" alt="Добавить в избранное" class="add-to-favorite" onclick="addToFavorites(${productId})">`;
        }
    }
}

// Функция для обновления изображения продукта
function updateProductImage(productId) {
    const productCard = document.getElementById(`product-${productId}`);
    if (productCard) {
        const imageElement = productCard.querySelector('img');
        if (imageElement) {
            const isFavorite = isProductInFavorites(productId);
            const newImageSrc = isFavorite ? './Img/Sect1_img/Rectangle 45.jpg' : './Img/Sect1_img/Rectangle 45.jpg'; // Путь к вашему изображению
            imageElement.src = newImageSrc;
        }
    }
}

// Функция для проверки, добавлен ли продукт в избранное
function isProductInFavorites(productId) {
    const favorites = localStorage.getItem('favorites') ? JSON.parse(localStorage.getItem('favorites')) : [];
    return favorites.includes(productId);
}

// Вызов функции для получения и отображения продуктов
fetchAndDisplayProducts();

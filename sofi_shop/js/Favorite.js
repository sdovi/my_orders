



// Функция для удаления продукта из избранного
function removeFromFavorites(productId) {
  let favorites = localStorage.getItem('favorites') ? JSON.parse(localStorage.getItem('favorites')) : [];
  favorites = favorites.filter(id => id !== productId);
  localStorage.setItem('favorites', JSON.stringify(favorites));
  // После удаления обновляем отображение избранных продуктов
  document.getElementById('cart-items').innerHTML = '';
  displayFavoriteProducts();
}

// Функция для проверки, добавлен ли продукт в избранное
function isProductInFavorites(productId) {
  const favorites = localStorage.getItem('favorites') ? JSON.parse(localStorage.getItem('favorites')) : [];
  return favorites.includes(productId);
}
async function fetchProduct(productId) {
    try {
      const response = await fetch(`http://localhost:3000/products/${productId}`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const product = await response.json();
      return product;
    } catch (error) {
      console.error('Error fetching product:', error);
      throw error;
    }
  }
  

// Функция для отображения карточек избранных продуктов с загрузкой данных с сервера
async function displayFavoriteProducts() {
  const favorites = localStorage.getItem('favorites') ? JSON.parse(localStorage.getItem('favorites')) : [];
  const container = document.getElementById('cart-items');

  for (const productId of favorites) {
    try {
      // Загружаем данные о продукте с сервера
      const product = await fetchProduct(productId);
      
      // Создаем карточку продукта
      const card = document.createElement('div');
      card.classList.add('col-6', 'sect_card');
      card.innerHTML = `
      <img src="${product.photo}" alt="">
      <h5>${product.name}</h5>
      <p>${product.desk}</p>
      <div class="sect__card-price">
        <div class="sect__card-price-txt">
          <h5>Цена</h5>
          <h5>${product.price} сум</h5>
        </div>
        <div class="sect__card-like">
          <div class="favorite-button">
            <img src="./Img/Sect1_img/Vector (1).svg" alt="Удалить из избранного" class="remove-from-favorite" onclick="removeFromFavorites(${product.id})">
          </div>
        </div>
      </div>
      `;
      
      container.appendChild(card); // Добавляем карточку в контейнер
    } catch (error) {
      console.error('Error fetching product:', error);
    }
  }
}

// Вызов функции для отображения избранных продуктов
displayFavoriteProducts();

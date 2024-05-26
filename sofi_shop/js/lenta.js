// Создаем контейнер с классом container2
const container2 = document.createElement('div');
container2.classList.add('container2');

// 1. Организуем запрос к API для получения данных
fetch('http://localhost:3000/products')
  .then(response => response.json())
  .then(data => {
    // 2. Обрабатываем полученные данные
    data.forEach(product => {
      // Создаем контейнер продукта
      const productContainer = document.createElement('div');
      productContainer.classList.add('lenta__header');

      // Создаем контейнер для изображения продукта
      const productImageContainer = document.createElement('div');
      productImageContainer.classList.add('lenta__header-img');

      // Создаем изображение продукта
      const productImage = document.createElement('img');
      productImage.src = product.photo;
      productImage.alt = product.name;

      // Добавляем изображение в контейнер изображения продукта
      productImageContainer.appendChild(productImage);

      // Добавляем контейнер изображения продукта в контейнер продукта
      productContainer.appendChild(productImageContainer);

      // Создаем контейнер под элементы "like" и "share"
      const likeShareContainer = document.createElement('div');
      likeShareContainer.classList.add('select__header-under-like', 'lenta__header-under-like');

      // Создаем контейнер для кнопки "like"
      const likeContainer = document.createElement('div');
      likeContainer.classList.add('select__header-like-card');

      // Создаем изображение кнопки "like"
      const likeImage = document.createElement('img');
      likeImage.src = './Img/select/Vector (4).svg';
      likeImage.alt = 'like';

      // Создаем элемент для отображения количества лайков
      const likeCount = document.createElement('p');
      likeCount.innerText = '1202';

      // Добавляем изображение и количество лайков в контейнер для кнопки "like"
      likeContainer.appendChild(likeImage);
      likeContainer.appendChild(likeCount);

      // Создаем контейнер для кнопки "share"
      const shareContainer = document.createElement('div');
      shareContainer.classList.add('select__header-link', 'lenta__header-like');

      // Создаем изображение кнопки "share"
      const shareImage = document.createElement('img');
      shareImage.src = './Img/select/fluent_share-20-regular.svg';
      shareImage.alt = 'share';

      // Добавляем изображение кнопки "share" в контейнер для кнопки "share"
      shareContainer.appendChild(shareImage);

      // Создаем контейнер для изображения кнопки "phone-vibrate"
      const phoneContainer = document.createElement('div');
      phoneContainer.classList.add('lenta__header-link', 'ms-auto');

      // Создаем изображение кнопки "phone-vibrate"
      const phoneImage = document.createElement('img');
      phoneImage.src = './Img/lenta/bi_phone-vibrate.svg';
      phoneImage.alt = 'phone-vibrate';

      // Добавляем изображение кнопки "phone-vibrate" в контейнер для изображения кнопки "phone-vibrate"
      phoneContainer.appendChild(phoneImage);

      // Добавляем контейнеры кнопок "like", "share" и "phone-vibrate" в контейнер под элементы "like" и "share"
      likeShareContainer.appendChild(likeContainer);
      likeShareContainer.appendChild(shareContainer);
      likeShareContainer.appendChild(phoneContainer);

      // Добавляем контейнер под элементы "like" и "share" в контейнер продукта
      productContainer.appendChild(likeShareContainer);

      // Создаем контейнер для заголовка продукта
      const productTitleContainer = document.createElement('div');
      productTitleContainer.classList.add('lenta__header-title');

      // Создаем элементы заголовка продукта: название, цена, описание
      const productName = document.createElement('h5');
      productName.innerText = product.name;

      const productPrice = document.createElement('h6');
      productPrice.innerText = `Price: ${product.price} UZS`;

      const productDescription = document.createElement('p');
      productDescription.innerText = `Description: ${product.desk}`;

      // Добавляем элементы заголовка продукта в контейнер заголовка продукта
      productTitleContainer.appendChild(productName);
      productTitleContainer.appendChild(productPrice);
      productTitleContainer.appendChild(productDescription);

      // Добавляем контейнер заголовка продукта в контейнер продукта
      productContainer.appendChild(productTitleContainer);

      // Добавляем контейнер продукта в контейнер 2
      container2.appendChild(productContainer);
    });

    // Добавляем контейнер 2 в body
    document.body.appendChild(container2);
  })
  .catch(error => console.error('Error fetching data:', error));





  
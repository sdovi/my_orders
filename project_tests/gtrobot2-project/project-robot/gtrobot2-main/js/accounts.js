// post token 

var token = localStorage.getItem('token');
fetch('https://api.gtrobot.shop/accounts/user/', {
  method: 'GET',
  headers: {
    'Authorization': 'Token ' + token
  }
})
.then(response => response.json())
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Ошибка при отправке запроса:', error);
});

fetch('https://api.gtrobot.shop/accounts/user/', {
  method: 'GET',
  headers: {
    'Authorization': 'Token ' + token
  }
})
.then(response => response.json())
.then(data => {
  console.log('Полученные данные:', data);

  document.querySelector('.account_data-email').href = "mailto:" + data.name;
  document.querySelector('.account_data-email').textContent = data.name;
  document.querySelector('.account_data-number').href = "tel:" + data.phone;
  document.querySelector('.account_data-number').textContent = data.phone;
  
  console.log('Имя пользователя:', data.name);
  console.log('Телефон пользователя:', data.phone);
})
.catch(error => {
  console.error('Ошибка при отправке запроса:', error);
});






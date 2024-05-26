import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './style.css';
import { useParams } from 'react-router-dom';

export default function Test() {
  const [clubData, setClubData] = useState(null);
  const { id } = useParams(); // Получаем айди из параметров URL

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`https://soccer365.ru/clubs/${id}`);
        const parser = new DOMParser();
        const htmlDocument = parser.parseFromString(response.data, 'text/html');
        const clubDataElement = htmlDocument.querySelector('.block_body');
        if (clubDataElement) {
          // Удаляем ссылки, указанные текстовые элементы и фотографии тренеров из HTML кода перед установкой в state
          const cleanedHTML = removeElements(clubDataElement.innerHTML);
          setClubData(cleanedHTML);
        }
      } catch (error) {
        console.error('Ошибка при получении данных:', error);
      }
    };

    fetchData();
  }, []);

  // Функция для удаления ссылок, указанных текстовых элементов и фотографий тренеров из HTML
  const removeElements = (html) => {
    // Создаем временный div элемент
    const tempDiv = document.createElement('div');
    // Устанавливаем внутренний HTML содержимое во временный div
    tempDiv.innerHTML = html;
    // Удаляем ссылки
    tempDiv.querySelectorAll('a').forEach((link) => link.remove());
    // Удаляем указанные текстовые элементы
    tempDiv.querySelectorAll('.params_key').forEach((element) => {
      const text = element.textContent.trim();
      if (text === 'Главный тренер' || text === 'Соревнования' || text === 'Ссылки') {
        element.parentNode.removeChild(element);
      }
    });
    // Удаляем фотографии тренеров
    tempDiv.querySelectorAll('.img16').forEach((img) => {
      img.parentNode.removeChild(img);
    });
    // Возвращаем HTML содержимое без ссылок, указанных текстовых элементов и фотографий тренеров
    return tempDiv.innerHTML;
  };

  return (
    <div className=' container-fluid'>
      
      {clubData && (
        <div dangerouslySetInnerHTML={{ __html: clubData }} />
      )}
    </div>
  );
}

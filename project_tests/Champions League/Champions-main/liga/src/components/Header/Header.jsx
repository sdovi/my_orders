import React, { useState, useEffect } from 'react';
import img from './img/mg1.webp';
import './style.css';
import axios from 'axios';

export default function Header() {
  const [news, setNews] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [newsPerPage] = useState(16); // Количество новостей на одной странице
  const [pageNumbers, setPageNumbers] = useState([]); // Массив номеров страниц

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await axios.get('https://newsapi.org/v2/everything', {
          params: {
            q: 'Футбол',
            apiKey: '81874c94b20f4fa7ac5a88f5fbfd9006',
          },
        });
        setNews(response.data.articles);
      } catch (error) {
        console.error('Error fetching news:', error);
      }
    };

    fetchNews();
  }, []);

  const indexOfLastNews = currentPage * newsPerPage;
  const indexOfFirstNews = indexOfLastNews - newsPerPage;
  const currentNews = news.slice(indexOfFirstNews, indexOfLastNews);

  useEffect(() => {
    const pageNumbersArray = [];
    for (let i = 1; i <= Math.ceil(news.length / newsPerPage); i++) {
      pageNumbersArray.push(i);
    }
    setPageNumbers(pageNumbersArray);
  }, [news.length, newsPerPage]);

  const paginate = (pageNumber) => setCurrentPage(pageNumber);







  

  return (
    <div className="footbal__page">
      <div className="container-fluid">
        <h3 className="footbal__top-text pt-4 pb-3">Новости Футбола</h3>
        <div className="footbal__blocks row">
          {currentNews.map((article, index) => (
            <div className="col-lg-3 col-md-4 col-sm-12" key={index}>
              <div className="footbal__card">
                <div className="footbal__card-img">
                  <img src={article.urlToImage} alt="foto" />
                  <p>
                    {article.title.length > 55
                      ? article.title.slice(0, 55) + '...'
                      : article.title}
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
        <ul className="pagination justify-content-center">
          {pageNumbers.map((number, index) => (
            <li key={index} className="page-item">
              <button onClick={() => paginate(number)} className="page-link">
                {number}
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

import React, { useState } from 'react';
import { slide as Menu } from 'react-burger-menu';
import './style.css'
import img from './img/logo.webp'
import { Link } from 'react-router-dom';

export default function Navbar() {
//     const [isOpen, setIsOpen] = useState(false);
//     <div>
//     <button onClick={toggleMenu}>Меню</button>
//     <Menu right isOpen={isOpen} onClose={closeMenu}>
//       <a href="/">Главная</a>
//       <a href="/about">О нас</a>
//       <a href="/contact">Контакты</a>
//     </Menu>
//   </div>
//     const closeMenu = () => setIsOpen(false);
//     const toggleMenu = () => setIsOpen(!isOpen);


  return (
     <div>
      

    <nav class="navbar navbar-expand-lg navbar-bg">
  <div class="container-fluid navbar-com-block">
    <Link to={'/'} className='nav__txt-link'><img src={img} alt="" /></Link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0 ">
        <Link className='nav__txt-link' to={'/'}><li class="nav-item ms-5">
        <p className='nav-txt'>Новости</p>
        </li></Link>
        <Link className='nav__txt-link' to={'/ligaforms'}><li class="nav-itemms ms-3">
        <p className='nav-txt'>Расписание</p>
        </li></Link>
       <Link  className='nav__txt-link' to={'/table'}> <li class="nav-item ms-3">
        <p className='nav-txt'>Таблица</p>
        </li></Link>
        <Link className='nav__txt-link' to={'/basket'}><li class="nav-item ms-3">
        <p className='nav-txt'>Баскетбол</p>
        </li></Link>
        <Link className='nav__txt-link' to={'/hokey'}><li class="nav-item ms-3">
        <p className='nav-txt'>Хоккей</p>
        </li></Link>
      </ul>
      <button className='Navbar__register'>Войти</button>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Поиск" aria-label="Search"/>
      </form>
      
    </div>
  </div>
</nav>
     </div>
  )
}

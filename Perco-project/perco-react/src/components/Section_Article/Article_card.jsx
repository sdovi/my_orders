import React from 'react'
import { Link } from 'react-router-dom';
import img from './img/photo_1_2024-05-14_16-40-28.jpg'


import logo from '../Header/img/output-onlinetools.png'

import img2 from './img/card_img/photo_2024-05-14_21-55-43 (2).jpg'

import img3 from './img/card_img/photo_2024-05-14_21-55-44 (2).jpg'
import img4 from './img/card_img/photo_2024-05-14_21-55-44.jpg'



export default function Article_card() {
  return (
    <div className="article-card-container ">
      <div className="section2">
        <div className="sect4-bg mb-3" style={{ 
      backgroundImage: `url(${img})`
    }}
    >
    <nav className="navbar article-nav ">
      <div className="container-fluid navbar2">
          <Link className='header__link' to={`/`}>
          <span className="navbar-brand mb-0 h1">Main</span></Link>
        <form className="d-flex header__logo2" role="search">
        <Link className='header__link' to={`/`}><img className='header__logo me-2' src={logo} alt="" /></Link>
          
        </form>
      </div>
    </nav>
          <div className="container-fluid2 pb-5">
            <div className="section2__txt row">

              <div className="col-lg-4 col-md-6 col-sm-12 article-card">
              <Link className='article_link header__link' to={'/article_n1'}>
              <div className="arcicle_imgs">
                
                <img src={img2} alt="" className="article-image" />
                </div>
              </Link>
             
              <div className="article-content">
                    <h2>DENIAL. ITS FORMS AND INFLUENCE ON EFFICIENCY AT WORK</h2>
                  </div>
              </div>

<div className="col-lg-4 col-md-6 col-sm-12 article-card">
<div className="arcicle_imgs">
  <Link  className='article_link header__link' to={'/article_n2'}>
<img src={img3} alt="" className="article-image article-image2" /></Link>
</div>
  <div className="article-content">
    <h2>Today we will talk about the impact of such a pattern of behavior as 
people pleasing on effective work.</h2>
  </div>
</div>

<div className="col-lg-4 col-md-6 col-sm-12 article-card">
<div className="arcicle_imgs">
  <Link  className='article_link header__link' to={'/article_n3'}>
<img src={img4} alt="" className="article-image" /></Link>
  
</div>
  <div className="article-content">
    <h2>REQUIREMENTS FOR EMPLOYEE QUALITIES IN DIFFERENT POSITIONS</h2>
  </div>
</div>


{/* <div className="col-lg-4 col-md-6 col-sm-12 article-card">
<div className="arcicle_imgs">
  
<img src="https://imgbly.com/ib/KEXNjlaTq9.jpg" alt="" className="article-image" />
</div>
  <div className="article-content">
    <h2>Article Title</h2>
  </div>
</div> */}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

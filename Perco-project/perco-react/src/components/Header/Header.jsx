import React, { useEffect, useState, useCallback } from 'react';
import './style.css';
import { Link } from 'react-router-dom';
import axios from 'axios';
import logo from './img/output-onlinetools.png'
import nav from './img/nav.jpg'

export default function Header() {
  const [blackOverlayHeight, setBlackOverlayHeight] = useState(0);
  const [email, setEmail] = useState('');
  const [comment, setComment] = useState('');
  const [modalVisible, setModalVisible] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setBlackOverlayHeight(window.innerHeight);
  }, []);

  const handleSubmit = useCallback(async (event) => {
    event.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post('https://185.158.132.183:8084/user/email/', {
        title: email,
        description: comment
      });
      console.log(response.data);
      setEmail(''); 
      setComment('');
      setModalVisible(false);
    } catch (error) {
      console.error('Error:', error);
      setError('Failed to send email. Please try again.');
    } finally {
      setLoading(false);
    }
  }, [email, comment]);

  return (
    <div className="header__logo-text " style={{ 
      backgroundImage: `url(${nav})`
    }}>
      <nav className="navbar">
        <div className="container-fluid navbar2">
          <Link className='header__link' to={`/article`}>
            <span className="navbar-brand mb-0 h1">Articles</span>
          </Link>
          <form className="d-flex header__logo2" role="search">
          <Link className='header__link' to={`/`}><img className='header__logo me-2' src={logo} alt="" /></Link>
          </form>
        </div>
      </nav>

      <div className="sect__block_1">
        <h1 className='header__txt pb-2'>OUR MAIN AREAS</h1>
        <p className='header_p'>CHECKING THE BACKGROUNDS OF COMPANIES AND EMPLOYEES.</p>
        <p className='header_p'>POLITICAL CONSULTING (GEOPOLITICS, STRUCTURE, TRENDS, ANALYSIS).</p>
        <p className='header_p'>EFFECTIVE METHODS OF BUSINESS MANAGEMENT.</p>
        <p className='header_p'>INTERNAL BUSINESS STRUCTURING, EFFICIENCY INCREASE. CREATION OF A SYSTEM OF ANALYTICAL CONTROL OF YOUR BUSINESS.</p>
        <p className='header_p'>NEGOTIATION STRATEGY (INCLUDING AGGRESSIVE AND ATTACKING TECHNIQUES).</p>
        <p className='header_p'>HR CONSULTING.CONSTRUCTIVE SOLUTION OF INTERNAL CONFLICTS IN THE COMPANY.</p>
        <div className="mt-3 header_block-btn">
          <button className='header__btn2' >
            <a href="https://api.whatsapp.com/send?phone=972506332883">Contact us</a>
          </button>
          <button className='header__btn2' onClick={() => setModalVisible(true)}>Send an email</button>
          {modalVisible && (
            <div className="modal">
              <div className="modal-content">
                <span className="close" onClick={() => setModalVisible(false)}>&times;</span>
                <form className='header_form' onSubmit={handleSubmit}>
                  <input className="input" type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
                  <textarea className="input" placeholder="Comment (optional)" value={comment} onChange={(e) => setComment(e.target.value)} />
                  {error && <p className="error">{error}</p>}
                  <button className="submit-btn" type="submit" disabled={loading}>
                    {loading ? 'Submitting...' : 'Submit'}
                  </button>
                </form>
              </div>
            </div>
          )}
        </div>
        <p className='header_p header_p2 pt-3'>71-75, Shelton Street, Covent Garden, London, WC2H 9JQ</p>
      </div>
    </div>
  );
}

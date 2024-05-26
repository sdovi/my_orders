import React from 'react';
import img from './Img/1.png';
import './style.css';

export default function Section1() {
    return (
    <div>
         <div className='sect1'>
            <div className="sect1__overlay"></div> {/* Добавляем черный прозрачный фон */}
            <div className="container-fluid sect1__cards  ">
                <div className="sect1__comblock  row">
                <div className="col-lg-6 col-md-6 col-sm-12 sect__block_1 ">
                      <h1>OUR MAIN AREAS</h1>
                      <p>CHECKING THE BACKGROUNDS OF COMPANIES AND EMPLOYEES.</p>
                      <p>POLITICAL CONSULTING (GEOPOLITICS, STRUCTURE, TRENDS, ANALYSIS).</p>
                      <p>EFFECTIVE METHODS OF BUSINESS MANAGEMENT .</p>
                      <p>INTERNAL BUSINESS STRUCTURING, EFFICIENCY INCREASE. CREATION OF A SYSTEM OF ANALYTICAL CONTROL OF YOUR BUSINESS.</p>
                      <p>NEGOTIATION STRATEGY (INCLUDING AGGRESSIVE AND ATTACKING TECHNIQUES).</p>
                      <p>HR CONSULTING.CONSTRUCTIVE SOLUTION OF INTERNAL CONFLICTS IN THE COMPANY.</p>
                </div>
                <div className="col-lg-6 col-md-6 col-sm-12 sect__block_1 ">
                      <h1>OUR MAIN AREAS</h1>
                      <p>CHECKING THE BACKGROUNDS OF COMPANIES AND EMPLOYEES.</p>
                      <p>POLITICAL CONSULTING (GEOPOLITICS, STRUCTURE, TRENDS, ANALYSIS).</p>
                      <p>EFFECTIVE METHODS OF BUSINESS MANAGEMENT .</p>
                      <p>INTERNAL BUSINESS STRUCTURING, EFFICIENCY INCREASE. CREATION OF A SYSTEM OF ANALYTICAL CONTROL OF YOUR BUSINESS.</p>
                      <p>NEGOTIATION STRATEGY (INCLUDING AGGRESSIVE AND ATTACKING TECHNIQUES).</p>
                      <p>HR CONSULTING.CONSTRUCTIVE SOLUTION OF INTERNAL CONFLICTS IN THE COMPANY.</p>
                </div>
                <div className="offset-lg-3 col-lg-6 col-md-6 col-sm-12 sect__block_1 sect__block_2 ">
                      <h1>OUR MAIN AREAS</h1>
                      <p>CHECKING THE BACKGROUNDS OF COMPANIES AND EMPLOYEES.</p>
                      <p>POLITICAL CONSULTING (GEOPOLITICS, STRUCTURE, TRENDS, ANALYSIS).</p>
                      <p>EFFECTIVE METHODS OF BUSINESS MANAGEMENT .</p>
                      <p>INTERNAL BUSINESS STRUCTURING, EFFICIENCY INCREASE. CREATION OF A SYSTEM OF ANALYTICAL CONTROL OF YOUR BUSINESS.</p>
                      <p>NEGOTIATION STRATEGY (INCLUDING AGGRESSIVE AND ATTACKING TECHNIQUES).</p>
                      <p>HR CONSULTING.CONSTRUCTIVE SOLUTION OF INTERNAL CONFLICTS IN THE COMPANY.</p>
                </div>
                </div>
            </div>
        </div>
    </div>
    );
}

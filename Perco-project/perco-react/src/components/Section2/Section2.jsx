import React from 'react'
import './style.css'
import img from './img/1.jpg'

export default function Section2() {
  return (
    <div>
      <div className="section2">
      
          <div className="sect2-bg" style={{ 
      backgroundImage: `url(${img})`
    }}
    >
          
        <div className="container-fluid2">
        <div className="section2__txt">
            <h1 className='sect2__h1'>WHAT WE DO?</h1>
            <p>SCOPE OF SERVICES <br />
            ••• Checking the backgrounds of companies and employees ••• <br /> <br />
Our team will check for you all the information about the business 
and any of the employees and prepare a detailed report, on the
basis of which you will have a complete picture of who you are
dealing with and the risks associated with it. The check includes:
for business (legal cleanliness of the company, investments,
corrupt ties, money laundering, sanctions blocking,) for employees
(fake biography and education, violation of laws, testimonials from
previous jobs, financial viability, discrediting family ties, use of
illegal substances ) <br /> <br />
••Political consulting ••• <br />(geopolitics, structure, trends, analysis). <br /> <br />
To conduct and develop business, one must clearly understand
the trends and tools for implementing the geopolitical plans of
modern centers of influence in the world.   Even if your business is
limited to the domestic market of one country, geopolitical and
domestic trends have a direct impact on the economy, both
outside and inside the country. To effectively build and grow your
business, our team of analysts will provide you with data for short
and medium term planning opportunities. <br /> <br />
••• Effective methods of business management ••• <br /> <br />
We audit the effectiveness of your company's management
methods, the compliance of managers' knowledge with the tasks
and plans of the company. At the end of the audit, clear
recommendations are given for restructuring, increasing the
efficiency of management, employees are indicated that do not
correspond to the level of knowledge for managerial positions. If
necessary, we will take care of building the right management
vertical adapted specifically for your business.</p>
        </div>
        </div>
        </div>
      </div>
    </div>
  )
}

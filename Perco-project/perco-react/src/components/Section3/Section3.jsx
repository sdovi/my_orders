import React from 'react'
import './style.css'
import img from './img/1.jpg'

export default function Section3() {
  return (
    <div>
    <div className="section2">
        <div className="sect3-bg" style={{ 
      backgroundImage: `url(${img})`
    }}>
        
      <div className="container-fluid2">
      <div className="section2__txt">
          <h1 className='sect2__h1'>WHAT WE DO?</h1>
          <p>SCOPE OF SERVICES <br />
••• Internal business structuring, efficiency increase •••  <br /> <br />
Often, the functions of employees are duplicated in
companies, the priority of tasks is not correctly set by the
employees themselves, relationships within the team are built
on personal preferences and non-working connections.This
creates sub-groups within companies and has a strong impact
on performance and often translates into covert direct or
indirect sabotage that is contrary to the plans and policies of
the company. Our task, with the help of special techniques, is
to identify such trends and stop them at all stages.  <br /> <br />
••• Creation of a system of analytical control of your business ••• <br /> <br />
Modern business control methods allow the owner not to
waste time on checks, clarifications, doubts about the
reliability of information and risks associated with the human
factor. At your request, we will develop and implement a
control system for your business using automated data
collection and analysis. As a result, you will receive a real-time
interface with clear analytical data on the problem areas of the
company that require your intervention or adjustment. We will
free up additional time resources for you, which you use for
strategic planning and generating ideas for the development of
your business.This becomes impossible when the manager has
to "sink" in the organizational management and everyday
issues of the company. (We will be happy to tell you in detail
about the methods and tools for creating such a control
method during a personal consultation)</p>
      </div>
      </div>
      </div>
    </div>
      
    </div>
  )
}

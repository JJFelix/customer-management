import React from 'react'
import '../styles/Home.css'
const Home = () => {
  const username = 'Felix'
  return (
    <div className='main-wrapper'>
      {username === 'Felix' && 
        <div className='homepage'>
          {/* <h1>Home</h1> */}
          {/* <img src="https://www.nextiva.com/blog/what-is-customer-management.html" alt="image" /> */}
        </div>
      }
    </div>
  )
}

export default Home
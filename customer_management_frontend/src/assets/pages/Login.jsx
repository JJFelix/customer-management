import axios from 'axios'
import React, { useEffect, useState } from 'react'

import { backend_url } from '../../App'

const Login = () => {
    useEffect(()=>{
        
        // redirect user to backend login page to initiate the OAuth2 flow
        window.location.href = `${backend_url}/api/login`

        // axios
        // .post(`${backend_url}/api/login`)
        // .then(()=>{
        //     // setToken(response.data)  
        //     console.log("Logged in");
                      
        // })
        // .catch(()=>{
        //     console.error(error.response.data.error);
        // })
    }, [])

    const handleLoginClick = () => {
      window.location.href = `${backend_url}/api/login`
    }

  return (
    <div className='main-wrapper'>
        {/* Checking Login Status...<i className="fa fa-spinner" aria-hidden="true"></i> */}
        <Link onClick={handleLoginClick()}>Click here to login</Link>
    </div>
  )
}

export default Login
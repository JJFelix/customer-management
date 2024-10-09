import axios from 'axios'
import React, { useEffect, useState } from 'react'

import { backend_url } from '../../App'

const Login = () => {
    const [token, setToken] = useState()
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

  return (
    <div className='main-wrapper'>
        Checking Login Status...<i className="fa fa-spinner" aria-hidden="true"></i>
    </div>
  )
}

export default Login
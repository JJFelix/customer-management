import React, { useEffect, useState } from 'react'

const Logout = () => {
    const [token, setToken] = useState()
    useEffect(()=>{
        
        // redirect user to backend login page to initiate the OAuth2 flow
        window.location.href = "http://localhost:8000/api/logout"

        // axios
        // .post(`http://localhost:8000/api/login`)
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
        Redirecting to logout...
    </div>
  )
}

export default Logout
import axios from 'axios'
import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'

import { backend_url } from '../../App'

const AddCustomer = () => {
    const [userData, setUserData] = useState({
        name: "",
        phone:""
    })

    const navigate = useNavigate()

    const handleSubmit = (e)=>{
        e.preventDefault()

        console.log('user details: ', userData);
        axios
        .post(`${backend_url}/api/customers/add/`, userData)
        .then((response)=>{
            // console.log(response.data)    
            navigate('/customers')        
        })
        .catch((error)=>{
            console.error(error.response.data.error);            
        })
    }

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setUserData({
          ...userData,
          [name]: value,
        });
      };
    
  return (
    <div className='main-wrapper'>
        <h1><u>Add Customer</u></h1>
        <div>            
            <form className='' onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="name" className="form-label">
                    Name
                    </label>
                    <input name="name" value={userData.name} onChange={handleInputChange} type="text" className="form-control" id="name" aria-describedby="name"/>
                </div>
                <div className="mb-3">
                    <label htmlFor="phone" className="form-label">
                    Phone Number
                    </label>
                    <input name="phone" value={userData.phone} onChange={handleInputChange} type="text" className="form-control" id="phone" aria-describedby="phone"/>
                </div>
                <button className='btn btn-success' type="submit">Submit</button>
            </form>
        </div>
    </div>
  )
}

export default AddCustomer
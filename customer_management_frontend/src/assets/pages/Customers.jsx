import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

import { backend_url } from '../../App'

const Customers = () => {
  const [customers, setCustomers] = useState([])

  useEffect(()=>{
    axios
    .get(`${backend_url}/api/customers`)    
    .then((response) =>{
      // console.log(response.data)
      setCustomers(response.data)      
    })
    .catch((error) =>{
      console.error(error.response.data.error);      
    })
  }, [])

  // console.log(customers?.data);  

  return (
    <div className='main-wrapper'>
      <h1>Customers</h1>
      <div>
        <Link 
          className='btn btn-primary'
          to={'/add_customer'}
        >
        Add New Customer
        </Link>
      </div>
      <div className='data mt-4'>
        
        {customers.data?.map((customer, index) => (
          <div className='data-card' key={index}>
            <p><strong>Name: </strong>{customer.name}</p>
            <p><strong>Phone: </strong>{customer.phone}</p>
            <Link className='btn btn-primary m-1' to={{pathname:`/customers/${customer.customer_id}`}}>Click to see Orders</Link>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Customers
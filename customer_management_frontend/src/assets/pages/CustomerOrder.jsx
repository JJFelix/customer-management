import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'

import { backend_url, dateTime } from '../../App'

const CustomerOrder = () => {
  const { customer_id } = useParams()

  const [customer, setCustomer] = useState([])

  useEffect(()=>{
    axios
    .get(`${backend_url}/api/customers/${customer_id}`)
    .then((response)=>{
      // console.log(response.data)
      setCustomer(response.data)      
    })
    .catch((error)=>{
      console.error(error.response.data.error)     
    })
  })

  console.log("Customer data: ", customer?.customer, customer?.orders)
  
  return (
    <div className='main-wrapper'>
      <h1>Customer: {customer?.customer.name}</h1>
      <h2>Orders</h2>
      <div className='data mt-4'>        
        {customer.orders?.map((order, index) => (
          <div className='data-card' key={index}>
            <p><strong>Item: </strong>{order.item}</p>
            <p><strong>Amount: </strong>{order.amount}</p>
            <p><strong>Time: </strong>{dateTime(order.time)}</p>
          </div>
        ))}
        <Link className='btn btn-primary m-1' to={{pathname:`/customers`}}>Back to Customers</Link>
      </div>
    </div>
  )
}

export default CustomerOrder

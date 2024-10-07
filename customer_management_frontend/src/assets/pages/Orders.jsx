import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

const Orders = () => {
  const [orders, setOrders] = useState([])

  useEffect(()=>{
    axios
    .get(`http://localhost:8000/api/orders`)    
    .then((response) =>{
      // console.log(response.data)
      setOrders(response.data)      
    })
    .catch((error) =>{
      console.error(error.response.data.error);      
    })
  }, [])

  const dateTime = (e) =>{
    const date = new Date(e)
    const formatedDate = date.toLocaleDateString()
    const formatedTime = date.toLocaleTimeString()

    return formatedDate +" at "+ formatedTime
  }

  const handleDeleteOrder = (order_id) =>{
    axios.
    delete(`http://localhost:8000/api/orders/delete/${order_id}`)
    .then((response) => {
      console.log(response.data.success);
      // Filter out the deleted order from the state
      setOrders((prevOrders) => ({
        ...prevOrders,
        data: prevOrders.data.filter((order) => order.order_id !== order_id),
      }));
    })
    .catch((error) => {
      console.error('Error deleting order:', error)
    })
  }

  console.log(orders?.data);
  return (
    <div className='main-wrapper'>
      <h1>Orders</h1>
      <div>
        <Link 
          className='btn btn-primary'
          to={'/add_order'}
        >
        Add New Order
        </Link>
      </div>
      <div className='data mt-4'>
        
        {orders.data?.map((order, index) => (
          <div className='data-card' key={index}>
            <p><strong>Item: </strong>{order.item}</p>
            <p><strong>Amount: </strong>{order.amount}</p>
            <p><strong>Date: </strong>{dateTime(order.time)}</p>
            {/* <Link className='btn btn-primary' to={{pathname:`/customers/${order.customer}`}}>Click to see Customer</Link> */}
            <Link className='btn btn-success m-1'>Completed</Link>
            <Link className='btn btn-danger m-1' onClick={() => handleDeleteOrder(order.order_id)}>Delete</Link>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Orders
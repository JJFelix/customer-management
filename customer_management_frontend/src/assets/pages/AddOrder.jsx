import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom';

const AddOrder = () => {
    const [customers, setCustomers] = useState([]);
    const [orderData, setOrderData] = useState({
        customer: '',
        item: '',
        amount: 0,
    });
    const navigate = useNavigate();

    // Fetch customers to populate the dropdown
    useEffect(() => {
        axios
        .get('http://localhost:8000/api/customers')
        .then((response) => {
            setCustomers(response.data.data)
            // console.log(customers)
            
        })
        .catch((error) => {
            console.error('Error fetching customers:', error)
        })
    }, [])

    // Handle input change
    const handleChange = (e) => {
        const { name, value } = e.target
        setOrderData({
        ...orderData,
        [name]: value,
        })
    }

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(orderData);
        
        axios
        .post('http://localhost:8000/api/orders/add', orderData)
        .then((response) => {
            console.log('Order added successfully:', response.data)
            // Redirect to the orders page or show a success message
            navigate('/orders')
        })
        .catch((error) => {
            console.error('Error adding order:', error)
        })
    }

  return (
    <div className='main-wrapper'>
        <h1><u>Add Order</u></h1>
        <div>            
            <form className='' onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="customer" className="form-label">
                    Customer: 
                    </label>
                    {/* <input name="customer" value={orderData.customer_id} onChange={handleChange} type="text" className="form-control" id="customer" aria-describedby="customer"/> */}
                    <select name="customer" id="customer" value={orderData.customer} onChange={handleChange} className="form-select form-select-sm" aria-label=".form-select-sm example" required>
                        <option value="">Select Customer</option>
                        {customers?.map((customer, index) => (
                            <option key={index} value={customer.customer_id}>
                                {customer.name}
                            </option>
                        ))}
                    </select>
                </div>
                <div className="mb-3">
                    <label htmlFor="item" className="form-label">
                    Item
                    </label>
                    <input name="item" value={orderData.item} onChange={handleChange} type="text" className="form-control" id="item" aria-describedby="item"/>
                </div>
                <div className="mb-3">
                    <label htmlFor="amount" className="form-label">
                    Amount
                    </label>
                    <input name="amount" value={orderData.amount} onChange={handleChange} type="number" className="form-control" id="amount" aria-describedby="amount"/>
                </div>
                <button className='btn btn-success' type="submit">Submit</button>
            </form>
        </div>
    </div>
  )
}

export default AddOrder
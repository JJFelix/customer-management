import { useEffect, useState } from 'react'
import './App.css'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Home from './assets/pages/Home'
import Navbar from './assets/components/Navbar'
import Customers from './assets/pages/Customers'
import Orders from './assets/pages/Orders'
import Login from './assets/pages/Login'
import AddCustomer from './assets/pages/AddCustomer'
import CustomerOrder from './assets/pages/CustomerOrder'
import AddOrder from './assets/pages/AddOrder'
import axios from 'axios'
import Logout from './assets/pages/Logout'

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [loading, setLoading] = useState(true)

  // const navigate = useNavigate()

  const checkLoginStatus = async () =>{
    try {
      // const response = await fetch("http://localhost:8000/api/is_logged_in", {
      //   method: "GET",
      //   credentials: "include",
      // })
      const response = await axios.get("http://localhost:8000/api/is_logged_in",{
        withCredentials: true,
      })
      // const data = await response.json()

      if(response.data.logged_in){
        setIsAuthenticated(true)
      }else{
        setIsAuthenticated(false)
      }
    } catch (error) {
      console.error("Error checking login status:", error);      
    }finally{
      setLoading(false)
    }
  }

  useEffect(()=>{
    checkLoginStatus()
  }, [])

  if(loading){
    return <div>Loading...<i className="fa fa-spinner" aria-hidden="true"></i></div>
  }

  // if(!isAuthenticated){
  //   // navigate('/login')
  //   return <Navigate to="/login" />
  // }

  return (
    <>
      <main>
        <BrowserRouter>
          <Navbar />
          <Routes>
            <Route path='/' element={<Home />} />
            {/* element={isAuthenticated ? <Home /> : <Navigate to="/login" />} /> */}
            <Route path='/customers' element={<Customers />} />
            <Route path='/customers/:customer_id' element={<CustomerOrder />} />
            <Route path='/add_customer' element={<AddCustomer />} />
            <Route path='/orders' element={<Orders />} />
            <Route path='/add_order' element={<AddOrder />} />

            <Route path='/login' element={<Login />}/>
            <Route path='/logout' element={<Logout />}/>

          </Routes>
        </BrowserRouter>
      </main>
    </>
  )
}

export default App

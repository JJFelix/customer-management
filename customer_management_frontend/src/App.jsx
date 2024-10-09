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

export const backend_url = 'https://customer-management-api-grx3.onrender.com'
// export const backend_url = 'http://localhost:8000'

export const dateTime = (e) =>{
  const date = new Date(e)
  const formatedDate = date.toLocaleDateString()
  const formatedTime = date.toLocaleTimeString()

  return formatedDate +" at "+ formatedTime
}
function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [loading, setLoading] = useState(true)

  // const navigate = useNavigate()
  useEffect(()=>{
    console.log("checkLoginStatus");
    
    checkLoginStatus()
  }, [])

  const checkLoginStatus = async () =>{
    try {
       const response = await axios.get(`${backend_url}/api/is_logged_in`,{
        withCredentials: true,
      })
      console.log("response.data", response.data)      

      if(response.data.logged_in){
        console.log("Logged in")        
        setIsAuthenticated(true)
      }else{
        setIsAuthenticated(false)
      }
    } catch (error) {
      if(error.response && error.response.status == 401){
        console.log("User not authenticated", error.response.data)
        setIsAuthenticated(false)        
      } else{
        console.error("Error checking login status:", error)
      }
    }finally{
      setLoading(false)
    }
  }
 

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
            <Route path='/' element={isAuthenticated ? <Home /> : <Navigate to="/login" />} />
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

import React from 'react'
import { Link } from "react-router-dom";
import "../styles/Navbar.css";

const Navbar = () => {
  return (
    <div>
      <nav className="nav">
        <div className="name-logo">
          Customer Management
        </div>

        <div className="below-500">
          <ul className="nav-list">
            <Link to={"/"} className="nav-links ">
              Home
            </Link>
            {/* {userName && ( */}
              <Link to={"/customers"} className="nav-links">
                Customers
              </Link>
            {/* )} */}
            <Link to={"/orders"} className="nav-links">
                Orders
            </Link>
          </ul>

          <>
            {/* {!userName && ( */}
              {/* <div className="auth-list">
                <Link to={"/register"} className="auth-links">
                  Register
                </Link>
                <Link to={"/login"} className="auth-links">
                  Login
                </Link>
              </div> */}
            {/* // )} */}
            {/* {userName && ( */}
              <div className="auth-list">
                <Link
                  to={"/logout"}
                //   onClick={handleLogout}
                  className="auth-links"
                >
                  Logout
                </Link>
              </div>
            {/* )} */}
          </>
        </div>
      </nav>
    </div>
  )
}

export default Navbar
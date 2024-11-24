import React, { useEffect, useState } from 'react'

import FormPage from './modules/form/index.jsx'
import LoginPage from './modules/login/index.jsx'
import MenuBar from './modules/menu-bar/index.jsx'
import Snackbar from '@mui/material/Snackbar';

import cookie from './utils/cookie.js'

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [toasterOpen, setToasterOpen] = useState({ open: false, msg: '' })

  useEffect(() => {
    const authCookie = cookie.getCookie("authToken")
    if (authCookie) setIsLoggedIn(authCookie)
  }, [])

  return (
    <>
      <MenuBar setIsModalOpen={setIsModalOpen} isLoggedIn={isLoggedIn} />
      <FormPage setToasterOpen={setToasterOpen} />
      {isModalOpen && <LoginPage 
        isModalOpen={isModalOpen} 
        setIsModalOpen={setIsModalOpen} 
        setIsLoggedIn={setIsLoggedIn} 
        setToasterOpen={setToasterOpen}
      />}
      <Snackbar
        anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
        open={toasterOpen.open}
        onClose={() => {
          setToasterOpen({ open: false, msg: '' });
        }}
        message={toasterOpen.msg}
      />
    </>
  )
}

export default App

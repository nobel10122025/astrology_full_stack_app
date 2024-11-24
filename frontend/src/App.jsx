import React, { useEffect, useState } from 'react'

import FormPage from './modules/form/index.jsx'
import LoginPage from './modules/login/index.jsx'
import MenuBar from './modules/menu-bar/index.jsx'

import cookie from './utils/cookie.js'

function App() {
  const [isModalOpen ,setIsModalOpen] = useState(false)
  const [isLoggedIn, setIsLoggedIn] = useState(false)

  useEffect(() => {
    const authCookie = cookie.getCookie("authToken")
    if (authCookie) setIsLoggedIn(authCookie)
  }, [])

  return (
    <>
      <MenuBar setIsModalOpen={setIsModalOpen} isLoggedIn={isLoggedIn} />
     <FormPage />
     {isModalOpen && <LoginPage isModalOpen={isModalOpen} setIsModalOpen={setIsModalOpen} setIsLoggedIn={setIsLoggedIn} />}
    </>
  )
}

export default App

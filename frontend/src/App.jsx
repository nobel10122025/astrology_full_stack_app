import { useState } from 'react'
import FormPage from './modules/form/index.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <FormPage />
    </>
  )
}

export default App

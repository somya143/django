import './App.css';
import axios from 'axios';
import React, {useState, useEffect} from 'react';

function App() {

  const [message,setMessage] = useState("");

  useEffect(() =>{
    axios.get('http://localhost:8000/api/index').then((res) => {
      setMessage(res.data.message)
      console.log(res.data.message)
    }).catch((err) => {
      console.log(err.message)
    })
  },[])

  return (
    <div className="App">
      {message}
    </div>
  );
}

export default App;

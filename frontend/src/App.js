import "./App.css"
import { useState } from "react";
import SubmitForm from "./components/SubmitForm";
import { BrowserRouter as Router, Route} from 'react-router-dom'
import { Redirect } from "react-router";
import Dashboard from "./components/Dashboard";
import Login from "./components/Login"
import Landing from "./components/Landing"
import axios from "axios";

function App() {

  const [user, setUser] = useState([])

  const checkIfLoggedIn = () => {
    let loggedIn = false

    //Add login Logic

    return loggedIn
  }

  

  const requestLogin = async (username, password) => {
    const data = JSON.stringify({username: username, password: password})
    let result = await axios.post("http://localhost:3000/api/login/", data)
    console.log(result)
    if (result.status === "success"){
      return true
    }
    return false
  }


  return (
    <Router>
      <div className="App">
        <Route path="/" exact component={Landing}/>
        <Route path="/dashboard" exact render={(props) => checkIfLoggedIn() === false ? 
        <Dashboard/> : <Redirect to={{pathname: "/login", state : {from: props.location}}}/>} />
        <Route path="/login" render={(props) => (<Login loginRequest={requestLogin}/>)} />
      </div>
    </Router>
  );
}

export default App;

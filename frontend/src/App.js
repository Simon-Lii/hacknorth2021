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
    let data = new FormData();
    data.append('username', username);
    data.append('password', password);
    let result = await axios.post("http://localhost:3000/api/login/", data)
    .then((result) => {return result})
    .catch((result) => { return result })
  }

  //TODO Login route needs logged in checking, add at the end when when we want to test our app
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

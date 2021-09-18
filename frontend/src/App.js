import "./App.css"
import { useState } from "react";
import SubmitForm from "./components/SubmitForm";
import { BrowserRouter as Router, Route} from 'react-router-dom'

function App() {

  const [fileUploaded, setFileUploaded] = useState(0);

  const [fileName, setFileName] = useState("");


  return (
    <Router>
      <div className="App">
        <Route path="/"  exact render={(props) => (
          <>
            <SubmitForm/>
          </>
        )}/>
      </div>
    </Router>
  );
}

export default App;

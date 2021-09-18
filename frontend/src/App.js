import "./App.css"
import { useState } from "react";
import SubmitForm from "./components/SubmitForm";

function App() {

  const [fileUploaded, setFileUploaded] = useState(0);

  const [fileName, setFileName] = useState("");

  return (
    <div className="App">
      <header className="App-header">
        <SubmitForm/>
      </header>
    </div>
  );
}

export default App;

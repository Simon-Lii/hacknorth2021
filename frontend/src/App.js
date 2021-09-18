import logo from './logo.svg';
import './App.css';
import Button from "./components/Button.js"
import FileUpload from './components/FileUpload';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <FileUpload/>
        <Button/>
      </header>
    </div>
  );
}

export default App;

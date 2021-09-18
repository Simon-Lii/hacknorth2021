import React, {useState} from 'react'
import axios from 'axios'
import SubmitForm from './SubmitForm'
import "../styles/dashboard.css"


const Dashboard = () => {
	const [fileUploaded, setFileUploaded] = useState(0);
	const [file, setFile] = useState(0);

	const handleSubmit = (e) => {
		e.preventDefault();
		console.log(file)
		const data = new FormData();
		data.append('file', file);
		axios.post('http://localhost:3000/api/upload', data)
		.then((result) => console.log(result))
		.catch((result) => console.log(result))
		setFileUploaded(0);
	}

	
	

	return (
		<div id="dashboard-container">
			<nav class="navbar navbar-expand-lg navbar-light bg-light">
				<div class="container-fluid">
					<a class="navbar-brand" href="#">Navbar</a>
					<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
					</button>
					<button class="btn btn-outline-primary">Sign Out</button>
				</div>
			</nav>
			<div id="upload-container" className="card">
				<SubmitForm handleSubmit={handleSubmit} setFile={setFile}/>
				{fileUploaded ? <p>file.name</p> : <p></p>}
			</div>
		</div>
	)
}

export default Dashboard

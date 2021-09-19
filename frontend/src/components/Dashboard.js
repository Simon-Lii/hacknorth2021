import React, {useEffect, useState} from 'react'
import axios from 'axios'
import SubmitForm from './SubmitForm'
import "../styles/dashboard.css"
import Scores from './Scores.js'


const Dashboard = ({user}) => {
	const [fileUploaded, setFileUploaded] = useState(0);
	const [file, setFile] = useState(0);
	const [scores, setScores] = useState([]);

	useEffect(() => {
		const getScores = async () => {
			const scoresFromServer = await getScoreHistory();
			setScores(scoresFromServer)
		}

		getScores()
	},[])

	const handleSubmit = (e) => {
		e.preventDefault()
		console.log(file)
		const data = new FormData()
		data.append('file', file)
		data.append('username', user)
		console.log(user)
		axios.post('http://localhost:3000/api/upload', data)
		.then((result) => {window.location.replace(result.data.filename); window.location.reload()})
		.catch((result) => console.log(result))
		setFileUploaded(0);
	}

	const signOut = () => {
		axios.get('http://localhost:3000/api/sign_out').then().catch()
		window.location.href = "../"
	}

	const getScoreHistory = async () => {
		const res = await fetch('http://localhost:3000/api/history');
		const data = await res.json();
		return data.body
	}
	

	return (
		<div id="dashboard-container" >
			<nav class="navbar navbar-expand-lg navbar-dark bg-dark py-4">
				<div class="container-fluid">
					<h4 class="display-5 titler"> Score.me</h4>
					<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
					</button>
					<h3 id="header1"className="display-4 my-scores-title"> My Scores </h3>
					<button class="btn btn-outline-info" onClick={signOut}>Sign Out</button>
				</div>
			</nav>
			<div id="main-content">
				<div id="upload-container" className="card">
					<h3 id = "upload1" className="display-6 upload-title"> Upload </h3>
					<div className="alert alert-warning"> To get your music score, upload your .wav file by clicking upload and after
					you finish uploading, press "Get my score".</div>
					<SubmitForm handleSubmit={handleSubmit} setFile={setFile} file={file}/>
				</div>
					<div id="history-container">
						<div id="background-dash">
						 <Scores scores={scores} style={{backgroundColor:"blue"}}/>
					</div></div>
					<div id="upload-container" className="card">
					<h3 id = "upload1" className="display-6 upload-title"> Upload </h3>
					<div className="alert alert-warning"> To get your music score, upload your .wav file by clicking upload and after
					you finish uploading, press "Get my score".</div>
					<SubmitForm handleSubmit={handleSubmit} setFile={setFile} file={file}/>
				</div>
			</div>
		</div>
	)
}

export default Dashboard

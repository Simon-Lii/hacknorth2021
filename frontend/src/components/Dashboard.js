import React, {useState} from 'react'
import axios from 'axios'
import SubmitForm from './SubmitForm'
import "../styles/dashboard.css"
import Score from './Score'


const Dashboard = ({user}) => {
	const [fileUploaded, setFileUploaded] = useState(0);
	const [file, setFile] = useState(0);

	const handleSubmit = (e) => {
		e.preventDefault();
		console.log(file)
		const data = new FormData();
		data.append('file', file);
		data.append('username', user)
		axios.post('http://localhost:3000/api/upload', data)
		.then((result) => console.log(result))
		.catch((result) => console.log(result))
		setFileUploaded(0);
	}

	const signOut = async (e) => {
		e.preventDefault();
		const data = new FormData();
		//TODO finish once api is done
	}
	

	return (
		<div id="dashboard-container" >
			<nav class="navbar navbar-expand-lg navbar-light bg-light">
				<div class="container-fluid">
					<a class="navbar-brand " href="#">Score.me</a>
					<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
					</button>
					<button class="btn btn-outline-primary">Sign Out</button>
				</div>
			</nav>
			<div id="main-content">
				<div id="upload-container" className="card">
					<h3 className="display-6 upload-title"> Upload </h3>
					<div className="alert alert-warning"> To get your music score, upload your .wav file by clicking upload and after
					you finish uploading, press "Get my score".</div>
					<SubmitForm handleSubmit={handleSubmit} setFile={setFile} file={file}/>
				</div>
				<div id="history-container">
					<h3 className="display-4 my-scores-title"> &#127925; My Scores </h3>
					<hr></hr>
					<Score score={{title: "mii_song_very_simple.mp3", url:"score.me/api/download/ae5Uys9p"}}/>
					<Score score={{title: "flight_of_bumblebee.wav", url:"score.me/api/download/kqos012nN"}}/>
				</div>
			</div>
		</div>
	)
}

export default Dashboard

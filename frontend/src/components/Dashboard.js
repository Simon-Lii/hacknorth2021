import React, {useState} from 'react'
import axios from 'axios'
import SubmitForm from './SubmitForm'


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
			fileUploaded ? <p>Uploaded</p> : <SubmitForm handleSubmit={handleSubmit} setFile={setFile}/>
	)
}

export default Dashboard

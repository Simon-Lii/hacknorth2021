import React from 'react'
import "../styles/submitform.css"

const SubmitForm = ({handleSubmit, setFile, file}) => {

	const changeHandler = (event) => {
		setFile(event.target.files[0]);
		document.getElementById("uploaded-file-name").textContent = event.target.files[0].name 
	}

	return (
		<>
			<form onSubmit={handleSubmit}>
				<div type="button" className="fileUpload btn btn-outline-primary">
					<span>Upload</span>
					<input type="file" name="file" onChange={changeHandler} className="upload" />
				</div>
				<input className="btn btn-rounded btn-outline-primary" type="submit" value="Get my Score" />
			</form>
			<p id="uploaded-file-name"></p>
		</>
	)
}

export default SubmitForm

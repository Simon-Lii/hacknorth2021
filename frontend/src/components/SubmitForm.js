import React from 'react'
import "../styles/submitform.css"

const SubmitForm = ({handleSubmit}) => {
	return (
		<form onSubmit={() => handleSubmit()}>
			<div className="fileUpload btn btn-outline-primary">
				<span>Upload</span>
				<input type="file" className="upload" />
			</div>
			<input className="btn btn-rounded btn-outline-primary" type="submit" value="Get my Score" />
		</form>
	)
}

export default SubmitForm

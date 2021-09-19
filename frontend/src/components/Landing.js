import React from 'react'
import "../styles/landing.css"
import score0 from "../img/score_0.png"
import bronto from "../img/bronto.png"

const Landing = () => {
	return (
		<div id="landing" className="container-fluid">
			<div id="landing-background">
			</div>
			<div id="content" className="container-fluid"></div>
			<h3 className="display-1 title"> &#127932; Score.me</h3>
			<h5 className="display-6 motto">Scores generated right at your fingertips</h5>
			<a className="btn btn-outline-info btn-lg" href="/login" id="login-btn">Login</a> 
			<a className="btn btn-outline-warning btn-lg" href="/create_user" id="create-btn">Create an account</a>
			<img id="rick-1" src={score0} alt="Rick and Morty Score" />
			<img id="rick-2" src={score0} alt="Rick and Morty Score" />
			<img id="rick" src={score0} alt="Rick and Morty Score" />
			<img id="bonto" src={bronto} alt="Rick and Morty Score" />
			<div id="blocker"></div>
			<hr id="blocker-1"></hr>
		</div>
	)
}

export default Landing
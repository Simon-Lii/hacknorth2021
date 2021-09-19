import React from 'react'
import "../styles/landing.css"

const Landing = () => {
	return (
		<div id="landing">
			<nav className="navbar navbar-expand-lg shadow-5-strong landing-bar">
				<div className="container-fluid">
				<h3 className="display-5">Score.me</h3>
				</div>
			</nav>
			<div id="landing-background"></div>
		</div>
	)
}

export default Landing
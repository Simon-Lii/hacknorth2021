import React from 'react'
import "../styles/score.css"

const Score = ({score}) => {
	return (
		<div className="card score" id="card1">
			<div className="grow">
			<div className="card-body">
				<a id = "title1" className="score-link lead" href={score.url}>{score.title}</a>
			</div>
			</div>
		</div>
	)
}

export default Score

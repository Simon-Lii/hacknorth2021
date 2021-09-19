import React from 'react'
import "../styles/score.css"

const Score = ({score}) => {
	return (
		<div className="card score">
			<div className="card-body">
				<h3 className=" score-title">{score.title}</h3>
				<a className="score-link lead" href={score.url}>Ligma</a>
			</div>
		</div>
	)
}

export default Score

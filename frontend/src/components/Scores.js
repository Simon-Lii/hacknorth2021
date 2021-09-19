import React from 'react'
import Score from './Score'

const Scores = ({scores}) => {
	return (
		<div id="scores">
			{scores.map((score) => (
				<Score score={score} style={{backgroundColor:"blue"}}/>
			))}
		</div>
	)
}

export default Scores

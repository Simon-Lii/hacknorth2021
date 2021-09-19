import React from 'react'
import Score from './Score'

const Scores = ({scores}) => {
	return (
		<div id="scores">
			{scores.map((score) => (
				<Score score={score}/>
			))}
		</div>
	)
}

export default Scores

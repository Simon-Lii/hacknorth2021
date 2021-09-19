import React from 'react'
import Score from './Score'

const Scores = ({scores}) => {
	return (
		<div>
			{scores.map((score) => (
				<Score score={score}/>
			))}
		</div>
	)
}

export default Scores

import React from 'react'
import "../styles/login.css"



const Login = () => {
	return (
		<div id="login">
			<div id="background">
			</div>
			<div className="card">
				<form>
					<div class="mb-2">
						<label for="username" class="form-label">Username</label>
						<input type="email" class="form-control" id="username" />
					</div>
					<div class="mb-3">
						<label for="password" class="form-label">Password</label>
						<input type="password" class="form-control" id="password" />
					</div>
					<button type="submit" class="btn btn-outline-warning">Login</button>
				</form>
			</div>
		</div>
	)
}

export default Login

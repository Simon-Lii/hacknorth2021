import React from 'react'
import "../styles/login.css"



const Login = ({loginRequest}) => {
	
	const handleLogin = (event) => {
		event.preventDefault()
		const result = loginRequest(event.target[0].value, event.target[1].value)
			if(result.status != "success"){
			const loginErrorMsgBox = document.getElementById("login-error")
			loginErrorMsgBox.textContent = "Username and Password not detected. Please try again or make a new account"
			loginErrorMsgBox.removeAttribute("hidden")
		}
	}

	return (
		<div id="login">
			<div id="background">
			</div>
			<div className="card login-box">
				<div class="alert alert-danger" role="alert" id="login-error" hidden>
				</div>
				<form onSubmit={handleLogin}>
					<div class="mb-2">
						<label for="username" class="form-label">Username</label>
						<input type="username" class="form-control" id="username" />
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

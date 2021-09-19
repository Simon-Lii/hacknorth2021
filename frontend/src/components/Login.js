import React from 'react'
import "../styles/login.css"



const Login = ({loginRequest}) => {
	
	const handleLogin = (event) => {
		event.preventDefault()
		loginRequest(event.target[0].value, event.target[1].value).then((result) => {
			console.log(result)
			if(result !== 200){
				const loginErrorMsgBox = document.getElementById("login-error")
				loginErrorMsgBox.textContent = "Username and Password not detected. Please try again or make a new account"
				loginErrorMsgBox.removeAttribute("hidden")
			}
			else{
				window.location.href = "dashboard"
			}
		})
	}

	return (
		<div id="login">
			<div id="background">
			</div>
			<div className="card login-box">
				<div className="alert alert-danger" role="alert" id="login-error" hidden>
				</div>
				<form onSubmit={handleLogin}>
					<div className="mb-2">
						<label for="username" className="form-label">Username</label>
						<input type="username" className="form-control" id="username" />
					</div>
					<div className="mb-3">
						<label for="password" className="form-label">Password</label>
						<input type="password" className="form-control" id="password" />
					</div>
					<button type="submit" className="btn btn-outline-warning">Login</button>
				</form>
				<a className="card-link" href="/create_user">Create an account</a>
			</div>
		</div>
	)
}

export default Login

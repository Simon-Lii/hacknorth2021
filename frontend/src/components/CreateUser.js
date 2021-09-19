import React from "react";
import "../styles/login.css";

const CreateUser = ({ createUserRequest }) => {
  const handleCreateUser = (event) => {
    event.preventDefault();
    createUserRequest(event.target[0].value, event.target[1].value).then(
      (response) => {
        if (response !== 200) {
          const loginErrorMsgBox = document.getElementById("createUserError");
          loginErrorMsgBox.textContent =
            "This username already exists, please choose a new one.";
          loginErrorMsgBox.removeAttribute("hidden");
        } else {
          window.location.replace("http://localhost:3000/login");
        }
      }
    );
  };

  return (
    <div id="createUser">
      <div id="background"></div>
      <div className="card login-box">
        <div class="alert alert-danger" role="alert" id="createUserError" hidden></div>
        <form onSubmit={handleCreateUser}>
          <div className="mb-2">
            <label for="username" className="form-label">
              Username
            </label>
            <input type="username" className="form-control" id="username" />
          </div>
          <div className="mb-3">
            <label for="password" className="form-label">
              Password
            </label>
            <input type="password" className="form-control" id="password" />
          </div>
          <button type="submit" className="btn btn-outline-success">
            Create user
          </button>
        </form>
				<a className="card-link" href="/login">Login to an account</a>
      </div>
    </div>
  );
};

export default CreateUser;

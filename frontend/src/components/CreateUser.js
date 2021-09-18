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
      <div className="card">
        <form onSubmit={handleCreateUser}>
          <div class="mb-2">
            <label for="username" class="form-label">
              Username
            </label>
            <input type="username" class="form-control" id="username" />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">
              Password
            </label>
            <input type="password" class="form-control" id="password" />
          </div>
          <button type="submit" class="btn btn-outline-warning">
            Create user
          </button>
        </form>

        <div
          class="alert alert-danger"
          role="alert"
          id="createUserError"
          hidden
        ></div>
      </div>
    </div>
  );
};

export default CreateUser;

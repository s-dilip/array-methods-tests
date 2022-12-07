import { useState } from "react";
import { fields } from "../defaultUser.js";

export default function EditProfile(props) {
	let [isFormVisible, setIsFormVisible] = useState(false);
	let [username, setUsername] = useState("");
	let [displayName, setDisplayName] = useState("");

	function handleFormSubmit(event) {
		// TO DO
	}

	function handleUserNameChange(e) {
		// TO DO
	}

	function handleDisplayNameChange(e) {
		// TO DO
	}

	function toggleProfileEdit(e) {
		const visibility = !isFormVisible;
		setIsFormVisible(visibility);
	}

	function createFormField(key) {
		return (
			<div key={`${key}Input`}>
				<label>{fields[key]}</label>
				<input
					className="profileEditFields"
					name={key}
					type="text"
					onChange={
						key === "username" ? handleUserNameChange : handleDisplayNameChange
					}
				/>
				<br />
			</div>
		);
	}
	function displayForm() {
		return (
			<div id="editProfileWrapper">
				<form id="editProfileForm" onSubmit={handleFormSubmit}>
					{() => {
						createFormField("username");
						createFormField("displayName");
					}}
					<button type="submit">Update Details</button>
				</form>
			</div>
		);
	}

	return (
		<div id="editProfile">
			<button onClick={toggleProfileEdit}>Edit Profile</button>
			{isFormVisible ? displayForm() : ""}
		</div>
	);
}

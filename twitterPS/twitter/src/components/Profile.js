import React from "react";
import EditProfile from "./EditProfile";

export default function Profile(props) {
	return (
		<div className="profileWrapper">
			<div className="profileInfo">
				<div id="profilePicture">
					<img alt="profile" src={props.info.profilePictureURL}></img>
				</div>
				<div id="info">
					<h1>
						{props.info.firstName} {props.info.lastName}
					</h1>
					<h2>@{props.info.username}</h2>
					<p>{props.info.bio}</p>
				</div>
			</div>
			<EditProfile
				handleUserInfoChange={props.handleUserInfoChange}
				info={props.info}
			/>
		</div>
	);
}

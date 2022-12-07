export default function TweetsList(props) {
	return (
		<div className="tweetsListWrapper">
			{props.tweets.map((tweet, i) => (
				<Tweet key={i} tweet={tweet} userInfo={props.userInfo} />
			))}
		</div>
	);
}

function Tweet(props) {
	return (
		<div className="tweet">
			<div className="tweetUserInfo">
				<img
					className="tweetProfilePicture"
					src={props.userInfo.profilePictureURL}
					alt="user"
				/>
				<div className="tweetNames">
					<h1 className="tweetDisplayUserName">{props.userInfo.firstName}</h1>
					<h2 className="tweetDisplayName">{`@${props.userInfo.username}`}</h2>
				</div>
				<p className="tweetContent">{props.tweet}</p>
			</div>
		</div>
	);
}

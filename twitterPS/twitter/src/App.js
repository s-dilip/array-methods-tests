import "./App.css";
import Profile from "./components/Profile";
import TweetsList from "./components/TweetsList";
import { useState } from "react";
import { defaultUserInfo } from "./defaultUser.js";
import AddTweet from "./components/AddTweet";

export default function App() {
  let [tweets, setTweets] = useState([]);
  let [currentUserInfo, setCurrentUserInfo] = useState({ ...defaultUserInfo });

  function handleUserInfoChange(userInfo) {}

  function addTweetToList(tweetMessage) {
    const updatedTweets = [tweetMessage, [...tweets]];
    setTweets(updatedTweets);
  }

  return (
    <div className="bodyWrapper">
      <Profile
        info={currentUserInfo}
        handleUserInfoChange={handleUserInfoChange}
      />
      <div className="rhs">
        <AddTweet addTweetToList={addTweetToList} />
        <TweetsList userInfo={currentUserInfo} tweets={tweets} />
      </div>
    </div>
  );
}

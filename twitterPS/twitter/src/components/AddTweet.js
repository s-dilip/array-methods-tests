import { useState } from "react";
export default function AddTweet(props) {
  const [tweetInput, setTweetInput] = useState("");

  function handleTweetInput(e) {
    setTweetInput(e.target.value);
  }

  function handleAddTweet(e) {
    props.addTweetToList(tweetInput);
  }
  return (
    <div className="createTweet">
      <div className="tweetInputFields">
        <input
          onChange={handleTweetInput}
          type="textarea"
          className="tweetInput"
          cols={5}
        />
        <button id="tweetButton" onClick={handleAddTweet}>
          Tweet
        </button>
      </div>
    </div>
  );
}

import React, { useState, useEffect } from "react";
import { InlineShareButtons } from "sharethis-reactjs";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import "./LandingPage.css"

const SearchAddress = () => {
  const [address, setAddress] = useState("");

  const handleSubmit = (event) => {
    console.log("yay");
  };

//   const makeApiCall = () => {
//     // fetch(
//     //   //need some api to search addresses
//     //   //or will search through the addresses we already have on file
//     // )
//     //   .then((res) => res.json())
//     //   .then((data) => {
//     //     //do something with the address
//     //   });
//   };

  const handleChange = (event) => {
    event.preventDefault();
    if (event.target.type === "text") {
      setAddress(event.target.value)
      console.log(address);
    }
  };

//   useEffect(() => {
//     makeApiCall();
//   }, [address]);

  return (
    <div id="searchaddress">
        <input
          // onChange={handleEmailChange}
          onChange={handleChange}
          value={address}
          type="text"
          className="form-control"
          name="address"
          placeholder="&#xf002; Search your Address"
        />
        <p className="searchtext">Discover the likelihood of lead pipes.</p>
    </div>
  );
};

export default SearchAddress;

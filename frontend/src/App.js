import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from "react";

function NavBar(){
  return(<>
  <ul>
  <li><a href="default.asp">Home</a></li>
  <li><a href="news.asp">News</a></li>
  <li><a href="contact.asp">Contact</a></li>
  <li><a href="about.asp">About</a></li>
</ul></>);
}

function App() {
  const [data, setdata] = useState({
    name: "",
    age: 0,
    date: "",
    programming: "",
});
useEffect(() => {
  // Using fetch to fetch the api from 
  // flask server it will be redirected to proxy
  fetch("/data").then((res) =>
      res.json().then((data) => {
          // Setting a data from api
          setdata({
              name: data.Name,
              age: data.Age,
              date: data.Date,
              programming: data.programming,
          });
      })
  );
}, []);
  return (
    <>
    <NavBar/>
    <div class="container">
	   <div class="column">
	     <h2> User's current stats </h2>
		 <p> money</p>
     <p> stocks they hold</p>
	   </div>
	   <div class="column">
	     <h2> visualizations for stocks </h2>
		 <p>general stock info</p>
     <p>info from our model</p>
	   </div>
	   <div class="column">
      <h2>Displaying Data from Python Flask backend</h2>
     <p>{data.name}</p>
                <p>{data.age}</p>
                <p>{data.date}</p>
                <p>{data.programming}</p>
	   </div>
	</div>
  </>
  );
}

export default App;

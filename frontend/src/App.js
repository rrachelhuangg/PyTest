import logo from './logo.svg';
import './App.css';
import { useState } from "react";
import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
//can read .csv file data and display it on the page: if we write data that we collect from the api to a csv
//file, we will be able to use it in react 

function TickerDisplay(){
  return(<>
  <div className = "tickerContainer">
  <img src = "./testgraph.png" className = "images"/>
    <button>Buy</button>
    <button>Sell</button></div></>
    );
}

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
  const [ text, setText ] = useState();

    fetch( './constituents.csv' )
        .then( response => response.text() )
        .then( responseText => {
            setText(responseText.slice(0, 100));
        })

  return (
    <>
    <NavBar/>
    <div class="container">
  <div class="column">
    <h2> User's current stats </h2>
  <p> money</p>
  <p> stocks they hold</p>
  </div>
  <div class="column" style={{ height: '100vh', overflow: 'scroll' }}>
    <h2> visualizations for stocks </h2>
    <TickerDisplay/>
    <TickerDisplay/>
    <TickerDisplay/>

  </div>
  <div class="column">
    <h2> other info </h2>
    <pre>{ text }</pre>
  </div>
</div>
  </>
  );
}

export default App;
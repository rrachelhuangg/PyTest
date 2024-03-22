import logo from './logo.svg';
import './App.css';

function NavBar(){
  return(<>
  <ul>
  <li><a href="default.asp">Home</a></li>
  <li><a href="news.asp">News</a></li>
  <li><a href="contact.asp">Contact</a></li>
  <li><a href="about.asp">About</a></li>
</ul></>);
}

function Content(){
  return (<><div class="container">
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
    <h2> other info </h2>
  <p> ---</p>
  </div>
</div></>);
}

function App() {
  return (
    <>
    <NavBar/>
    <Content/>
  </>
  );
}

export default App;

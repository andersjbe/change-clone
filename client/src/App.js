import React, { useEffect } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import Footer from './components/Footer'
import Home from "./components/Home"
import Search from "./components/Search"
import UpdateForm from "./components/UpdateForm"
import UpdatesBox from "./components/UpdatesBox"
import UpdateCard from "./components/UpdateCard"
import StartPetition from "./components/StartPetition"
import MyPetitions from "./components/MyPetitions"
import Petitions from "./components/Petitions"
import SettingsPage from "./components/SettingsPage"
import PetitionDetails from './components/PetitionDetails';
import { fetchUserDetails } from './store/auth'
import Navbar from './components/Navbar'

function App() {
  const token = localStorage.getItem("SESSION_TOKEN");
  const id = localStorage.getItem("USER_ID");
  const dispatch = useDispatch();

  useEffect(() => {
    if (token && id) {
      dispatch(fetchUserDetails(token, id))
    }
  })

  return (
    <>
      <BrowserRouter>
        <Navbar />
        <Switch >
          <Route
            exact path="/"
            component={Home}
          />
          <Route
            path="/start-a-petition"
            component={StartPetition} />
          <Route
            path="/u/me"
            component={MyPetitions} />
          <Route
            path="/petitions"
            component={Petitions} />
          <Route
            exact path="/p/:header"
            component={PetitionDetails} />
          <Route
            path="/search"
            component={Search} />
          <Route
            path="/settings"
            component={SettingsPage} />
          <Route
            path="/p/:name/updateform"
            component={UpdateForm} />
          <Route
            path="/:name/updates"
            component={UpdatesBox} />
          <Route 
          path="/:name/update/:id"
          component={UpdateCard} />
        </Switch>
        <Footer />
      </BrowserRouter>
    </>
  );
}

export default App;

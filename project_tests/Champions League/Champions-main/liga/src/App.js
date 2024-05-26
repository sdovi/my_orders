import { Route, Routes } from 'react-router-dom';
import Footbalnews from './Pages/Footbalnews';
import Basketnews from './Pages/Basketnews';
import Hokeynews from './Pages/Hokeynews';
import Schedule from './Pages/Schedule';
import MatchDetails from './Pages/MatchDetails ';
import Tablelig from './Pages/Tablelig';
import Ligainfo from './Pages/Ligainfo';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/games/:id" element={<MatchDetails/>} />
        <Route path='/' element={<Footbalnews />} />
        <Route path='/Basket' element={<Basketnews />} />
        <Route path='/hokey' element={<Hokeynews />} />
        <Route path='/ligaforms' element={<Schedule />} />
        <Route path='/table' element={<Tablelig/>} />
        <Route path='/table' element={<Tablelig/>} />
        <Route path="/table/:id" element={<Ligainfo/>} />
      </Routes>
    </div>
  );
}

export default App;

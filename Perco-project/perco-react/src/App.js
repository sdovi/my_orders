
import { Route, Routes } from 'react-router-dom'
import Main_page from './Pages/Main_page'
import Article_page from './Pages/Article_page';
import Article from './components/Section_Article/Article';
import Article_n2 from './components/Section_Article/Article_n2';
import Article_n3 from './components/Section_Article/Article_n3';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route  path='/' element={<Main_page/>} />
        <Route  path='/article' element={<Article_page/>} />
        <Route  path='/article_n1' element={<Article/>} />
        <Route  path='/article_n2' element={<Article_n2/>} />
        <Route  path='/article_n3' element={<Article_n3/>} />

      </Routes>
    </div>
  );
}

export default App;

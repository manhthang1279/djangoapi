import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Home from './pages/home/Home';
import Bookslist from './pages/library/bookslist/Bookslist';
import Take from './pages/library/take/Take';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path='library/'>
            <Route index element={<Bookslist />} />
            <Route path='take/' element={<Take />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

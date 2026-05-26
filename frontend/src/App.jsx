import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Navbar from "./components/Navbar";

import Dashboard from "./pages/Dashboard";

import History from "./pages/History";

function App() {

  return (

    <BrowserRouter>

      <div className="min-h-screen bg-slate-900 text-white">

        <Navbar />

        <div className="p-8">

          <Routes>

            <Route
              path="/"
              element={<Dashboard />}
            />

            <Route
              path="/history"
              element={<History />}
            />

          </Routes>

        </div>

      </div>

    </BrowserRouter>

  );
}

export default App;
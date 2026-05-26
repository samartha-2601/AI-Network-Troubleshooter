import { Link } from "react-router-dom";

function Navbar() {

  return (

    <nav className="bg-slate-800 p-4">

      <div className="flex gap-6">

        <Link
          to="/"
          className="font-semibold hover:text-blue-400"
        >
          Dashboard
        </Link>

        <Link
          to="/history"
          className="font-semibold hover:text-blue-400"
        >
          Analysis History
        </Link>

      </div>

    </nav>
  );
}

export default Navbar;
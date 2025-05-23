import { Link } from "react-router-dom";

export const Navbar = () => {

	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">Home</span>
				</Link>
				<div className="ml-auto">
					<Link to="/signup" className="me-2">
						<button className="btn btn-primary">Sign Up</button>
					</Link>
					<Link to="/login" className="me-2">
						<button className="btn btn-primary">Log In</button>
					</Link>
				</div>
			</div>
		</nav>
	);
};
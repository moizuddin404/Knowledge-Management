import { googleLogout } from "@react-oauth/google";

function Logout() {
    const handleLogout = () => {
        googleLogout();  // Logs the user out
        localStorage.removeItem("token");  // Clear token
        window.location.href = "/";  // Redirect to login page
    };

    return (
        <button onClick={handleLogout} className="logout-button">
            Logout
        </button>
    );
}

export default Logout;

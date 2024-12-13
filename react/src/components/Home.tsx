// react/src/components/Home.tsx
import {Link} from "react-router-dom";

const Home = () => {
    return (
        <div>
            <h1>Home</h1>
            <nav>
                <ul>
                    <li><Link to="/client-form">Client Form</Link></li>
                    <li><Link to="/realtor-form">Realtor Form</Link></li>
                    <li><Link to="/fuzzy-search">Fuzzy Search</Link></li>
                    <li><Link to="/property-form">Property Form</Link></li>
                    <li><Link to="/property-search">Property Search</Link></li>
                    <li><Link to="/offer-form">Offer Form</Link></li>
                    <li><Link to="/need-form">Need Form</Link></li>
                    <li><Link to="/client-needs">Client Needs</Link></li>
                    <li><Link to="/client-offers">Client Offers</Link></li>
                    <li><Link to="/realtor-needs">Realtor Needs</Link></li>
                    <li><Link to="/realtor-offers">Realtor Offers</Link></li>
                    <li><Link to="/client-realtor-management">Client and Realtor Management</Link></li>
                    <li><Link to="/deal-form">Deal Form</Link></li>
                </ul>
            </nav>
        </div>
    );
};

export default Home;
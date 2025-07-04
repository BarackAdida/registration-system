import { useEffect, useState } from "react"
import "./styles.css";



function SavedList() {
    const [names, setNames] = useState([]);

    useEffect(() => {
        fetch("http://localhost:5000/save")
        .then((res) => res.json())
        .then((data) => setNames(data))
        .catch((error) => console.error("Error fetching data:", error));
    },[])
    return (
        <div>
             <h1>Registered members</h1>
             <table  id="namestable">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Date Of Birth</th>
                        <th>Email</th>
                        <th>Gender</th>
                    </tr>
                </thead>
                <tbody>
                    {names.map(({ sir_name, othernames, date_of_birth, email, gender}, i) => (
                        <tr key={`${sir_name}-${email}-${i}`}>
                            <td>{sir_name} {othernames}</td>
                            <td>{date_of_birth}</td>
                            <td>{email}</td>
                            <td>{gender}</td>
                        </tr>
                    ))}
                </tbody>
             </table>
        </div>
    )
}
export default SavedList
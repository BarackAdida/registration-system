import { useState } from "react";

function Home() {

    const [FormData, setFormData] = useState({
        sir_name: '',
        othernames: '',
        date_of_birth: '',
        email: '',
        gender: ''
    })

    function handleChange(event) {
        const {name, value} = event.target;
        setFormData(preData => ({
            ...preData,
            [name]: value
        }))
    }

    function handleSubmit(event) {
        event.preventDefault();

        fetch('http://localhost:5000/save',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(FormData),
        })
        .then(response => response.json())
        .then(data => {
            console.log("success:", data);
            alert("Data saved to the json file!");
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    }

    return (
       <div>
         <h1>THE REGISTARTION BOOK</h1>
         <form onSubmit={handleSubmit}>
            <div>
            <input name = "sir_name" type="text" placeholder="Enter sir name" value={FormData.sir_name} onChange={handleChange}/>
            <input name = "othernames" type="text" placeholder="Enter other names" value={FormData.othernames} onChange={handleChange}/>
            <input type="date" name="date_of_birth" placeholder="Date Of Birth"value={FormData.date_of_birth} onChange={handleChange}/>
            <select name="gender" id="gender"onChange={handleChange} value={FormData.gender}>
                <option value="">Select Gender</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
                <option value="">I Prefer Not To Say</option>
            </select>
            <input type="text" name="email" placeholder="Enter email" value={FormData.email} onChange={handleChange}/>
            <button type="submit">Save</button>
        </div>
         </form>
        
       </div>
    )
}

export default Home;
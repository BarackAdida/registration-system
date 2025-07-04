import { useState } from "react";

function Home() {

    const [formData, setFormData] = useState({
        sir_name: '',
        othernames: '',
        date_of_birth: '',
        email: '',
        profile_image: '',
        gender: ''
    })

    function handleChange(event) {
        const {name, type, value, files} = event.target;
        setFormData(preData => ({
            ...preData,
            [name]: type === 'file' ? files[0] : value
        }))
    }

    function handleSubmit(event) {
        event.preventDefault();

        const data = new FormData();
        for(let key in formData){
            data.append(key, formData[key])
        }
        fetch('http://localhost:5000/save',{
            method: 'POST',
            body: data
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
            <input type="file" accept="image/*"name="profile_image" onChange={handleChange}/>
            <button type="submit">Save</button>
            </div>
        </form>
        
       </div>
    )
}

export default Home;
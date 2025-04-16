import React, { useState } from 'react';
import axios from 'axios';

function App(){
  const [location,setLocation] = useState("");
  const [size,setSize] = useState(0.0);
  const [price,setPrice] = useState(0.00);

  const predictPrice = async () => {
    try{
      const response = await axios.post("http://localhost:5000/predict",{
        location,
        size
      });

      setPrice(response.data.predicted_price);

    }catch(error){
      console.error(error);

    }
  };

  return(
    <div>
      <h1>Sri Lanka Land Price Predictor</h1>

      <form onSubmit={(e) => { e.preventDefault(); predictPrice();}}>
        <input type="text" placeholder='Location Ex:Colombo ' value={location} onChange={(e)=>setLocation(e.target.value)} required />
        <input type="number" placeholder='Size in Perches' value={size} onChange={(e)=>setSize(e.target.value)} required />
        <button type="submit">Predict Price</button>
      </form>

      {price && <h2>Predicted Price: {price} LKR</h2>}
    </div>
  );
}

export default App;
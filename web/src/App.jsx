import React, { useState } from 'react';
import axios from 'axios';

function App(){
  const [location,setLocation] = useState("");
  const [size,setSize] = useState();
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
      <h1 className='text-center'>Sri Lanka Land Price Predictor</h1>

      <div className='row'>
          <form onSubmit={(e) => { e.preventDefault(); predictPrice();}} style={{ margin:'20px', width:'650px',border:'1px solid black',padding:'20px',borderRadius:'10px'}}>
            <label htmlFor="location">District:</label> <br />
            <input type="text" placeholder='Input a District' value={location} onChange={(e)=>setLocation(e.target.value)} required className='form-control' /> <br />
            <label htmlFor="size">Size:</label>
            <input type="number" placeholder='Size in Perches' value={size} onChange={(e)=>setSize(e.target.value)} required className='form-control' /> <br />
            <button type="submit" className='btn btn-primary'>Predict Price</button>
          </form>

          <h2>Predicted Price: {price} LKR</h2>
      </div>
    </div>
  );
}

export default App;
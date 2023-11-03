import React, { Component } from "react";

class SymptomForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedSymptoms: Array(5).fill([]), // Array of 5 selected symptoms arrays
      predictions: {},
    };
    this.availableSymptoms = [
      "Itching",
      "Skin Rash",
      "Nodal Skin Eruptions",
      "Continuous Sneezing",
      "Shivering",
      "Chills",
      "Joint Pain",
      "Stomach Pain",
      "Acidity",
      "Ulcers On Tongue",
      "Muscle Wasting",
      "Vomiting",
      "Burning Micturition",
      "Spotting  Urination",
      "Fatigue",
      "Weight Gain",
      "Anxiety",
      "Cold Hands And Feets",
      "Mood Swings",
      "Weight Loss",
      "Restlessness",
      "Lethargy",
      "Patches In Throat",
      "Irregular Sugar Level",
      "Cough",
      "High Fever",
      "Sunken Eyes",
      "Breathlessness",
      "Sweating",
      "Dehydration",
      "Indigestion",
      "Headache",
      "Yellowish Skin",
      "Dark Urine",
      "Nausea",
      "Loss Of Appetite",
      "Pain Behind The Eyes",
      "Back Pain",
      "Constipation",
      "Abdominal Pain",
      "Diarrhoea",
      "Mild Fever",
      "Yellow Urine",
      "Yellowing Of Eyes",
      "Acute Liver Failure",
      "Fluid Overload",
      "Swelling Of Stomach",
      "Swelled Lymph Nodes",
      "Malaise",
      "Blurred And Distorted Vision",
      "Phlegm",
      "Throat Irritation",
      "Redness Of Eyes",
      "Sinus Pressure",
      "Runny Nose",
      "Congestion",
      "Chest Pain",
      "Weakness In Limbs",
      "Fast Heart Rate",
      "Pain During Bowel Movements",
      "Pain In Anal Region",
      "Bloody Stool",
      "Irritation In Anus",
      "Neck Pain",
      "Dizziness",
      "Cramps",
      "Bruising",
      "Obesity",
      "Swollen Legs",
      "Swollen Blood Vessels",
      "Puffy Face And Eyes",
      "Enlarged Thyroid",
      "Brittle Nails",
      "Swollen Extremeties",
      "Excessive Hunger",
      "Extra Marital Contacts",
      "Drying And Tingling Lips",
      "Slurred Speech",
      "Knee Pain",
      "Hip Joint Pain",
      "Muscle Weakness",
      "Stiff Neck",
      "Swelling Joints",
      "Movement Stiffness",
      "Spinning Movements",
      "Loss Of Balance",
      "Unsteadiness",
      "Weakness Of One Body Side",
      "Loss Of Smell",
      "Bladder Discomfort",
      "Foul Smell Of Urine",
      "Continuous Feel Of Urine",
      "Passage Of Gases",
      "Internal Itching",
      "Toxic Look (Typhos)",
      "Depression",
      "Irritability",
      "Muscle Pain",
      "Altered Sensorium",
      "Red Spots Over Body",
      "Belly Pain",
      "Abnormal Menstruation",
      "Dischromic Patches",
      "Watering From Eyes",
      "Increased Appetite",
      "Polyuria",
      "Family History",
      "Mucoid Sputum",
      "Rusty Sputum",
      "Lack Of Concentration",
      "Visual Disturbances",
      "Receiving Blood Transfusion",
      "Receiving Unsterile Injections",
      "Coma",
      "Stomach Bleeding",
      "Distention Of Abdomen",
      "History Of Alcohol Consumption",
      "Fluid Overload",
      "Blood In Sputum",
      "Prominent Veins On Calf",
      "Palpitations",
      "Painful Walking",
      "Pus Filled Pimples",
      "Blackheads",
      "Scurring",
      "Skin Peeling",
      "Silver Like Dusting",
      "Small Dents In Nails",
      "Inflammatory Nails",
      "Blister",
      "Red Sore Around Nose",
      "Yellow Crust Ooze",
    ];
  }

  handleSelectChange = (event, selectIndex) => {
    const { value } = event.target;
    this.setState((prevState) => {
      const updatedSelectedSymptoms = [...prevState.selectedSymptoms];
      updatedSelectedSymptoms[selectIndex] = [value];
      return { selectedSymptoms: updatedSelectedSymptoms };
    });
  };

  handleSubmit = async (event) => {
    event.preventDefault();
    const allSelectedSymptoms = this.state.selectedSymptoms.flat().join(",");

    try {
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ symptoms: allSelectedSymptoms }),
      });

      if (response.ok) {
        const data = await response.json();
        this.setState({ predictions: data });
      } else {
        console.error("Failed to fetch predictions");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  render() {
    const { predictions, selectedSymptoms } = this.state;

    return (
      <div className="container text-center">
        <h1 className="mt-5">Autonomous Disease Predictor</h1>
        <form className="m-5" onSubmit={this.handleSubmit}>
          <div>
            <h2>Select your Symptoms:</h2>
            {selectedSymptoms.map((selected, selectIndex) => (
              <div className="form-group" key={selectIndex}>
                <select
                  className="form-control m-3"
                  value={selected[0] || ""}
                  onChange={(event) =>
                    this.handleSelectChange(event, selectIndex)
                  }
                >
                  <option value="">Select symptom {selectIndex + 1}</option>
                  {this.availableSymptoms.map((symptom, index) => (
                    <option key={index} value={symptom}>
                      {symptom}
                    </option>
                  ))}
                </select>
              </div>
            ))}
          </div>
          <button className="btn btn-danger mt-3" type="submit">
            Predict
          </button>
        </form>
        {Object.keys(predictions).length > 0 && (
          <div>
            <h2>Predictions:</h2>
            <p>RF Model Prediction: {predictions.rf_model_prediction}</p>
            <p>Naive Bayes Prediction: {predictions.naive_bayes_prediction}</p>
            <p>SVM Model Prediction: {predictions.svm_model_prediction}</p>
            <p>Final Prediction: {predictions.final_prediction}</p>
          </div>
        )}
      </div>
    );
  }
}

export default SymptomForm;

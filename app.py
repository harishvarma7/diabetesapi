from fastapi import FastAPI
import uvicorn
import pickle
from model import health
from fastapi.middleware.cors import CORSMiddleware



model=pickle.load(open("diabetes.pkl","rb"))

app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with the appropriate origins if needed
    allow_methods=["*"],  # Update this with the appropriate HTTP methods if needed
    allow_headers=["*"],  # Update this with the appropriate headers if needed
)

@app.post("/")
def predict(data:health):
    data=data.dict()
    
    gen=data['gender']
    age=data['age']
    ht=data['hypertension']
    heart=data['heart_disease']
    smoke=data['smoking_history']
    bmi=data['bmi']
    hb=data['HbA1c_level']
    glu=data['blood_glucose_level']
    features=list([gen,age,ht,heart,smoke,bmi,hb,glu])
    ans=model.predict([features])
    preds = model.predict_proba([features])
    res=round(preds[0][0]*100,2)
    
    return str(res)
        


if __name__=="__main__":
    uvicorn.run(app)

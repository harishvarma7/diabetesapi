from pydantic import BaseModel


class health(BaseModel):
    gender:int
    age :float
    hypertension :int
    heart_disease :int
    smoking_history :int
    bmi:float
    HbA1c_level :float
    blood_glucose_level:int
#[1,53.0,0,0,4,27.32,6.1,155]
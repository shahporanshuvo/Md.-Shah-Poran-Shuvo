"""This function checks a user's diabetes status
based on blood glucose level and measurement timing(fasting / postmeal)"""
import datetime
def check_diabetes_status():
    blood_glucose_level = float(input("Blood glucose level in mmol/L: "))
    condition_of_measurement = input("When you Measure Blood glucose level: ")
    age = int(input("Enter your Age: "))

    if 18 <= age <= 59 and 3.9 <= blood_glucose_level <= 5.5 and condition_of_measurement == "fasting":
        return "You are normal."
    elif 18 <= age <= 59 and  blood_glucose_level <= 3.8 and condition_of_measurement == "fasting":
        return "Your blood glucose level may be below normal,\nPlease eat a quick source of sugar."
    elif 18 <= age <= 59 and 3.8<= blood_glucose_level <= 7.8 and condition_of_measurement == "postmeal" :
        return "you are normal"
    elif 18 <= age <= 59 and blood_glucose_level <= 3.8 and condition_of_measurement == "postmeal":
        return "Your blood glucose level may be below normal,\nPlease eat a quick source of sugar."
    elif 18<= age <= 59 and 5.6 <= blood_glucose_level <= 6.9 and condition_of_measurement == "fasting":
        return "You are in a prediabetic state,\nIt's important to change your eating habits and lifestyle."
    elif 18<= age <= 59 and 7.8 <= blood_glucose_level <= 11 and condition_of_measurement == "postmeal":
        return "You are in a prediabetic state,\nIt's important to change your eating habits and lifestyle."
    elif 18<= age <= 59 and blood_glucose_level >= 7.0 and condition_of_measurement == "fasting":
        return " You are in a diabetic condition,\nPlease visit a doctor and take the necessary medication and advice to manage your diabetes."
    elif 18<= age <= 59 and blood_glucose_level >= 11.1 and condition_of_measurement == "postmeal":
        return "You are in a diabetic condition,\nPlease visit a doctor and take the necessary medication and advice to manage your diabetes."
    elif age<=17 and 4.4 <= blood_glucose_level <= 7.2 and condition_of_measurement == "fasting":
        return "you are normal"
    elif age <= 17 and  blood_glucose_level <= 4.3 and condition_of_measurement == "fasting":
        return "Your blood glucose level may be below normal,\nPlease eat a quick source of sugar."
    elif age <= 17 and blood_glucose_level <= 10.0 and condition_of_measurement == "postmeal":
        return "you are normal"
    elif age <= 17 and blood_glucose_level <= 5.0 and condition_of_measurement == "postmeal":
        return "Your blood glucose level may be below normal,\nPlease eat a quick source of sugar."
    elif age <= 17 and blood_glucose_level >= 7.3 and condition_of_measurement == "fasting":
        return "Your blood glucose level is abnormal,\nIt's important to adjust your lifestyle and eating habits."
    elif age <= 17 and blood_glucose_level >= 10.1 and condition_of_measurement == "postmeal":
        return "Your blood glucose level is abnormal,\nIt's important to adjust your lifestyle and eating habits."
    elif age >= 60 and 5.8<= blood_glucose_level <= 8.3 and condition_of_measurement == "fasting":
        return "you are normal"
    elif age >= 60 and blood_glucose_level <= 5.7 and condition_of_measurement == "fasting":
        return "Your blood glucose level may be below normal,\nPlease eat a quick source of sugar."
    elif age >= 60 and 7.2<= blood_glucose_level <= 11.1 and condition_of_measurement == "postmeal":
        return "you are normal"
    elif age >= 60 and blood_glucose_level <= 7.1 and condition_of_measurement == "postmeal":
        return "Your blood glucose level may be below normal,\nPlease eat a quick source of sugar."
    elif age >= 60 and blood_glucose_level >= 8.4 and condition_of_measurement == "fasting":
        return "Your blood glucose level is abnormal,\nIt's important to adjust your lifestyle,eating habits and please visit a doctor."
    elif age >= 60 and blood_glucose_level >= 11.2 and condition_of_measurement == "postmeal" :
        return "Your blood glucose level is abnormal,\n It's important to adjust your lifestyle,eating habits and please visit a doctor."

    else:
        return "you may have input Incorrect data to measure diabetes status, please check again, thank you"

result = check_diabetes_status()
print(result)


now = datetime.datetime.now()

formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_now)

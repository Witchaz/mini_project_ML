# !pip install gradio ipywidgets
import pandas as pd
import gradio as gr
import joblib

# "Artifacts"
pipeline = joblib.load("pipeline.joblib")
label_pipeline = joblib.load("label_pipeline.joblib")
departments = joblib.load("departments.joblib")
salary = joblib.load("salary.joblib")


def predict(department, promoted, review, projects, salary, tenure, satisfaction, bonus, avg_hrs_month):
    sample = dict()
    sample['department'] = department
    sample['promoted'] = promoted
    sample['review'] = review
    sample['projects'] = projects
    sample['salary'] = salary
    sample['tenure'] = tenure
    sample['satisfaction'] = satisfaction
    sample['bonus'] = bonus
    sample['avg_hrs_month'] = avg_hrs_month

    left = pipeline.predict(pd.DataFrame([sample]))
    left = label_pipeline.inverse_transform([price])
    return left

# https://www.gradio.app/guides
with gr.Blocks() as blocks:
    department = gr.Dropdown(departments, value=departments[0], label="Department")
    promoted = gr.Textbox(label="Promoted")
    review = gr.Number(label="Review", value=1, minimum=0.0, maximum= 1)
    projects = gr.Number(label="Projects", value=1, minimum=0, step=1)
    salary = gr.Dropdown(salary, value=salary[0], label="salary")
    tenure = gr.Number(label="Tenure", value=1, minimum=0)
    satisfaction = gr.Number(label="Satisfaciton", value=1, minimum=0.0, maximum= 1)
    bonus = gr.Number(label="Bonus", value=1, minimum=0, maximum= 1, step=1)
    avg_hrs_month = gr.Slider(label="Average hours/month", minimum=0)
    left = gr.Text(label="Price")

    inputs = [department, promoted, review, projects, salary, tenure, satisfaction, bonus, avg_hrs_month]
    outputs = [left]

    predict_btn = gr.Button("Predict")
    predict_btn.clieck(predict, inputs=inputs, outputs=outputs)

if __name__ == "__main__":
    blocks.launch() # Local machine only
    # blocks.launch(server_name="0.0.0.0") # LAN access toci local machine
    # blocks.launch(share=True) # Public access to local machine

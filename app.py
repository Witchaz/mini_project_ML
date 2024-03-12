# !pip install gradio ipywidgets
import pandas as pd
import gradio as gr
import joblib

# "Artifacts"
pipeline = joblib.load("pipeline.joblib")
label_pipeline = joblib.load("label_pipeline.joblib")
departments_list = joblib.load("departments.joblib")
salary_list = joblib.load("salary.joblib")
boolean_dict = {'Yes':1,'No':0}


def predict(department, promoted, review, projects, salary, tenure, satisfaction, bonus, avg_hrs_month):
    sample = dict()
    sample['department'] = department
    sample['promoted'] = boolean_dict[promoted]
    sample['review'] = review
    sample['projects'] = projects
    sample['salary'] = salary
    sample['tenure'] = tenure
    sample['satisfaction'] = satisfaction
    sample['bonus'] = boolean_dict[bonus]
    sample['avg_hrs_month'] = avg_hrs_month

    left = pipeline.predict(pd.DataFrame([sample]))
    print(left)
    return left

# https://www.gradio.app/guides
with gr.Blocks() as blocks:
    department = gr.Dropdown(departments_list, value=departments_list[0], label="Department")
    promoted = gr.Radio(['Yes','No'],label = "promoted",info = "is they promoted?")
    review = gr.Number(label="Review", value=0.0, minimum=0.0, maximum= 1.0,step=0.1,info="range(0-1)")
    projects = gr.Number(label="Projects", value=1, minimum=0, step=1)
    salary = gr.Dropdown(salary_list, value=salary_list[0], label="salary")
    tenure = gr.Number(label="Tenure", value=1, minimum=0)
    satisfaction = gr.Number(label="Satisfaction", value=0.0, minimum=0.0, maximum= 1.0,step=0.1,info="range(0-1)")
    bonus = gr.Radio(['Yes','No'],label = "bonus",info = "is they get bonus?")
    avg_hrs_month = gr.Number(label="Average hours/month", minimum=0)
    predict_btn = gr.Button("Predict")
    left = gr.Text(label="left")

    inputs = [department, promoted, review, projects, salary, tenure, satisfaction, bonus, avg_hrs_month]
    outputs = left

    predict_btn.click(predict, inputs=inputs, outputs=outputs)
    print(outputs)

    

if __name__ == "__main__":
    blocks.launch() # Local machine only
    # blocks.launch(server_name="0.0.0.0") # LAN access toci local machine
    # blocks.launch(share=True) # Public access to local machine

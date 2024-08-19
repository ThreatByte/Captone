# Capstone

## Introduction

- The purpose of this capstone project was to see if we can detect fileless malware using a large language model.
- Large language model we used was Securebert(RobertaSequenceClassification) Meta AI Model.
- Securebert is trained on cybersecurity textual data.

## My Contribution
- Setup Windows, and Remnux virtualmachines for project.
- Trained Large Language Model Locally.
- Created VolailityAuto.py and commands.yaml, and Helped with creating a function dealing with unzipping malware with password of infected.

## Scripts

- Host was used for starting, stop, and reverting VM to a predetonation snapshot.
- PyAutosys was used for unzipping malware with a password of infected, detonating sample, taking memory dump, transfering to remnux.
- VolatilityAuto Python script loops through commands.yaml to execute volatility plugins on memory dump.
- LLM Script finetuned securebert locally on our data from csv.

## Tools Used

- VMware Workstation, python, Volatility, winpmem, Office 2021

## Running Scripts
- If you want to run the scripts and see the output download Python 3.11.3, VSCode Extenstions Jupyter, and Python.
- Also, to fix importanterror restart jupyter kernel https://github.com/huggingface/transformers/issues/28191  

# Intrusion-Detecion-Using-ML-on-CICIDS-17

This project utilizes machine learning to detect anomalies and intrusions in network data. Trained on the benchmarked CICIDS dataset, the system identifies patterns indicative of security threats, contributing to enhanced cybersecurity through proactive detection.

# Intrusion Detection using Machine Learning

## Overview

This repository showcases a machine learning model developed using the CICIDS 17 dataset for intrusion detection. Through this project, we have explored the realms of both machine learning and deep learning methodologies.

## Dataset

- Utilized the CICIDS dataset, a comprehensive collection of intrusions with various attack types.
- The dataset is unbalanced, impacting algorithm performance.

## Dataset Download

- All Python files are available in the repository.
- To run the project, download the CICIDS dataset from [here](https://www.unb.ca/cic/datasets/ids-2017.html).
- Run all Python files in sequence to create the required CSV files, including the creation of a balanced dataset.

## Quick Start

- Alternatively, for a quick overview of the approach:
  - Unzip the two CSV files in the `required_csv.zip`.
  - Run `model_train_ML.py` to train the machine learning model.
  - Run `MLDF_model_test.py` to test the created model on the preprocessed dataset.

### Note: Change File Paths

- Please note that you may need to change the file paths in the Python code to match the location where you have saved the CSV files. Check and modify the file paths in the code accordingly.

## Model Training

- Trained a machine learning model on the balanced dataset.
- Achieved a trained model ready for deployment.

## Deployment on ELK Stack

- Utilized the ELK Stack to simulate the model's effectiveness on live data and attacks.
- While ELK Stack results cannot be displayed on GitHub, users can train their own model and simulate attacks using a basic Kali Linux setup with a router.

## Demonstration

- Successfully demonstrated the project at a national hackathon.
- The model proved highly efficient in detecting various types of attacks.

## Future Goals

- As future goals, aim to delve into Deep Learning.
- Plan to train a Convolutional Neural Network (CNN) model.
- Explore Generative Adversarial Networks (GAN) on tabular data.
- Verify generated data using statistical methods.
- Integrate the generated data into deep learning approaches.

## Project Authors

- Lakshya Agrawal
- Adarsh Jha
- Gunjan Agrawal

Feel free to explore, contribute, and adapt this project for your cybersecurity endeavors.

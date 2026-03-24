# S75-0326-CrashInsight-Python-Numpy-Pandas-Streamlit-Matlotlib-scikit-learn

# Understanding the Data Science Lifecycle: Question → Data → Insight

## 1. Explaining the Question → Data → Insight Lifecycle

Data science does not begin with tools, algorithms, or models. It begins with a **clear question**. The lifecycle of Question → Data → Insight represents the logical process used to convert a real-world problem into actionable understanding.

### Starting with a Clear Question

A data science project starts by defining a clear and specific problem. Without a well-defined question, analyzing data becomes unfocused and may produce patterns that are not useful for decision-making.   

For example, asking **“What does the data show?”** is vague and does not guide analysis. A stronger question would be **“Which factors contribute most to road accidents?”**

A clear question helps determine:

* What data needs to be collected
* Which variables are relevant
* What kind of analysis should be performed

This step ensures that the analysis is aligned with solving a real problem.

### Data as Evidence

Once the question is defined, the next step is understanding the data. Data acts as **evidence** that helps answer the question, but it must be interpreted carefully.

Before performing any analysis, it is necessary to understand:

* Where the data comes from
* What each column or feature represents
* Whether there are missing values or inconsistencies
* Whether the dataset is actually suitable for answering the question

For example, traffic accident data may include details such as road type, weather conditions, time of day, and accident severity. Understanding these variables is essential before drawing any conclusions.

Treating data as evidence rather than absolute truth helps prevent incorrect interpretations.

### From Exploration to Insight

After understanding the dataset, the next step is **exploratory analysis**. This stage focuses on observing patterns, trends, and relationships within the data.

Examples of exploration include:

* Examining how accidents vary across different times of day
* Comparing accident rates across road types
* Observing whether weather conditions influence accident frequency

However, raw observations are not enough. An **insight** occurs when these observations are connected to a meaningful explanation that can guide decisions.

For example:

Observation:
Accidents occur more frequently during rainy weather.

Insight:
Poor visibility and slippery roads during rain may increase accident risk, suggesting that improved road markings or warning systems could reduce accidents.

This lifecycle ensures that data analysis moves from identifying a problem to generating insights that can support real-world decisions.

---

## 2. Applying the Lifecycle to a Traffic Safety Scenario

### Project Context

Traffic police collect large amounts of accident data, but the data is often stored without detailed analysis. As a result, important patterns related to road safety may go unnoticed.

Applying the Question → Data → Insight lifecycle can help transform this raw data into useful information for reducing accidents.

### Question

Which factors such as road type, weather conditions, and time of day contribute most to traffic accidents?

This question focuses the analysis on identifying conditions that increase accident risk and allows authorities to design targeted safety measures.

### Data Needed

To answer this question, the following types of data would be useful:

* Accident location
* Road type (highway, intersection, residential road)
* Weather conditions during the accident
* Time of day
* Vehicle types involved
* Severity of the accident

This data could come from police accident reports, transportation department databases, or traffic monitoring systems.

Before analysis, it would be necessary to verify the quality of the data and ensure that important variables are consistently recorded.

### Insight

Exploring the data may reveal patterns such as:

* Higher accident frequency during late-night hours
* Increased accidents during rainy or foggy conditions
* Certain intersections or highways having unusually high accident rates

These patterns can lead to insights that inform safety improvements.

For example:

* Installing better lighting at high-risk intersections
* Increasing traffic patrols during late-night hours
* Adding warning systems or improved road markings in areas with frequent accidents

These insights allow authorities to implement **targeted interventions**, which are more effective than applying general safety measures across all locations.

---

## Conclusion

The Question → Data → Insight lifecycle ensures that data science projects remain focused on solving real problems. Starting with a clear question guides the analysis, understanding the data ensures reliable evidence, and exploring the data helps generate insights that support informed decisions.

In the case of traffic accident analysis, applying this lifecycle can help identify risk factors and enable targeted interventions that improve road safety and reduce accidents.


# Interpreting a Data Science Project Repository

## Understanding the Project Goal

The repository analyzes traffic accident data to understand factors
that contribute to road accidents.

## Role of the README

The README explains the project objective, describes the dataset,
and outlines the workflow used in the analysis.

## Repository Structure

The project contains folders for datasets, notebooks, and visual outputs.

- data/ contains the accident datasets
- notebooks/ includes exploratory analysis notebooks
- figures/ contains visualizations generated during analysis

This structure reflects the stages of the data science lifecycle.

## Understanding the Notebook

The notebook loads the dataset, performs cleaning operations,
and explores patterns using statistical summaries and visualizations.

## Assumptions and Limitations

The project assumes that accident reports contain accurate
weather and time information. However, missing values and incomplete
records may affect the reliability of the analysis.

## Opportunities for Improvement

Future work could include more detailed location analysis
and additional visualizations to identify accident hotspots.

# CrashInsight – Project Plan & MVP Definition

## 1. Problem Statement

Traffic police collect large amounts of accident data, but it is rarely analyzed to identify patterns such as road type, weather conditions, and time of day.

As a result, preventive actions are not targeted, and accidents continue to occur.

---

## 2. Solution Overview

CrashInsight aims to:

* Analyze accident data
* Identify high-risk conditions
* Predict accident risk based on input factors

The system will connect:

Problem → Data → Model → Application

Users will input conditions such as road type, weather, and time, and the system will output a predicted risk level.

---

## 3. Dataset & Scope

### Dataset

The dataset includes:

* Road type (highway, intersection, residential)
* Weather conditions (clear, rainy, foggy)
* Time of day (morning, evening, night)
* Accident severity
* Location data

### Scope

Included:

* Structured tabular data
* Basic feature analysis
* Classification model

Excluded:

* Image/video data
* Real-time traffic systems
* Complex deep learning models

---

## 4. MVP (Minimum Viable Product)

The MVP will include:

* Input:

  * Road type
  * Weather condition
  * Time of day

* Processing:

  * Preprocessed dataset
  * Machine learning classification model

* Output:

  * Accident Risk Level (Low / Medium / High)

* Interface:

  * Simple web app using Streamlit

---

## 5. Functional Requirements

* Accept user inputs (road, weather, time)
* Process inputs using trained ML model
* Display predicted accident risk level
* Show basic visual insights (charts)

---

## 6. Non-Functional Requirements

* Fast response time (< 2 seconds)
* Simple and user-friendly UI
* Reliable predictions
* Easy to maintain code structure

---

## 7. Roles & Responsibilities

* Data Processing:
  Data cleaning, preprocessing, feature selection

* Modeling:
  Model training, evaluation, tuning

* Application:
  Building UI using Streamlit and integrating model

---

## 8. Sprint Timeline (4 Weeks)

Week 1:

* Define problem clearly
* Collect and clean dataset

Week 2:

* Perform EDA (Exploratory Data Analysis)
* Identify important features

Week 3:

* Train ML model (Logistic Regression / Decision Tree)
* Evaluate model performance

Week 4:

* Build Streamlit app
* Integrate model into app
* Testing and deployment

---

## 9. Success Metrics

* Model accuracy ≥ 70%
* App runs without crashes
* Predictions are consistent
* User can input data and get results successfully

---

## 10. Risks & Mitigation

Risk: Poor data quality
Mitigation: Perform data cleaning and validation

Risk: Model performs poorly
Mitigation: Try multiple models and tune parameters

Risk: Time constraints
Mitigation: Focus only on MVP features

Risk: Incomplete dataset
Mitigation: Use simplified assumptions and limit scope

---

## 11. Deployment Plan

* Use Streamlit for frontend
* Deploy using Streamlit Cloud / local server
* Ensure app is accessible and functional

---

## 12. Final Outcome

CrashInsight will be a working system that:

* Takes real-world conditions as input
* Uses data + ML to evaluate accident risk
* Helps in making data-driven safety decisions

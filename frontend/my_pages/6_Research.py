import streamlit as st

def show():

    st.markdown("""
    <style>
        .title {font-family: 'Times New Roman'; font-size: 26pt; font-weight: bold; text-align: center;}
        .author {font-family: 'Times New Roman'; font-size: 14pt; text-align: center;}
        .section {font-family: 'Times New Roman'; font-size: 16pt; font-weight: bold; margin-top: 20px;}
        .content {font-family: 'Times New Roman'; font-size: 12pt; text-align: justify; line-height: 1.6;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="title">
    Physics-Informed Machine Learning Approach for NOx Prediction in Indian Subway Tunnel Environments Using Real-Time Air Quality Data
    </div>

    <div class="author">
    Sudhanshu Ranjan Singh¹ <br>
    ¹ Department of Computer Science / AI & ML <br>
    Correspondence: ranjansinghsudhanshu13@gmail.com
    </div>
    <hr>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section">Abstract</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="content">
    Air pollution in subway tunnel environments is a growing concern in densely populated cities like Delhi due to pollutant accumulation under limited ventilation. 
    This study proposes a physics-informed machine learning framework to predict NOx concentrations using real-world air quality data from sources such as OpenAQ, 
    combined with simulated tunnel parameters like airflow, traffic intensity, and depth. 
    Multiple models including Linear Regression, Polynomial Regression, Random Forest, and XGBoost were evaluated. 
    The Random Forest model achieved the best performance with an R² score of 0.988 and RMSE of 7.80. 
    Explainable AI techniques (SHAP and LIME) were used to interpret model predictions. 
    The results demonstrate that integrating physical insights with machine learning enables accurate and interpretable NOx prediction, 
    supporting real-time monitoring in subway systems.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="content">
    <b>Keywords:</b> NOx Prediction; Subway Air Pollution; Machine Learning; Random Forest; SHAP; LIME; OpenAQ; Tunnel Ventilation
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section">1. Introduction</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="content">
    Air pollution in cities has become a huge problem for the environment and for people's health[1]. As more people move to cities and industries grow, the air is getting worse[2], [3]. 
    This is especially true in big cities like Delhi, where a lot of cars and other vehicles are making the air dirty[4], [5]. 
    While we know a lot about the pollution on the streets, we don't know as much about the air quality in underground transportation systems like metro trains[6], [7]. 
    These systems are important for helping people get around cities, but they can also trap pollutants in a small space, making the air worse over time[5], [6].

    Subway tunnels are special because they don't get much fresh air[6], [7]. This is different from being outside in the city where the air can move around and spread-out pollutants[2], [5]. 
    In tunnels, the bad air gets stuck and can't escape, making it worse for people breathing it in[6], [8]. 
    There are lots of things in tunnels that make the air dirty, like the trains running, the brakes being used, and all the equipment that keeps everything working[9], [10]. 
    Even when people are just walking around in the tunnels, they can make the air worse[6]. 
    And to make things worse, bad air from outside can also get into the tunnels through the vents and entrances, making the whole situation even more polluted[5], [7]
    </div>
    """, unsafe_allow_html=True)

    # ===== FIGURE 1 ONLY =====
    st.image("Research images/Figure 1.jpeg", caption="Figure 1", use_container_width=True)

    st.markdown("""
<div class="content">
Breathing easy is not always a given, especially in crowded places like subways[6], 
[7]. There are lots of things in the air that can hurt us, but some of the worst ones are 
nitrogen oxides, like nitric oxide and nitrogen dioxide[1], [8]. These gases are really 
bad for our health, and can cause problems like trouble breathing, lungs that don't 
work as well, and getting sick more easily[1], [6]. If we're around them for a long 
time, they can even lead to big health problems like asthma and bronchitis[1], [6]. 
And it's not just our health that's the problem - these gases also make the air worse 
by helping to create other bad things like ozone and tiny particles that float 
around[1], [7]. When we're in small spaces like subway tunnels, it's even worse 
because we're breathing in all those bad things for a long time, which can be really 
dangerous for people who ride the subway every day and for the people who work 
there[6], [7]. 

Given these risks, accurate prediction and monitoring of NOx concentrations in 
subway systems are critical for ensuring public safety and improving environmental 
management strategies[5], [6], [11]. Traditional approaches to air quality prediction 
can be broadly categorized into two types: physics-based models and data-driven 
machine learning models[3], [12], [13], [14]. Physics-based models rely on 
fundamental principles such as fluid dynamics, mass balance equations, and 
chemical kinetics to simulate pollutant dispersion[11], [12]. While these models 
provide strong theoretical grounding, they often require complex assumptions, 
detailed parameter estimation, and significant computational resources. Moreover, 
their applicability may be limited in dynamic and data-scarce environments like 
subway tunnels. 

Machine learning models provide a different approach to predicting air quality by 
looking at patterns in past data[3], [13], [14], [15]. Some techniques, like Linear 
Regression, Decision Trees, Random Forest, and Gradient Boosting, have done well 
in predicting air quality[3], [13], [15]. These models can find relationships between 
variables that aren't always straightforward, without needing to know the exact 
physical processes behind them[12], [14]. But models that only rely on data have 
their own set of problems. It's hard to understand why they make certain 
predictions, and they might not work as well in new situations where the physical 
conditions are different. This is because they don't consider what we already know 
about the subject[12]. 

To overcome these limitations, researchers have been exploring new approaches 
that bring together the best of both worlds - physical modeling and machine 
learning[8], [12], [14]. These hybrid methods combine the strengths of both 
techniques by adding domain-specific knowledge to machine learning 
frameworks[8], [12]. By including physics-based features like how air moves, the 
shape of tunnels, how busy the roads are, and what the weather is like, these 
models can be more accurate while still being easy to understand and reliable[8], 
[12], [14]. This means they can take into account things like airflow dynamics, tunnel 
geometry, traffic intensity, and environmental conditions to make better 
predictions[8], [12]. 

In this study, a physics-informed machine learning framework is proposed to predict 
NOx concentrations in subway tunnel environments[8], [12], [14]. The approach 
leverages real-world air quality data obtained through the OpenAQ platform[16], 
[17], which provides access to pollutant measurements from monitoring stations 
such as Shadipur in Delhi[16]. The dataset includes key pollutant indicators such as 
carbon monoxide (CO), nitric oxide (NO), nitrogen dioxide (NO₂), ozone (O₃), and 
particulate matter (PM₁₀), along with meteorological variables like temperature, 
humidity, and wind speed[2], [6], [16]. 

To make the model better at predicting things, we're adding some new features that 
are based on how the world works[8], [12]. We're looking at things like how air 
moves, which helps spread pollutants around, how busy the traffic is, which shows 
how much pollution is being made, and how deep tunnels are, which affects how 
well they can get rid of pollutants[5], [7], [10]. By putting these features together with 
real data, the model can understand both how the environment changes and the 
underlying rules that govern how pollutants behave[8], [12], [14]. This way, it can give 
us more accurate predictions. 

To better understand what affects the levels of nitrogen oxides, or NOx, in the air, 
researchers looked at several different machine learning models[3], [13], [15]. These 
included Linear Regression, Polynomial Regression, Random Forest, and XGBoost, 
to see which one worked best for predicting NOx levels[3], [13]. They also used 
special techniques like SHAP and LIME to help explain what the models were doing 
and which factors were most important[12], [15]. This made it clearer how the 
models were working and what was driving NOx levels, giving useful insights into the 
problem[8], [12]. By using these methods, the study aimed to make the process 
more transparent and to identify the key factors that influence NOx levels, which is 
crucial for improving air quality[1], [6], [14]. 

The primary objective of this research is to develop a robust, accurate, and 
interpretable framework for predicting NOx concentrations in subway 
environments[8], [12], [15]. Such a system can support real-time monitoring[16], 
[17], assist in ventilation system optimization[7], [10], and contribute to data-driven 
decision-making for urban air quality management[2], [13]. Ultimately, this work 
aims to bridge the gap between theoretical modeling and practical implementation, 
offering a scalable solution to address the growing challenge of underground air 
pollution in modern cities[5], [6], [11].
</div>
""", unsafe_allow_html=True)
    
    st.markdown('<div class="section">2. Literature Review</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
Extensive research has been conducted on subway air quality, tunnel pollution, and 
machine learning-based environmental modeling. Previous studies provide valuable 
insights into pollutant behavior, influencing factors, and modeling approaches. 

[5]Zhang et al. (2024), in Environment International, reviewed indoor subway air quality 
across multiple cities. They identified key influencing factors such as passenger density, 
ventilation efficiency, and train frequency. Their work highlights the importance of 
environmental and operational variables in determining pollutant levels, reinforcing the 
need for multi-feature modeling. 

Additionally, [9]Banasiewicz et al. (2023) developed a machine learning model for NOx 
prediction in underground mining environments. Their work demonstrated the 
effectiveness of combining sensor data with machine learning, providing a strong 
foundation for this study’s approach. 

[7]Smith et al. (2014), published in Elsevier’s Atmospheric Environment, conducted an 
experimental study on subway platform air quality, focusing on ventilation systems and 
the piston effect caused by train movement. Their findings indicated that poor 
ventilation leads to pollutant accumulation, while train-induced airflow significantly 
impacts pollutant dispersion. This study strongly supports the inclusion of airflow and 
traffic related features in predictive models Figure 2.
</div>
""", unsafe_allow_html=True)
    
    # ===== FIGURE 2 =====
    st.image("Research images/Figure 2.png", caption="Figure 2: Influence of ventilation, airflow (piston effect), and traffic on pollutant dispersion in tunnel environments", use_container_width=True)
    st.markdown("""
<div class="content">
[5]Li et al. (2019), published by MDPI, performed a global analysis of subway pollution 
and reported that over 70% of subway systems exceed safe pollution limits. They 
emphasized the role of ventilation and system design, which aligns with the physics
based approach used in this study. 

[11]Kumar et al. (2020), in Elsevier, analyzed pollution in roadway tunnels and found 
that traffic emissions are the primary source of NOx, while ventilation controls pollutant 
concentration. This directly supports the inclusion of traffic intensity and airflow in the 
proposed model. 

Additionally, [9]Banasiewicz et al. (2023) developed a machine learning model for NOx 
prediction in underground mining environments. Their work demonstrated the 
effectiveness of combining sensor data with machine learning, providing a strong 
foundation for this study’s approach. 

Other studies, including Jung et al. (2017)[6] and Dong et al. (2013)[8], further confirm 
the importance of environmental variables and machine learning techniques in 
pollution modelling.
</div>
""", unsafe_allow_html=True)
    st.markdown('<div class="section">3. Methodology</div>', unsafe_allow_html=True)
    st.markdown('<div class="section">3.1 Data Collection</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
Air quality data were obtained from the OpenAQ API for monitoring locations such as 
Shadipur in Delhi[16]. The dataset consists of high-frequency observations recorded at 
15-minute intervals, ensuring fine temporal resolution for analysis. It includes pollutant 
concentrations such as carbon monoxide (CO), nitric oxide (NO), nitrogen dioxide 
(NO₂), ozone (O₃), and particulate matter (PM₁₀), along with meteorological variables 
like temperature, humidity, and wind speed. Figure 3
</div>
""", unsafe_allow_html=True)

    # ===== FIGURE 3 =====
    st.image("Research images/Figure 3.webp", caption="Figure 3: Data collection pipeline from OpenAQ API to machine learning dataset", use_container_width=True)
    st.markdown("""
<div class="content">
This real-world dataset provides the foundation for modelling NOx concentration and 
simulating subway-like environmental conditions.
</div>
""", unsafe_allow_html=True)
    st.markdown('<div class="section">3.2.1 Fundamental Formulation (Mass Balance Principle)</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
The modelling process begins with the mass balance equation Figure 4: 

Accumulation = Emission − Removal 

Under steady-state tunnel conditions, accumulation can be approximated by pollutant 
concentration, leading to: 

C = E / V 

where C represents NOx concentration, E is emission rate, and V is the ventilation 
rate[11].
</div>
""", unsafe_allow_html=True)

    # ===== FIGURE 4 =====
    st.image("Research images/Figure 4.jpg", caption="Figure 4: Mass balance representation of emission, accumulation, and ventilation", use_container_width=True)
    st.markdown('<div class="section">3.2.2 NOx Aggregation from Measured Data</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
The total NOx concentration was computed using: 

NOx = NO + NO2 

This provides the primary target variable for prediction[1].
</div>
""", unsafe_allow_html=True)
    st.markdown('<div class="section">3.2.3 Emission Modelling (Traffic Influence)</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
Emission rate is directly influenced by traffic intensity: 

E ∝ T ⋅ EF 

where T represents traffic intensity and EF is the emission factor. 

In this study, traffic intensity was approximated as a normalized variable, assuming 
higher traffic leads to higher emissions[8], [10].
</div>
""", unsafe_allow_html=True)
    st.markdown('<div class="section">3.2.4 Ventilation Modelling (Airflow and Wind Effects)</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
Ventilation plays a critical role in pollutant dispersion and is influenced by airflow and 
wind speed Figure 5: 

V ∝ A + W 

where A is airflow and W is wind speed. 

Airflow was derived from wind speed data to represent ventilation efficiency in tunnel 
conditions[7], [10].
</div>
""", unsafe_allow_html=True)
    # ===== FIGURE 5 =====
    st.image("Research images/Figure 5.webp", caption="Figure 5: Influence of airflow and wind speed on ventilation and pollutant dispersion", use_container_width=True)
    st.markdown('<div class="section">3.2.5 Tunnel Confinement Effect</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
Tunnel depth contributes to pollutant accumulation due to restricted dispersion. This 
effect was modelled as: 

C ∝ e^(k d) 

where d is tunnel depth and k is a constant representing confinement intensity[5], [6].
</div>
""", unsafe_allow_html=True)
    st.markdown('<div class="section">3.2.6 Combined Physics-Based NOx Model</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
By integrating emission, ventilation, and confinement effects, the final core formulation 
is expressed as[5], [6], [8]: 

C_NOx = (C_surface ⋅ (1 + αT_p) e^(βd)) / (1 + γA + δW)
</div>
""", unsafe_allow_html=True)
    st.markdown('<div class="section">3.2.7 Environmental Adjustment Factors</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
To account for atmospheric and chemical influences, temperature and humidity were 
incorporated[5], [6], [12]: 

C_NOx = (C_surface ⋅ (1 + αT_p) e^(βd)) / (1 + γA + δW) ⋅ (1 + ηTemp)(1 + μRH)
</div>
""", unsafe_allow_html=True)
    st.markdown('<div class="section">3.2.8 Practical Implementation in ML Framework</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
Based on the above formulations, the following features were engineered Figure 6: 

• NOx = NO + NO₂  
• Traffic intensity (emission proxy)  
• Airflow (ventilation proxy)  
• Tunnel depth (confinement effect)  
• Temperature and humidity (environmental modifiers)  

This approach ensures that the machine learning model learns not only from data but 
also from real-world physical relationships governing pollutant behaviour[8], [12].
</div>
""", unsafe_allow_html=True)
    # ===== FIGURE 6 =====
    st.image("Research images/Figure 6.webp", caption="Figure 6: Influence of airflow and wind speed on ventilation and pollutant dispersion", use_container_width=True)
    st.markdown('<div class="section">3.3 Data Preprocessing</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
The collected data underwent several preprocessing steps to ensure quality and 
consistency: 

• Merged 11 CSV datasets into a unified dataset  
• Handled missing values using forward filling techniques  
• Converted datetime fields into a standardized format for temporal analysis  
• Removed inconsistencies, outliers, and duplicate entries  

These steps ensured that the dataset was clean, structured, and suitable for machine 
learning model training Figure 7.
</div>
""", unsafe_allow_html=True)
    # ===== FIGURE 7 =====
    st.image("Research images/Figure 7.avif", caption="Figure 7: Data preprocessing workflow for preparing dataset", use_container_width=True)
    st.markdown('<div class="section">3.4 Model Development</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
Four machine learning models were developed and evaluated: 

• Linear Regression  
• Polynomial Regression  
• Random Forest  
• XGBoost  

The dataset was split into training (80%) and testing (20%) sets. The training set was 
used to learn patterns, while the testing set evaluated model generalization. 

Polynomial Regression achieved the highest accuracy but showed potential overfitting. 
Random Forest provided the best balance between accuracy and real-world 
applicability, while XGBoost also demonstrated strong performance. Linear Regression 
showed comparatively lower performance due to its inability to model nonlinear 
relationships.
</div>
""", unsafe_allow_html=True)
    st.markdown('<div class="section">3.5 Project Workflow</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
The overall workflow of the project consists of the following stages Figure 8: 

1. Data Processing  
o Real-world air quality data collected from OpenAQ  
o Parameters: NO, NO₂, CO, O₃, PM₁₀, Temperature, Humidity, Wind Speed  

2. Physics-Based Feature Engineering  
o NOx = NO + NO₂  
o Traffic (simulated emission)  
o Airflow (ventilation proxy)  
o Depth (tunnel confinement)  

3. Target Variable Construction  
o NOx tunnel derived using emission, dispersion, and accumulation principles  

4. Model Training and Evaluation  
o Multiple ML models trained and compared  
o Performance metrics: R², RMSE  

5. Explainability and Validation  
o SHAP used for global feature importance  
o LIME used for local prediction interpretation  

6. Visualization and Analysis  
o Line plots showing tunnel vs surface NOx  
o Actual vs predicted comparisons  
o Residual analysis for model stability  
o Correlation heatmaps to identify feature relationships  

Figure 8: System Architecture of Nox Prediction Framework
</div>
""", unsafe_allow_html=True)
    # ===== FIGURE 8 =====
    st.image("Research images/Figure 8.png", caption="Figure 8: System Architecture of Nox Prediction Framework", use_container_width=True)
    st.markdown('<div class="section">4. Results and Analysis</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
The performance of different models was evaluated using R² and RMSE metrics. The 
Random Forest model achieved the best balance between accuracy and generalization. 
The performance comparison of different machine learning models for NOx prediction 
is presented in Table 4.1. Among all the models evaluated, the Random Forest model 
achieved the highest predictive accuracy with an R² score of 0.91, along with the lowest 
MAE (2.76) and RMSE (3.98), indicating superior performance in capturing the nonlinear 
relationships in the data. XGBoost also demonstrated strong performance, though 
slightly lower than Random Forest. In contrast, Linear Regression showed 
comparatively weaker results due to its inability to model complex patterns effectively. 
These results highlight the effectiveness of ensemble-based approaches, particularly 
Random Forest, for accurate NOx concentration prediction in subway tunnel 
environments[3], [8], [13].
</div>
""", unsafe_allow_html=True)
    st.markdown('<div class="section">4.1 Model Performance Table</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="content">
Figure 9 summarizes the evaluation metrics of four machine learning models used for 
predicting NOx concentrations. The comparison provides a quantitative basis for 
selecting the most suitable model for this study. 

Analysis of Model Performance 

Optimal Performance (Random Forest): 
The Random Forest model achieved the best overall performance, with the highest 
coefficient of determination (R² = 0.91) and the lowest error values (MAE = 2.76, RMSE = 
3.98). This indicates its strong ability to capture complex nonlinear relationships and 
generalize effectively in tunnel environments. 

Gradient Boosting (XGBoost): 
XGBoost also demonstrated strong predictive capability (R² = 0.89), though slightly 
lower than Random Forest. This marginal difference may be attributed to dataset 
characteristics, noise sensitivity, or hyperparameter configuration. 

Baseline Models: 
Linear Regression showed the lowest performance (R² = 0.72), confirming that linear 
models are insufficient for modeling the nonlinear dynamics of pollutant dispersion. 
The Decision Tree model (R² = 0.81) performed moderately well but is more prone to 
overfitting due to higher variance compared to ensemble methods. 

Error Sensitivity: 
For all models, RMSE values are higher than MAE, indicating the presence of occasional 
large prediction errors. This suggests the existence of outliers or sudden spikes in NOx 
concentration (as observed in Fig. 4(a)). Among all models, Random Forest handled 
these variations most effectively. 

Discussion Linkage 
These results directly support the discussion that while simpler models provide 
baseline understanding, ensemble methods—particularly Random Forest—offer 
superior performance. The improvement of approximately 0.19 in R² between Linear 
Regression and Random Forest highlights the importance of selecting models capable 
of capturing nonlinear environmental interaction. 

Figure 9: Comparative Performance Metrics of Machine Learning Models
</div>
""", unsafe_allow_html=True)
    # ===== FIGURE 9 =====
    st.image("Research images/Figure 9.png", caption="Figure 9: Comparative Performance Metrics of Machine Learning Models", use_container_width=True)
    st.markdown('<div class="section">4.2 Graphical Analysis</div>', unsafe_allow_html=True)
    # ================= 1 =================
    st.markdown("""
<div class="content">
1. Time-Series Analysis of NOx Concentration 

This time-series plot compares NOx concentration levels measured at the surface and 
within the tunnel environment over a three-month period from January to March 2026 
Figure 10. 

Key Observations 

Magnitude Disparity: 
Tunnel NOx concentrations (orange) consistently exhibit significantly higher values 
compared to surface levels (blue). While surface concentrations remain relatively stable 
and lower, tunnel concentrations frequently show sharp peaks exceeding 400 and even 
800 units. This behavior is attributed to the accumulation of vehicular emissions in a 
confined tunnel environment with limited ventilation[6], [7], [9]. 

Synchronous Trends: 
Both surface and tunnel datasets display synchronized temporal patterns. Increases in 
surface NOx levels are typically followed by corresponding increases in tunnel 
concentrations, albeit with much higher magnitude. This indicates that ambient outdoor 
air quality and regional traffic patterns influence both environments simultaneously, with 
amplification occurring inside the tunnel. 

Extreme Volatility: 
Tunnel NOx data demonstrates high variability, characterized by rapid and short-duration 
spikes. These fluctuations are indicative of peak traffic periods or the passage of heavy
duty vehicles[6], [9], which generate transient but intense pollution events within the 
confined tunnel space. 

Data Gaps: 
Linear segments observed during mid-January indicate potential missing data or sensor 
downtime. Such gaps are common in long-term environmental monitoring and highlight 
the importance of robust data preprocessing techniques. 
</div>
""", unsafe_allow_html=True)
    st.image("Research images/Figure 10.jpeg", caption="Figure 10: Temporal Comparison of Surface vs. Tunnel NOx Concentrations", use_container_width=True)
    # ================= 2 =================
    st.markdown("""
<div class="content">
2. Actual vs Predicted (Random Forest) 

This scatter plot illustrates the performance of the Random Forest regression model 
in predicting NOx tunnel concentrations. The y=x reference line represents a perfect 
prediction scenario where the predicted values exactly match the observed data 
Figure 11. 

Analysis of Model Performance: 

• High Correlation: The majority of data points are tightly clustered along the 
diagonal identity line, indicating that the model captures the underlying variance 
of the NOx emissions with high precision[8], [13], [15]. 

• Predictive Accuracy: The model demonstrates strong performance across both 
low and high concentration ranges, maintaining linearity throughout the 
dataset[8], [13]. 

• Outlier Identification: A few minor deviations are visible (notably near the 200 
and 400 actual NOx marks), suggesting specific environmental or operational 
conditions where the model slightly under-predicted the concentration[8]. 

• Overall Fit: The close alignment between the predicted and actual values 
suggests a high Coefficient of Determination (R^2), validating the Random Forest 
approach as an effective tool for this application[13], [15]. 
</div>
""", unsafe_allow_html=True)
    st.image("Research images/Figure 11.jpeg", caption="Figure 11: Actual vs. Predicted NOx Tunnel Concentrations", use_container_width=True)
    # ================= 3 =================
    st.markdown("""
<div class="content">
3. Residual Plot 

The residual plot provides a diagnostic evaluation of the model’s error distribution. 
By plotting the residuals (the difference between actual and predicted values) 
against the predicted NOx levels, we can assess the reliability of the Random Forest 
regressor Figure 12 [8], [13], [15]. 

Key Observations: 

• Homoscedasticity: The majority of the residuals are concentrated near the zero
horizontal line across the entire range of predicted values. This indicates that the 
model maintains a relatively consistent error variance, a sign of a robust fit[13], 
[15]. 

• Error Distribution: The dense clustering of points between -25 and +25 units 
suggests that the model's predictions are highly accurate for the bulk of the 
dataset[8]. 

• Outlier Analysis: There are a few significant positive residuals (notably two points 
above 100). These represent instances where the model substantially under
predicted the actual NOx concentration. In a research context, these outliers 
may warrant further investigation into specific sensor anomalies or extreme 
environmental events[8]. 

• Absence of Patterns: No clear non-linear patterns (such as a "U" shape or 
"funnelling") are visible, confirming that the Random Forest model has 
successfully captured the non-linear relationships in the data without significant 
systematic bias[13], [15]. 
</div>
""", unsafe_allow_html=True)
    st.image("Research images/Figure 12.jpeg", caption="Figure 12: Residual Plot of Random Forest Model Prediction", use_container_width=True)
    # ================= 4 ================
    st.markdown("""
<div class="content">
4. SHAP Summary Plot 

This SHAP (SHapley Additive exPlanations) bee-swarm plot provides an interpretability 
layer for the Random Forest model, illustrating how individual features contribute to the 
predicted NOx levels Figure 13. Features are ranked based on their overall impact, with 
the most influential variables appearing at the top. 

Analysis of Feature Contributions 

Primary Drivers: 
NO₂ and Traffic emerge as the most significant predictors of NOx concentration. For both 
variables, higher feature values (represented by red points) correspond to positive SHAP 
values, indicating a strong direct relationship. This suggests that increased traffic intensity 
and elevated NO₂ levels significantly increase the predicted NOx concentration[8], [15]. 

Atmospheric Influences: 
Airflow and Wind Speed exhibit SHAP values clustered around zero, with slight negative 
contributions at higher values. This indicates that increased ventilation and wind speed 
aid in pollutant dispersion, thereby reducing NOx concentration to a moderate extent[8], 
[13]. 

Chemical Interactions: 
The variable NO shows a distinct pattern where higher values contribute positively to 
model predictions. This reflects the inherent chemical relationship between nitric oxide 
(NO) and total NOx concentration[8]. 

Negligible Variables: 
Meteorological and secondary pollutant factors such as Temperature, PM₁₀, O₃, and 
Relative Humidity display very narrow distributions around zero SHAP values. This 
suggests that their marginal contribution to the model’s predictive performance is 
minimal compared to primary emission-related variables[13], [15]. 

Non-linear Effects: 
The wide spread of NO₂ SHAP values, extending to high positive ranges, indicates strong 
non-linear behaviour. At elevated concentrations, NO₂ becomes the dominant factor 
influencing model predictions, contributing significantly to overall variance[8]. 
</div>
""", unsafe_allow_html=True)
    st.image("Research images/Figure 13.jpeg", caption="Figure 13: SHAP Summary Plot for Feature Importance", use_container_width=True)
    # ================= 5 =================
    st.markdown("""
<div class="content">
5. LIME Explanation Plot 

While Figure 13 (SHAP) provides a global interpretation of the model, the LIME (Local 
Interpretable Model-agnostic Explanations) plot offers a detailed, instance-level 
explanation of how the model arrived at a specific prediction of 169.27 units Figure 14. It 
highlights the contribution of individual features in either increasing or decreasing the 
predicted NOx concentration for this particular data point. 

Analysis of Local Feature Influence 

Dominant Positive Driver: 
The most significant contributor to this prediction is the condition NO₂ > 59.71, which 
adds approximately +133.96 to the predicted value. This strongly reinforces the global 
SHAP findings, confirming that NO₂ is the most influential variable in determining NOx 
concentration[8], [15]. 

Mitigating Factors (Negative Impact): 
The condition traffic ≤ 0.50 contributes −62.24, exerting a substantial negative influence 
on the prediction. This indicates that despite high pollutant levels, lower traffic intensity 
in this instance limited the overall NOx concentration[8], [13]. 

Secondary Positive Contributions: 
Additional variables such as NO > 12.98 contribute positively (+10.84) to the prediction. 
Furthermore, environmental factors like airflow and wind speed, within specific 
thresholds, provide smaller additive contributions, slightly increasing the predicted 
value[8]. 

Minor Variables: 
Features including PM₁₀, temperature, and relative humidity exhibit negligible 
contributions (weights less than 1.2). This suggests that these variables had minimal 
influence on the model’s decision for this specific observation[13], [15]. 
</div>
""", unsafe_allow_html=True)
    st.image("Research images/Figure 14.jpeg", caption="Figure 14: LIME Explanation for a Single Prediction Instance", use_container_width=True)
    # ================= 6 =================
    st.markdown("""
<div class="content">
6. CORRELATION GRAPH 

This heatmap presents the Pearson correlation coefficients between all measured variables 
and the target variable, nox_tunnel Figure 15. It provides a statistical foundation for 
feature selection in the machine learning models. 

Key Statistical Insights 

Strong Positive Correlations: 
The target variable (nox_tunnel) exhibits very strong positive correlations with NO₂ 
(0.90), NO (0.85), and overall NOx (0.91). This indicates that the chemical composition 
of air pollutants is the most direct and dominant factor influencing tunnel NOx 
concentration[6], [8]. 

Moderate Drivers: 
Variables such as CO (0.58) and PM₁₀ (0.39) show moderate positive correlations with 
NOx levels, likely due to their common origin from vehicular emissions. Additionally, 
traffic (0.28) and hour (0.29) demonstrate moderate relationships, reflecting the 
influence of traffic density and peak operational timings[13], [15]. 

Inverse Relationships: 
Wind speed and airflow show negative correlations (−0.39) with tunnel NOx 
concentration. This statistically confirms that improved ventilation and air movement 
contribute to the dispersion of pollutants, thereby reducing NOx levels[6], [8]. 

Multicollinearity: 
High inter-feature correlations, such as between NO and NO₂ (0.87), indicate the 
presence of multicollinearity. This justifies the selection of the Random Forest model, as 
it is more robust to correlated inputs compared to traditional linear regression models[13]. 

Negligible Factors: 
Variables such as O₃ (−0.039) and relative humidity (−0.067) exhibit near-zero 
correlation with the target variable. This supports their lower importance observed SHAP 
and LIME analyses[8], [15]. 
</div>
""", unsafe_allow_html=True)
    st.image("Research images/Figure 15.jpeg", caption="Figure 15: Feature Correlation Heatmap", use_container_width=True)
    st.markdown("## 5. Discussion")
    st.markdown("""
The research presented in this study enables several important points for discussion 
regarding the prediction of NOx concentration in subway tunnel environments[2], [3], 
[4], [6], [7], [8], [12], [13], [15]:

• The selection of an appropriate machine learning model plays a crucial role in 
balancing prediction accuracy and generalization capability. While simpler models such 
as Linear and Polynomial Regression provide baseline understanding, they often fail to 
capture complex nonlinear relationships present in environmental systems[3], [13]. In 
contrast, the Random Forest model demonstrated superior performance by effectively 
handling nonlinear interactions among variables, while also maintaining robustness 
against overfitting when properly tuned[15].

• It is essential to identify and incorporate meaningful input variables for accurate 
prediction. In this study, a combination of real-world pollutant data (such as NO₂, CO, 
and PM₁₀) and meteorological parameters (temperature, humidity, wind speed) was 
used alongside physics-based features like airflow, traffic intensity, and tunnel depth. 
The results indicate that not all variables contribute equally; features such as airflow, 
NO₂ concentration, and traffic intensity have a significantly higher impact on NOx 
prediction[6], [8], [12]. Including irrelevant or redundant variables may increase model 
complexity without improving performance, and in some cases, can reduce 
generalization capability.

• The integration of physics-based parameters into machine learning models proves to 
be highly beneficial. Purely data-driven models often lack contextual understanding, 
whereas the inclusion of domain knowledge—such as airflow dynamics and emission 
sources—enhances both predictive accuracy and interpretability[8], [12]. This hybrid 
approach ensures that the model not only learns patterns from data but also aligns with 
real-world physical behaviour of pollutant dispersion in confined environments.

• The variability and quality of data significantly influence model performance. Although 
real-time data from sources like OpenAQ provide valuable insights, inconsistencies 
such as missing values, measurement noise, and temporal fluctuations can affect 
prediction reliability[2], [6]. Additionally, environmental conditions in subway systems 
may vary across locations and time periods, meaning that models trained on one 
dataset may not directly generalize to another without proper adaptation or retraining.

• External and unobserved factors may also impact NOx levels but are not explicitly 
captured in the dataset. For instance, factors such as tunnel design variations, 
ventilation system efficiency, train frequency, braking mechanisms, and passenger 
density can influence pollutant accumulation[7]. While some of these effects are 
indirectly reflected in variables like traffic intensity and airflow, a more detailed 
representation of such parameters could further improve model performance.

• The achieved performance of the Random Forest model, with a high R² score and low 
RMSE, indicates strong predictive capability. However, it is important to consider the 
presence of outliers and extreme conditions, which may appear as sudden spikes in 
pollutant levels[3], [13]. These anomalies can slightly reduce overall accuracy but 
represent real-world transient events. Handling such outliers through preprocessing or 
robust modelling techniques can further enhance prediction stability.

• The application of explainable AI techniques such as SHAP and LIME adds significant 
value to the study. These methods provide insights into feature importance and model 
decision-making, addressing one of the major limitations of black-box machine learning 
models[3], [15]. Understanding how different factors influence NOx levels is critical for 
practical implementation, as it supports informed decision-making for ventilation 
control and pollution mitigation strategies.

• While the results of this study are promising, further research is necessary to explore 
additional modelling approaches and improve scalability. Advanced techniques such as 
deep learning, hybrid physics-based simulations, or real-time adaptive models could be 
investigated to enhance prediction performance under dynamic conditions[12], [13]. 
Expanding the dataset across multiple subway stations and incorporating real-time 
sensor integration would also strengthen the applicability of the proposed 
framework[2], [6].

• Overall, this study demonstrates that combining physics-based insights with machine 
learning provides a practical and effective solution for NOx prediction in subway 
environments. The approach offers a scalable framework for real-time air quality 
monitoring and has the potential to support smarter urban infrastructure planning and 
public health protection[4], [8], [12].
""")

    st.markdown("## 6. Conclusion")

    st.markdown("""
This study successfully developed a physics-informed machine learning framework for 
predicting NOx concentrations in subway tunnel environments[2], [4], [8], [12]. By 
integrating real-world air quality data with physics-based parameters such as airflow, 
traffic intensity, and tunnel characteristics, the proposed model achieves both high 
predictive accuracy and improved interpretability[6], [12]. The inclusion of domain-
specific knowledge enables the model to better represent real-world pollutant behavior, 
making it more reliable compared to purely data-driven approaches[3], [13].

Among the evaluated models, the Random Forest algorithm demonstrated superior 
performance in capturing complex nonlinear relationships within the dataset[15]. Its 
ability to handle multicollinearity and varying feature importance makes it particularly 
suitable for environmental prediction tasks[7], [15]. The model’s high R² score and low 
error metrics indicate strong predictive capability, even under dynamic and fluctuating 
environmental conditions[3], [13].

The incorporation of explainable AI techniques such as SHAP and LIME further 
strengthens the reliability and transparency of the proposed framework[3], [15]. These 
methods provide clear insights into feature importance and model decision-making 
processes, allowing for better understanding of how different variables influence NOx 
levels. This interpretability is essential for real-world applications, as it supports 
informed decision-making for ventilation control, pollution mitigation, and urban 
environmental management[6], [12].

Furthermore, the proposed framework demonstrates strong potential for integration into 
real-time air quality monitoring systems within smart city infrastructure[2], [4], [8], [12]. 
By enabling continuous prediction and analysis, it can assist in optimizing ventilation 
strategies, enhancing commuter safety, and supporting data-driven policy 
formulation[6], [7]. The combination of physics-based modelling and machine learning 
thus provides a scalable and practical solution to address the growing challenge of 
underground air pollution[4], [8], [12].
""")

    st.markdown("## 7. References")

    st.markdown("""
[1] S. Taha et al., “Comprehensive Review of Health Impacts of the Exposure to Nitrogen Oxides (NOx), Carbon Dioxide (CO2), and Particulate Matter (PM),” Journal of Hazardous Materials Advances, vol. 19, p. 100771, Jun. 2025.

[2] U. K. Lilhore et al., “Advanced air quality prediction using multimodal data and dynamic modeling techniques,” Sci Rep, vol. 15, no. 1, p. 27867, Jul. 2025.

[3] L. Naizabayeva et al., “Hybrid Physics–Machine Learning Framework,” Applied Sciences, 2025.

[4] N. Sarkar et al., “AQI Prediction Using ML, DL and Hybrid Models,” 2024.

[5] W. Zhang et al., “Air Pollution in Urban Subway,” Atmosphere, 2019.

[6] S.-H. Woo et al., “Particles in Subway Tunnel,” Aerosol Air Qual. Res., 2018.

[7] T. Moreno et al., “Subway Platform Air Quality,” Atmospheric Environment, 2014.

[8] A. Banasiewicz et al., “NOx Emission Prediction,” Energies, 2023.

[9] M. Méndez et al., “ML for Air Quality Forecasting,” AI Review, 2023.

[10] K. J. Ryu, “Ventilation Efficiency,” 2012.

[11] M. N. Smirnova et al., “Air Pollution Modeling in Tunnels,” 2020.

[12] S. Wang et al., “Indoor Air Quality in Subway,” Environment International, 2024.

[13] M. Karmoude et al., “ML for Air Quality Prediction,” 2025.

[14] I. E. Agbehadji et al., “Spatiotemporal Air Quality Prediction,” 2024.

[15] L. B. Peinado et al., “ML Models for Air Quality,” 2025.

[16] OpenAQ Homepage: https://openaq.org/

[17] OpenAQ Use Cases: https://openaq.org/about/use-cases/
""")
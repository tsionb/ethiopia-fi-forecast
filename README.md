# ethiopia-fi-forecast

---


##  Task 1: Data Exploration & Enrichment

###  Objective

Understand the unified financial inclusion dataset for Ethiopia and enrich it with relevant indicators and events to support forecasting of **Access** and **Usage**.

---

###  Dataset Overview

* **Source:** Global Findex, operators, policy reports
* **Total records:** **57**

  * **30** observations
  * **10** events
  * **14** impact links
  * **3** policy targets
* **Time coverage:** **2011 – 2024**
* **Core pillars:**

  * **Access** – Account Ownership
  * **Usage** – Digital Payments

---

###  Schema Understanding

All records follow a **unified schema**, differentiated by `record_type`:

* `observation` → measured indicators
* `event` → policies, product launches, infrastructure milestones
* `impact_link` → modeled relationships between events and indicators
* `target` → official national goals

**Key design principle:**
Events are **not pre-assigned** to pillars to avoid bias; their effects are captured via `impact_link`.

---

###  Data Enrichment Performed

* Added **infrastructure and ecosystem indicators** (e.g., mobile money users, interoperability milestones)
* Added **missing national events** relevant to financial inclusion
* Created additional **impact_link records** to model event–indicator relationships

Each new record includes:

* **Source URL**
* **Original text**
* **Confidence level (High / Medium / Low)**
* **Collection date & notes**

 All changes are documented in **`data_enrichment_log.md`**

---

###  Key Outcomes

* Dataset cleaned and validated
* Schema fully understood and documented
* Enriched dataset ready for exploratory analysis and modeling

---

##  Task 2: Exploratory Data Analysis (EDA)

###  Objective

Analyze trends, patterns, and constraints in Ethiopia’s financial inclusion journey and identify drivers of **Access** and **Usage**.

---

###  Dataset Summary

* **Account Ownership (Access):**

  * **2011:** 14%
  * **2014:** 22% (**+8pp**)
  * **2017:** 35% (**+13pp**)
  * **2021:** 46% (**+11pp**)
  * **2024:** 49% (**+3pp**)

* **Digital Payment Usage (Usage):**

  * **2024:** ~**35%** (single Findex observation)

* **Mobile Money Ownership:**

  * **2021:** ~4.7%
  * **2024:** **9.45%**

---

###  Key Visual Analyses

* Account ownership trend (2011–2024)
* Mobile money growth over time
* Major financial inclusion events by year
* Indicator coverage and data completeness
* Yearly growth rates in account ownership

---

###  Key Insights

1. **Strong long-term growth** in account ownership, but **sharp slowdown** after 2021 (**+3pp** only).
2. **Mobile money expansion** has not translated proportionally into account ownership.
3. **Usage grows faster than access**, indicating many accounts are underutilized.
4. **Digital payment usage data is sparse**, limiting trend analysis.
5. **Infrastructure and policy events show delayed effects**, not immediate impacts.

---

###  Data Limitations

* Only **one official Findex data point (2024)** for digital payment usage.
* Limited disaggregation by **gender** and **region**.
* High uncertainty due to **sparse time series**.

**Mitigation:**
Mobile money indicators and transaction metrics are used as **proxy variables** for usage trends.

---

###  Key Outcomes

* Clear understanding of Ethiopia’s financial inclusion dynamics
* Evidence-based hypotheses for event impact modeling
* Strong analytical foundation for forecasting (Task 3 & 4)

---

##  Task 3: Event Impact Modeling

### **Objective**
Model how events (policy changes, product launches, infrastructure investments) affect Ethiopia's financial inclusion indicators.

### **Key Deliverables**
- `event_indicator_matrix.csv` – Raw event-impact matrix
- `refined_event_matrix.csv` – Adjusted impact estimates
- `task3_methodology.md` – Modeling approach documentation
- `impact_modeling.ipynb` – Analysis notebook

### **Refined Impact Matrix**
| Event | ACC_OWNERSHIP | ACC_MM_ACCOUNT | USG_DIGITAL_PAYMENT |
|-------|---------------|----------------|---------------------|
| Telebirr Launch | +2.4pp | +6.0pp | +2.0pp |
| M-Pesa Entry | +1.05pp | +10.0pp | +1.0pp |
| NFIS Policy | +3.0pp | 0pp | +1.5pp |

### **Key Insights**
- Telebirr launch had strongest mobile money impact
- Policy effects show 6–12 month lag
- Comparable country evidence used where Ethiopian data sparse

---

##  Task 4: Forecasting Access & Usage

### **Objective**
Forecast Account Ownership (Access) and Digital Payment Usage for 2025–2027.

### **Forecast Results**

#### **Account Ownership (ACCESS)**
| Year | Optimistic | Base | Pessimistic |
|------|------------|------|-------------|
| 2025 | 67.2% | 51.7% | 36.2% |
| 2026 | 73.7% | 56.7% | 39.7% |
| 2027 | 76.4% | 58.8% | 41.1% |

#### **Digital Payment Usage (USAGE)**
| Year | Optimistic | Base | Pessimistic |
|------|------------|------|-------------|
| 2025 | 40.0% | 38.0% | 36.0% |
| 2026 | 45.0% | 41.0% | 37.0% |
| 2027 | 50.0% | 44.0% | 38.0% |

### **Methodology**
- **Linear Regression**: Baseline trend extrapolation
- **Scenario Analysis**: Optimistic/Base/Pessimistic scenarios
- **Event-Augmented Model**: Incorporated major event impacts
- **95% Confidence Intervals**: Quantified uncertainty

### **Key Findings**
- **Base Scenario**: 52–59% account ownership by 2027
- **Optimistic Scenario**: Could meet NFIS 60% target by 2025
- **Digital Payments**: Growing faster than account ownership
- **Mobile Money**: Key driver of digital payment adoption

---

##  Task 5: Interactive Dashboard** 

### **Objective**
Create an interactive dashboard for stakeholders to explore data, understand impacts, and view forecasts.

### **Dashboard Structure**
```
 dashboard/
├── app.py              # Main Streamlit application
├── pages/
│   ├── 01_Overview.py  # Key metrics & introduction
│   ├── 02_Trends.py    # Historical data analysis
│   ├── 03_Forecasts.py # Future predictions
│   └── 04_Analysis.py  # Interactive tools
└── requirements.txt    # Dependencies
```

### **Features**
 **Multi-page navigation** – 4 dedicated pages  
 **Interactive charts** – Plotly visualizations from Tasks 2–4  
 **Data filtering** – Year, indicator, scenario selectors  
 **Forecast scenario toggles** – Optimistic/Base/Pessimistic  
 **Download functionality** – Export charts and data  
 **Mobile-responsive design** – Works on all devices  
 **Professional styling** – Clean, intuitive interface  

### **Pages**
1. **Overview** – Key metrics and project introduction
2. **Trends** – Historical financial inclusion analysis
3. **Forecasts** – 2025–2027 predictions with confidence intervals
4. **Analysis** – Interactive tools for deeper exploration

### **Quick Start**
```bash
# 1. Install dependencies
pip install -r dashboard/requirements.txt

# 2. Run the dashboard
streamlit run dashboard/app.py
```

---

##  **Getting Started**

### **Prerequisites**
- Python 3.8+
- Git
- Jupyter Notebook (for Tasks 1–4)

### **Setup**
```bash
# Clone repository
git clone https://github.com/your-username/ethiopia-fi-forecast.git
cd ethiopia-fi-forecast

# Install dependencies
pip install -r requirements.txt

# Run Task 3 analysis
jupyter notebook task3/impact_modeling.ipynb

# Run Task 4 forecasting
jupyter notebook task4/forecasting.ipynb

# Launch dashboard
streamlit run dashboard/app.py
```

### **Data Flow**
```
Task 1 (Data) → Task 2 (EDA) → Task 3 (Modeling) → Task 4 (Forecasting) → Task 5 (Dashboard)
```

---

##  **Key Insights Summary**

### **Drivers of Financial Inclusion**
1. **Mobile Money Expansion** – Telebirr (54M+ users), M-Pesa (10M+ users)
2. **Policy Support** – National Financial Inclusion Strategies
3. **Infrastructure Growth** – 4G coverage increased from 37.5% to 70.8% (2023–2025)
4. **Market Competition** – Multiple players driving innovation

### **Forecast Implications**
- **Optimistic**: Ethiopia could reach 60% account ownership by 2025
- **Base**: Steady growth to ~59% by 2027
- **Pessimistic**: Potential stagnation at 41% if challenges persist

### **Recommendations**
1. **Prioritize digital infrastructure** – Expand 4G and agent networks
2. **Monitor competition** – Ensure healthy market dynamics
3. **Targeted interventions** – Address gender and regional gaps
4. **Regular data collection** – Advocate for annual Findex surveys

---

##  **Repository Structure**
```
ethiopia-fi-forecast/
├── data/               # Raw and processed data
├── notebooks/          # Jupyter notebooks (Tasks 1-4)
├── dashboard/          # Streamlit dashboard (Task 5)
├── reports/            # Documentation and reports
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

---

##  **Stakeholder Value**
- **Policymakers**: Evidence-based insights for financial inclusion strategies
- **Mobile Money Operators**: Market intelligence and growth projections
- **Development Partners**: Monitoring and evaluation framework
- **Researchers**: Replicable methodology and open data







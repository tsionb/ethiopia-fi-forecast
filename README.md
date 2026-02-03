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





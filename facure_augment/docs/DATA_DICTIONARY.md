# Data Dictionary

Full schema documentation for all 21 datasets in `facure_augment/data/facure/`.

---

## Quick Reference

| Dataset | Rows | Cols | Domain | Chapters |
|---------|------|------|--------|----------|
| ak91.csv | 329,509 | 5 | Labor Economics | 08 IV |
| app_engagement_push.csv | 10,000 | 3 | Mobile App | 09 LATE |
| billboard_impact.csv | 4,600 | 3 | Marketing | 13 DiD |
| collections_email.csv | 5,000 | 6 | Finance | 07 Controls |
| customer_features.csv | 10,000 | 4 | Retail | 17 Prediction |
| customer_transactions.csv | 10,000 | 32 | Retail | 17 Prediction |
| drinking.csv | 50 | 19 | Public Health | 16 RDD |
| enem_scores.csv | 37,941 | 4 | Education | 01, 03, 06 |
| hospital_treatment.csv | 80 | 4 | Healthcare | 07 Colliders |
| ice_cream_sales.csv | 10,000 | 5 | Retail | 05b, 22 DML |
| ice_cream_sales_rnd.csv | 5,000 | 5 | Retail | 18-19 HTE |
| invest_email.csv | 5,000 | 11 | Finance | 11 PS, A3 |
| invest_email_biased.csv | 15,000 | 8 | Finance | 21 Meta |
| invest_email_rnd.csv | 15,000 | 8 | Finance | 20-21 CATE |
| learning_mindset.csv | 10,391 | 13 | Education | 11-12 PS/DR |
| medicine_impact_recovery.csv | 20,000 | 5 | Healthcare | 10 Matching |
| online_classroom.csv | 323 | 10 | Education | 02, 05 RCT |
| sheepskin.csv | 46 | 5 | Labor Economics | 16 Fuzzy RDD |
| smoking.csv | 1,209 | 9 | Public Health | 15, 25, A1 SCM |
| trainees.csv | 40 | 4 | Labor Economics | 10 Matching |
| wage.csv | 935 | 16 | Labor Economics | 05, 06 |

---

## Detailed Schemas

### ak91.csv

**Source**: Angrist & Krueger (1991) — "Does Compulsory School Attendance Affect Schooling and Earnings?"
**Rows**: 329,509 | **Columns**: 5
**Used In**: Chapter 08 (Instrumental Variables)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| log_wage | float | Log weekly wage | Continuous |
| years_of_schooling | float | Years of completed education | ~8-20 |
| year_of_birth | float | Birth year | 30-39 (1930-1939) |
| quarter_of_birth | float | Quarter of birth (INSTRUMENT) | 1-4 |
| state_of_birth | float | State FIPS code | 1-56 |

**Causal Question**: Does education increase wages?
**Treatment**: years_of_schooling (endogenous)
**Instrument**: quarter_of_birth (compulsory schooling laws)
**Outcome**: log_wage
**Design**: IV/2SLS

---

### app_engagement_push.csv

**Source**: Facure Ch. 9 (simulated mobile app RCT)
**Rows**: 10,000 | **Columns**: 3
**Used In**: Chapter 09 (Non-Compliance & LATE)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| in_app_purchase | float | In-app purchase amount (OUTCOME) | ≥0 |
| push_assigned | int | Assigned to push notification (Z) | 0/1 |
| push_delivered | int | Actually received push (T) | 0/1 |

**Causal Question**: Do push notifications increase purchases?
**Assignment**: push_assigned (randomized)
**Treatment**: push_delivered (with non-compliance)
**Outcome**: in_app_purchase
**Design**: RCT with one-sided non-compliance

---

### billboard_impact.csv

**Source**: Facure Ch. 13 (simulated marketing study)
**Rows**: 4,600 | **Columns**: 3
**Used In**: Chapter 13 (Difference-in-Differences)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| deposits | float | Customer deposits in R$ (OUTCOME) | Continuous |
| poa | int | Porto Alegre indicator (TREATED) | 0=Florianópolis, 1=POA |
| jul | int | July indicator (POST) | 0=May, 1=July |

**Causal Question**: Do billboard ads increase bank deposits?
**Treatment**: poa (city-level, Porto Alegre treated in June)
**Outcome**: deposits
**Design**: DiD (2×2 panel, May vs July)

---

### collections_email.csv

**Source**: Facure Ch. 7 (simulated debt collection)
**Rows**: 5,000 | **Columns**: 6
**Used In**: Chapter 07 (Beyond Confounders)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| payments | float | Payment amount (OUTCOME) | ≥0 |
| email | int | Sent collection email (TREATMENT) | 0/1 |
| opened | int | Email opened (MEDIATOR) | 0/1 |
| agreement | int | Has payment agreement | 0/1 |
| credit_limit | float | Credit limit | Continuous |
| risk_score | float | Credit risk score | Continuous |

**Causal Question**: Do collection emails increase payments?
**Treatment**: email
**Outcome**: payments
**Design**: Observational (good/bad controls exercise)
**Note**: `opened` is a post-treatment variable (mediator)

---

### customer_features.csv

**Source**: Facure Ch. 17 (simulated retail)
**Rows**: 10,000 | **Columns**: 4
**Used In**: Chapter 17 (Predictive Models)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| customer_id | int | Unique customer ID | 1-10000 |
| region | str | Geographic region | Category |
| income | float | Annual income | Continuous |
| age | int | Age in years | ~18-80 |

**Causal Question**: (Prediction, not causation)
**Design**: Customer segmentation features

---

### customer_transactions.csv

**Source**: Facure Ch. 17 (simulated retail)
**Rows**: 10,000 | **Columns**: 32
**Used In**: Chapter 17 (Predictive Models)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| customer_id | int | Unique customer ID | 1-10000 |
| cacq | float | Customer acquisition cost | Continuous |
| day_0 to day_29 | float | Daily transaction amounts | ≥0 |

**Causal Question**: (Prediction — forecast LTV)
**Design**: Transaction time series for each customer

---

### drinking.csv

**Source**: Carpenter & Dobkin (2009) — "The Effect of Alcohol Consumption on Mortality"
**Rows**: 50 | **Columns**: 19
**Used In**: Chapter 16 (Regression Discontinuity)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| agecell | float | Age in months relative to 21 (RUNNING VAR) | ~19-23 |
| all | float | All-cause mortality rate (OUTCOME) | Per 100,000 |
| allfitted | float | Fitted all-cause mortality | Per 100,000 |
| internal | float | Internal mortality rate | Per 100,000 |
| external | float | External mortality rate | Per 100,000 |
| alcohol | float | Alcohol-related mortality | Per 100,000 |
| homicide | float | Homicide rate | Per 100,000 |
| suicide | float | Suicide rate | Per 100,000 |
| mva | float | Motor vehicle accidents (OUTCOME 2) | Per 100,000 |
| ... | | Other mortality causes | |

**Causal Question**: Does legal drinking age affect mortality?
**Treatment**: Legal to drink (age ≥ 21)
**Running Variable**: agecell (age in months)
**Cutoff**: 21 years
**Outcome**: Mortality rates (all, mva, alcohol)
**Design**: Sharp RDD

---

### enem_scores.csv

**Source**: ENEM (Brazilian national exam, aggregated)
**Rows**: 37,941 | **Columns**: 4
**Used In**: Chapters 01, 03, 06 (intro, stats, grouped)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| year | int | Exam year | 2005-2015 |
| school_id | int | School identifier | Unique |
| number_of_students | int | Students tested | ≥1 |
| avg_score | float | Average exam score (OUTCOME) | ~300-700 |

**Causal Question**: (Varies by chapter — heteroskedasticity, school effects)
**Design**: Panel of schools over time
**Note**: Demonstrates heteroskedasticity by school size

---

### hospital_treatment.csv

**Source**: Facure Ch. 7 (simulated)
**Rows**: 80 | **Columns**: 4
**Used In**: Chapter 07 (Collider example)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| hospital | str | Hospital name | "General", "Specialist" |
| treatment | int | Received treatment | 0/1 |
| severity | float | Illness severity (COLLIDER) | Continuous |
| days | float | Days in hospital (OUTCOME) | ≥0 |

**Causal Question**: Does treatment reduce hospital stay?
**Treatment**: treatment
**Outcome**: days
**Design**: Observational (collider bias demonstration)
**Note**: `severity` is a collider (affected by hospital AND treatment)

---

### ice_cream_sales.csv

**Source**: Facure Ch. 22 (simulated pricing)
**Rows**: 10,000 | **Columns**: 5
**Used In**: Chapters 05b, 22 (DML)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| temp | float | Temperature (°C) | ~15-35 |
| weekday | int | Day of week | 0-6 |
| cost | float | Unit cost | Continuous |
| price | float | Sale price (TREATMENT) | Continuous |
| sales | float | Units sold (OUTCOME) | ≥0 |

**Causal Question**: What is the price elasticity of demand?
**Treatment**: price (continuous, confounded by temp/cost)
**Outcome**: sales
**Design**: Observational (DML for price elasticity)
**Note**: temp confounds price and sales (hot → high price, high sales)

---

### ice_cream_sales_rnd.csv

**Source**: Facure Ch. 18-19 (simulated, randomized version)
**Rows**: 5,000 | **Columns**: 5
**Used In**: Chapters 18-19 (HTE evaluation)

Same schema as `ice_cream_sales.csv` but with randomized prices.

**Causal Question**: Evaluate CATE models with randomized test set
**Design**: RCT (prices randomized for evaluation)

---

### invest_email.csv

**Source**: Facure Ch. 11 (simulated investment marketing)
**Rows**: 5,000 | **Columns**: 11
**Used In**: Chapters 11, A3 (PS, IPTW)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| age | float | Customer age | ~20-70 |
| income | float | Annual income | Continuous |
| insurance | int | Has insurance product | 0/1 |
| invested | float | Investment amount (OUTCOME) | ≥0 |
| em1_ps | float | Propensity for email 1 | 0-1 |
| em2_ps | float | Propensity for email 2 | 0-1 |
| em3_ps | float | Propensity for email 3 | 0-1 |
| em1 | int | Received email 1 (TREATMENT) | 0/1 |
| em2 | int | Received email 2 | 0/1 |
| em3 | int | Received email 3 | 0/1 |
| converted | int | Converted to investor | 0/1 |

**Causal Question**: Do marketing emails increase investment?
**Treatment**: em1, em2, em3 (multiple treatments)
**Outcome**: invested, converted
**Design**: Observational with known propensity scores

---

### invest_email_biased.csv

**Source**: Facure Ch. 21 (simulated, selection bias)
**Rows**: 15,000 | **Columns**: 8
**Used In**: Chapter 21 (Meta-learners training)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| age | float | Customer age | ~20-70 |
| income | float | Annual income | Continuous |
| insurance | int | Has insurance product | 0/1 |
| invested | float | Previous investment | ≥0 |
| em1 | int | Received email 1 | 0/1 |
| em2 | int | Received email 2 | 0/1 |
| em3 | int | Received email 3 | 0/1 |
| converted | int | Converted (OUTCOME) | 0/1 |

**Causal Question**: (Training set with selection bias)
**Design**: Observational (treatment assigned based on confounders)

---

### invest_email_rnd.csv

**Source**: Facure Ch. 20-21 (simulated, randomized)
**Rows**: 15,000 | **Columns**: 8
**Used In**: Chapters 20-21 (CATE evaluation)

Same schema as `invest_email_biased.csv` but randomized.

**Causal Question**: Evaluate CATE learners with randomized test
**Design**: RCT (emails randomized)

---

### learning_mindset.csv

**Source**: National Study of Learning Mindsets (Yeager et al., 2019)
**Rows**: 10,391 | **Columns**: 13
**Used In**: Chapters 11-12 (PS, Doubly Robust)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| schoolid | int | School identifier | ~70 schools |
| intervention | int | Growth mindset treatment (T) | 0/1 |
| achievement_score | float | Academic achievement (OUTCOME) | Standardized |
| success_expect | float | Success expectation | Standardized |
| ethnicity | int | Student ethnicity | Coded |
| gender | int | Student gender | 0/1 |
| frst_in_family | int | First in family to college | 0/1 |
| school_urbanicity | int | Urban/suburban/rural | 1-3 |
| school_mindset | float | School-level mindset culture | Standardized |
| school_achievement | float | School-level achievement | Standardized |
| school_ethnic_minority | float | % Minority students | 0-1 |
| school_poverty | float | % Free lunch | 0-1 |
| school_size | float | School size | Continuous |

**Causal Question**: Does growth mindset intervention improve achievement?
**Treatment**: intervention
**Outcome**: achievement_score
**Design**: RCT (school-level randomization, student covariates)

---

### medicine_impact_recovery.csv

**Source**: Facure Ch. 10 (simulated medical study)
**Rows**: 20,000 | **Columns**: 5
**Used In**: Chapter 10 (Matching)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| sex | int | Patient sex | 0/1 |
| age | float | Patient age | ~20-80 |
| severity | float | Illness severity | Continuous |
| medication | int | Received medication (TREATMENT) | 0/1 |
| recovery | float | Recovery time days (OUTCOME) | ≥0 |

**Causal Question**: Does medication reduce recovery time?
**Treatment**: medication (assigned based on severity)
**Outcome**: recovery
**Design**: Observational (matching on severity, age, sex)

---

### online_classroom.csv

**Source**: Facure Ch. 2, 5 (hypothetical education RCT)
**Rows**: 323 | **Columns**: 10
**Used In**: Chapters 02, 05 (RCT, regression)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| gender | int | Student gender | 0=female, 1=male |
| asian | float | Asian ethnicity | 0/1/NaN |
| black | float | Black ethnicity | 0/1/NaN |
| hawaiian | float | Hawaiian ethnicity | 0/1/NaN |
| hispanic | float | Hispanic ethnicity | 0/1/NaN |
| unknown | float | Unknown ethnicity | 0/1/NaN |
| white | float | White ethnicity | 0/1/NaN |
| format_ol | int | Online format (TREATMENT) | 0=face-to-face, 1=online |
| format_blended | float | Blended format | 0/1 |
| falsexam | float | Final exam score (OUTCOME) | 0-100 |

**Causal Question**: Does online instruction affect exam performance?
**Treatment**: format_ol
**Outcome**: falsexam
**Design**: RCT (students randomly assigned to format)

---

### sheepskin.csv

**Source**: Clark & Martorell (2014) — "The Signaling Value of a High School Diploma"
**Rows**: 46 | **Columns**: 5
**Used In**: Chapter 16 (Fuzzy RDD)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| minscore | float | Min score to pass (RUNNING VAR) | ~-10 to +10 |
| person_years | float | Person-years in sample | Continuous |
| avgearnings | float | Average earnings (OUTCOME) | Continuous |
| receivehsd | float | Received HS diploma (TREATMENT) | 0-1 (compliance rate) |
| n | int | Sample size in bin | Continuous |

**Causal Question**: Does a HS diploma increase earnings (beyond human capital)?
**Treatment**: receivehsd (having diploma)
**Running Variable**: minscore (score relative to cutoff)
**Cutoff**: 0 (barely pass vs barely fail)
**Outcome**: avgearnings
**Design**: Fuzzy RDD (not everyone who passes gets diploma)

---

### smoking.csv

**Source**: Abadie et al. (2010) — "Synthetic Control Methods" (Proposition 99)
**Rows**: 1,209 | **Columns**: 9
**Used In**: Chapters 15, 25, A1 (SCM, SDID, Conformal)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| state | int | State identifier | 1-39 |
| year | int | Year | 1970-2000 |
| cigsale | float | Cigarette sales per capita (OUTCOME) | Packs/person |
| lnincome | float | Log income | Continuous |
| beer | float | Beer consumption | Continuous |
| age15to24 | float | % Age 15-24 | 0-1 |
| retprice | float | Retail cigarette price | Continuous |
| california | int | California indicator (TREATED) | 0/1 |
| after_treatment | int | Post-1988 (POST) | 0/1 |

**Causal Question**: Did Proposition 99 reduce cigarette consumption in California?
**Treatment**: california (treated in 1988)
**Outcome**: cigsale
**Design**: Synthetic control (California vs weighted donors)

---

### trainees.csv

**Source**: Facure Ch. 10 (simulated job training)
**Rows**: 40 | **Columns**: 4
**Used In**: Chapter 10 (Simple matching example)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| unit | int | Unit identifier | 1-40 |
| trainees | int | Received training (TREATMENT) | 0/1 |
| age | float | Age | ~20-50 |
| earnings | float | Earnings (OUTCOME) | Continuous |

**Causal Question**: Does job training increase earnings?
**Treatment**: trainees
**Outcome**: earnings
**Design**: Observational (simple matching on age)

---

### wage.csv

**Source**: Wooldridge "Introductory Econometrics" (NLS data)
**Rows**: 935 | **Columns**: 16
**Used In**: Chapters 05, 06 (Regression, Interactions)

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| wage | float | Hourly wage | Continuous |
| hours | float | Hours worked per week | ~0-80 |
| lhwage | float | Log hourly wage (OUTCOME) | Continuous |
| IQ | float | IQ score | ~60-150 |
| educ | int | Years of education | 0-20 |
| exper | int | Years of experience | 0-40 |
| tenure | int | Years at current job | 0-30 |
| age | int | Age | ~18-65 |
| married | int | Married | 0/1 |
| black | int | Black | 0/1 |
| south | int | Lives in South | 0/1 |
| urban | int | Lives in urban area | 0/1 |
| sibs | int | Number of siblings | 0-15 |
| brthord | int | Birth order | 1-10 |
| meduc | int | Mother's education | 0-20 |
| feduc | int | Father's education | 0-20 |

**Causal Question**: Returns to education, experience
**Treatment**: educ (endogenous)
**Outcome**: wage, lhwage
**Design**: Observational (regression with controls)

---

## Data Loading

All datasets can be loaded via `common.py`:

```python
from facure_augment.common import load_facure_data

# Load single dataset
df = load_facure_data("online_classroom.csv")

# Load with path
import pandas as pd
df = pd.read_csv("facure_augment/data/facure/online_classroom.csv")
```

---

## Data Source Citations

1. **Angrist & Krueger (1991)**: "Does Compulsory School Attendance Affect Schooling and Earnings?" *QJE*
2. **Carpenter & Dobkin (2009)**: "The Effect of Alcohol Consumption on Mortality" *AEJ: Applied*
3. **Abadie et al. (2010)**: "Synthetic Control Methods for Comparative Case Studies" *JASA*
4. **Yeager et al. (2019)**: "A National Experiment Reveals Where a Growth Mindset Improves Achievement" *Nature*
5. **Clark & Martorell (2014)**: "The Signaling Value of a High School Diploma" *JPE*
6. **Wooldridge**: "Introductory Econometrics: A Modern Approach"
7. **Facure**: "Causal Inference for the Brave and True" (simulated datasets)

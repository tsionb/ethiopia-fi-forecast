

## EVENT IMPACT MODELING METHODOLOGY

### 1. DATA SOURCES USED
• **Primary Data**: Ethiopia financial inclusion dataset (Tasks 1-2)
• **Impact Links**: Pre-defined relationships between events and indicators
• **Historical Validation**: Actual before/after data where available
• **Comparable Evidence**: Kenya, Tanzania, Rwanda case studies

### 2. MODELING APPROACH

#### Step 1: Event-Impact Matrix Creation
- Extracted all events from dataset (n=11 events)
- Joined with impact links (n=15 relationships)
- Created pivot matrix showing event → indicator effects
- Used impact_estimate values where available

#### Step 2: Historical Validation
For each major event:
1. Identified event date
2. Found indicator values before event
3. Found indicator values after event
4. Calculated actual change
5. Compared with estimated change

#### Step 3: Comparable Country Adjustment
When Ethiopian data insufficient:
1. Identified similar countries (Kenya, Tanzania, Rwanda)
2. Extracted their impact rates
3. Applied adjustment factors for Ethiopia context:
   - Population size: 0.8x (slower due to size)
   - Infrastructure: 0.9x (developing)
   - Policy support: 1.2x (stronger)
   - Competition: 1.3x (multiple players)

#### Step 4: Impact Refinement
Based on validation:
- Increased Telebirr's mobile money impact (actual growth faster)
- Decreased M-Pesa's account ownership impact (limited so far)
- Increased policy impacts (strong government support)

### 3. KEY ASSUMPTIONS

#### Temporal Assumptions
1. **Immediate effects**: Some impacts occur within 3 months
2. **Lagged effects**: Policy impacts take 6-12 months
3. **Cumulative effects**: Multiple events have additive impacts

#### Impact Assumptions
1. **Linear relationships**: Simple additive model
2. **Independent events**: Events don't interfere with each other
3. **Constant environment**: No major economic shocks

#### Data Assumptions
1. **Missing data**: Used comparable evidence when Ethiopian data missing
2. **Measurement consistency**: Findex surveys comparable over time
3. **Indicator reliability**: Official reports are accurate

### 4. LIMITATIONS

#### Data Limitations
1. **Sparse time series**: Only 5 data points for most indicators
2. **Missing counterfactual**: Cannot know what would have happened without events
3. **Confounding factors**: Other factors (economy, demographics) not controlled

#### Modeling Limitations
1. **Simple additive model**: Doesn't capture complex interactions
2. **Static estimates**: Doesn't account for changing impact over time
3. **No uncertainty quantification**: Point estimates only

### 5. UNCERTAINTY LEVELS

**High Confidence (★ ★ ★)**
- Telebirr mobile money impact (direct observation)
- M-Pesa user growth (operator reports)

**Medium Confidence (★ ★ ☆)**
- Policy impacts (comparable country evidence)
- Digital payment adoption (challenge data)

**Low Confidence (★ ☆ ☆)**
- Lag timing estimates
- Interaction effects between events
- Long-term sustainability of impacts

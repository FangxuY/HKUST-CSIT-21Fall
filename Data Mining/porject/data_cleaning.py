# Title: CSIT5210 Research Project -- Goal 1
# Editor: Fangxu Yuan
# Date created: 4/15/2021
# Date edited: 6/02/2021

import pandas as pd
import datetime
import operator
import numpy as np
import matplotlib.pyplot as plt


def judgeLevel(df, str):
    if df[str].find(str):
        return 1
    else:
        return 0

# ---------------- read in dataset---------------------------------

VAERSDATA21 = pd.read_csv('./2021VAERSDATA.csv', encoding='utf-8', low_memory=False)
VAERSVAX21 = pd.read_csv('./2021VAERSVAX.csv', encoding='utf-8', low_memory=False)
VAERSSYMPTOMS21 = pd.read_csv('./2021VAERSSYMPTOMS.csv', encoding='utf-8', low_memory=False)

VAERSVAX21 = VAERSVAX21.loc[VAERSVAX21['VAX_TYPE'] == 'COVID19']

# merge by id and restrict to covid vaccine
data21 = pd.merge(VAERSDATA21, VAERSVAX21, on='VAERS_ID', how='left')
data21 = pd.merge(data21, VAERSSYMPTOMS21, on='VAERS_ID', how='left')

# ---------------- pre-processing---------------------------------
# remove unknown sex/manufactor or age <12
data21 = data21.drop(data21[data21['SEX'] == "U"].index)
data21 = data21.drop(data21[data21['VAX_MANU'] == "UNKNOWN MANUFACTURER"].index)
data21 = data21.drop(data21[data21['VAX_MANU'].isna()].index)
data21 = data21.drop(data21[data21['AGE_YRS'] < 12].index)
data21 = data21.drop(data21[data21['AGE_YRS'].isna()].index)

# redefine categorical variables
data21.loc[data21['OTHER_MEDS'].notna(), 'OTHER_MEDS'] = 1
data21.loc[data21['OTHER_MEDS'].isna(), 'OTHER_MEDS'] = 0
data21.rename(columns={'OTHER_MEDS': 'othermeds'}, inplace=True)
data21.loc[data21['CUR_ILL'].notna(), 'CUR_ILL'] = 1
data21.loc[data21['CUR_ILL'].isna(), 'CUR_ILL'] = 0
data21.rename(columns={'CUR_ILL': 'curr_ill'}, inplace=True)
data21.loc[data21['ALLERGIES'].notna(), 'ALLERGIES'] = 1
data21.loc[data21['ALLERGIES'].isna(), 'ALLERGIES'] = 0
data21.rename(columns={'ALLERGIES': 'allergies'}, inplace=True)
# 1 means female, 0 means male
data21.loc[data21['SEX'] == "F", 'SEX'] = 1
data21.loc[data21['SEX'] == "M", 'SEX'] = 0
data21.rename(columns={'SEX': 'sex'}, inplace=True)
data21.loc[data21['DISABLE'].notna(), 'DISABLE'] = 1
data21.loc[data21['DISABLE'].isna(), 'DISABLE'] = 0
data21.rename(columns={'DISABLE': 'disable'}, inplace=True)
# MODERNA = 0, PFIZER\BIONTECH = 2, JANSSEN = 3
data21.loc[data21['VAX_MANU'] == "MODERNA", 'VAX_MANU'] = 0
data21.loc[data21['VAX_MANU'] == "PFIZER\\BIONTECH", 'VAX_MANU'] = 2
data21.loc[data21['VAX_MANU'] == "JANSSEN", 'VAX_MANU'] = 3
data21.rename(columns={'VAX_MANU': 'manu'}, inplace=True)
data21['AGE_YRS'].astype("int")

# manipulate date variable
# 1. onset date and imputation
date_before = datetime.date(2020, 1, 1)
data21['ONSET_DATE'] = pd.to_datetime(data21['ONSET_DATE']).dt.date
data21.rename(columns={'ONSET_DATE': 'date'}, inplace=True)
data21 = data21.drop(data21[data21['date'] < date_before].index)
# data21['date'].plot(kind='bar')
# plt.show()
# 2. vaccination date and imputation
data21['VAX_DATE'] = pd.to_datetime(data21['VAX_DATE']).dt.date
data21.rename(columns={'VAX_DATE': 'date_vax'}, inplace=True)
data21 = data21.drop(data21[data21['date_vax'] < date_before].index)
# define duration
data21 = data21.drop(data21[data21['date_vax'] > data21['date']].index)
data21['dur'] = data21['date'] - data21['date_vax']

# ---------description plots---------------------------------
# symptom = data21[['SYMPTOM1', 'SYMPTOM2', 'SYMPTOM3', 'SYMPTOM4', 'SYMPTOM5']]

data21['Allergic'] = 0
data21['diabetes'] = 0
data21['hypertension'] = 0
data21['arthritis'] = 0
data21['Asthma'] = 0
data21['Migraine'] = 0
data21['copd'] = 0
data21['anxiety'] = 0
data21['obesity'] = 0
data21['depression'] = 0
data21['Thyroid'] = 0
data21['Anemia'] = 0
data21['Dementia'] = 0
data21['Cancer'] = 0
data21['Kidney'] = 0
data21['Hyperlipidemia'] = 0
data21['CVD'] = 0
data21['AF'] = 0

data21['HISTORY'] = data21['HISTORY'].astype(str)

# histogram showing frequency of top 15 common symptom
for index, row in data21.iterrows():
    if operator.contains(row['HISTORY'].lower(), 'allergic'):
        data21.at[index, 'Allergic'] = 1

    if operator.contains(row['HISTORY'].lower(), 'diabete'):
        data21.at[index, 'diabetes'] = 1

    if operator.contains(row['HISTORY'].lower(), 'diabete') or operator.contains(row['HISTORY'].lower(), 'high blood'):
        data21.at[index, 'hypertension'] = 1

    if operator.contains(row['HISTORY'].lower(), 'arthritis'):
        data21.at[index, 'arthritis'] = 1

    if operator.contains(row['HISTORY'].lower(), 'asthma'):
        data21.at[index, 'Asthma'] = 1

    if operator.contains(row['HISTORY'].lower(), 'migraine'):
        data21.at[index, 'Migraine'] = 1

    if operator.contains(row['HISTORY'].lower(), 'copd'):
        data21.at[index, 'copd'] = 1

    if operator.contains(row['HISTORY'].lower(), 'anxiety'):
        data21.at[index, 'anxiety'] = 1

    if operator.contains(row['HISTORY'].lower(), 'obesity'):
        data21.at[index, 'obesity'] = 1

    if operator.contains(row['HISTORY'].lower(), 'depression'):
        data21.at[index, 'depression'] = 1

    if operator.contains(row['HISTORY'].lower(), 'thyroid'):
        data21.at[index, 'Thyroid'] = 1

    if operator.contains(row['HISTORY'].lower(), 'anemia'):
        data21.at[index, 'Anemia'] = 1

    if operator.contains(row['HISTORY'].lower(), 'dementia'):
        data21.at[index, 'Dementia'] = 1

    if operator.contains(row['HISTORY'].lower(), 'cancer'):
        data21.at[index, 'Cancer'] = 1

    if operator.contains(row['HISTORY'].lower(), 'kidney') or operator.contains(row['HISTORY'].lower(), 'ckd'):
        data21.at[index, 'Kidney'] = 1

    if operator.contains(row['HISTORY'].lower(), 'hyperlipidemia'):
        data21.at[index, 'Hyperlipidemia'] = 1

    if operator.contains(row['HISTORY'].lower(), 'heart') or operator.contains(row['HISTORY'].lower(), 'cvd') or \
            operator.contains(row['HISTORY'].lower(), 'stroke') or operator.contains(row['HISTORY'].lower(), 'hf'):
        data21.at[index, 'CVD'] = 1

    if operator.contains(row['HISTORY'].lower(), 'af') or operator.contains(row['HISTORY'].lower(), 'atrial') or operator.contains(row['HISTORY'].lower(), 'fibrillation'):
        data21.at[index, 'AF'] = 1

data21 = data21.drop(data21[data21['NUMDAYS'] > 50].index)
# clean = data21[['NOC', 'region', 'notes', 'Avg_age', 'Medal', 'Gold', 'Athletes']]
data21.to_csv('./data21.csv', index=False)
# fds = fds.loc[fds['Age'].notna()]
#
# # select female or male athletes
# fds = fds.loc[fds['Sex'] == 'F']
# # fds = fds.loc[fds['Sex'] == 'M']
#
# medals = fds.loc[fds['Medal'].notna()]
# medals = medals.NOC.value_counts().reset_index(name='Medal')
# medals.rename(columns={'index': 'NOC'}, inplace=True)
#
# golds = fds.loc[fds['Medal'] == 'Gold']
# golds = golds.NOC.value_counts().reset_index(name='Gold')
# golds.rename(columns={'index': 'NOC'}, inplace=True)
#
# age = fds.loc[fds['Age'].notna()]
# avg_age = age.groupby('NOC').mean()['Age'].reset_index(name='Avg_age')
#
# Athletes = fds.NOC.value_counts().reset_index(name='Athletes')
# Athletes.rename(columns={'index': 'NOC'}, inplace=True)
#
# clean = pd.merge(avg_age, medals, on='NOC', how='left')
# clean = pd.merge(clean, golds, on='NOC', how='left')
#
# clean = pd.merge(clean, Athletes, on='NOC', how='left')
#
# clean = pd.merge(full_noc, clean, on='NOC', how='left')
# clean.fillna(0, inplace=True)
#
# clean = clean[['NOC', 'region', 'notes', 'Avg_age', 'Medal', 'Gold', 'Athletes']]
#
# clean.to_csv('./data_male.csv', index=False)


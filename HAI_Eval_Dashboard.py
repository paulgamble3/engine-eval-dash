import streamlit as st
import json
import pandas as pd

# wide
st.set_page_config(layout="wide")

st.title("HAI Eval Dashboard")

# for each engine
# in a folder
# load the various subsections

# the results shown in each table
# will come from a single file
# the order in the file will determine the order in the table
# the columns of the table will be the keys into the objects

# write a loader+displayer that generalizes across all engine results

def load_display(results_fn, results_dict):
    with open(results_fn) as f:
        results = json.load(f)

    df_rows = []

    for result in results:
        row = [result["date"], result["run_name"], result["benchmark_version"]]
        for key in results_dict:
            row.append(result["results"][key])
        df_rows.append(row)

    df = pd.DataFrame(df_rows, columns=["Date", "Run Name", "Benchmark"] + list(results_dict.values()))

    st.write(df)



drug_detector_results = './results/drug_detector/drug_detector_results.json'
drug_detector_results_dict = {
    "med_discussed_accuracy": "Med Detection Accuracy",
    "med_identified_accuracy": "Med Identification Accuracy",
    "FPR": "FPR",
    "FNR": "FNR",
}
st.subheader("Drug Detector")
st.write("n = 300")
load_display(drug_detector_results, drug_detector_results_dict)

st.divider()

drug_asr_results = './results/drug_asr/drug_asr_results.json'
drug_asr_results_dict = {
    "accuracy": "Overall Accuracy",
    "FPR": "FPR",
    "FNR": "FNR",
    "TPR": "TPR",
    "TNR": "TNR"
}
st.subheader("Drug ASR")
st.write("n = 202")
load_display(drug_asr_results, drug_asr_results_dict)

st.divider()


retrieval_detector_results = './results/retrieval_detector/retrieval_detector_results.json'
retrieval_detector_results_dict = {
    "accuracy": "Overall Accuracy",
    "FPR": "FPR",
    "FNR": "FNR",
    "TPR": "TPR",
    "TNR": "TNR"
}
st.subheader("Policy Retrieval Detector")
st.write("n = 211")
load_display(retrieval_detector_results, retrieval_detector_results_dict)



st.divider()
## Kickout Detector 
kickout_detector_results = './results/kickout_detector/ko_detector_results.json'
kickout_detector_results_dict = {
    "accuracy": "Overall Accuracy",
    "FPR": "FPR",
    "FNR": "FNR",
    "TPR": "TPR",
    "TNR": "TNR",     
}    
st.subheader("Kickout Detector")
st.write("n = 1250")
load_display(kickout_detector_results, kickout_detector_results_dict)

## Kickout Evaluator
kickout_evaluator_results = './results/kickout_evaluator/kickout_evaluator_results.json'
kickout_evaluator_results_dict = {
    "accuracy": "Overall Accuracy",
    "false_positive_rate": "FPR", 
    "false_negative_rate": "FNR",
    "true_positive_rate": "TPR",
    "true_negative_rate": "TNR", 
}    
st.subheader("Kickout Evaluator")
st.write("n = 565")
load_display(kickout_evaluator_results, kickout_evaluator_results_dict)



# ## Kickout Detector - end to end
# kod_ete_results = './results/ko_detector_end_to_end/KOD_ete.json'
# kod_ete_results_dict = {
#     "Accuracy - 1 KO": "Accuracy - 1 KO",
#     "Accuracy - 2 KO": "Accuracy - 2 KO",
#     "Accuracy - 3 KO": "Accuracy - 3 KO"  
# }    
# st.subheader("Kickout Detector - End to End")
# load_display(kod_ete_results, kod_ete_results_dict)

# ## Kickout Evaluator - end to end 
# koe_ete_results = './results/ko_evaluator_end_to_end/KOE_ete.json'
# koe_ete_results_dict = {
#     "Accuracy - 1 KO": "Accuracy - 1 KO",
#     "Accuracy - 2 KO": "Accuracy - 2 KO",
#     "Accuracy - 3 KO": "Accuracy - 3 KO"     
# }    
# st.subheader("Kickout Evaluator - End to End")
# load_display(koe_ete_results, koe_ete_results_dict)

st.divider()
## Lab Engine
lab_engine_results = './results/lab_engine/lab_results.json'
lab_engine_results_dict = {
    "overall_acc": "Overall Accuracy",
    "FPR": "FPR",
    "FNR": "FNR",
    "bp_accuracy": "BP Accuracy",
    "label_acc": "Label Accuracy",
    "value_acc": "Value Accuracy",     
}    
st.subheader("Lab Engine")
st.write("n = 359")
load_display(lab_engine_results, lab_engine_results_dict)
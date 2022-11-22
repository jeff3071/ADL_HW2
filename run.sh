# "${1}": path to the context file.
# "${2}": path to the testing file.
# "${3}": path to the output predictions.

python preprocess_CS.py "${2}" ./CS_data/test.json "${1}"
bash test_CS.sh
python preprocess_QA.py ./CS_result.json ./QA_data/test.json "${1}"
bash test_QA.sh
python convert_ans.py ./model/QA/predict_predictions.json "${3}"

rm ./CS_result.json
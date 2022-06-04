# Dacon 2022 코드 유사성 판단 NLP

- model: klue/roberta-base
  1. epoch_num=5, label_num=2, learning_rate=2e-5,train_test_split=0.2 ➡️ accuracy:0.97, private score:0.79
  2. epoch_num=10, label_num=2, learning_rate=2e-5,train_test_split=0.2 ➡️ accuracy:0.97, private score:0.79
  3. epoch_num-10, label_num=2, learning_rate=1e-5,train_test_split=0.1, seed=100 ➡️ accuracy:0.97, private score:0.80   
  
  📌 label_num=1로 할 경우 RuntimeError: Found dtype Long but expected Float 발생 (참고: https://stackoverflow.com/questions/70490710/runtimeerror-found-dtype-long-but-expected-float-when-fine-tuning-using-trainer)   
  📌 klue/roberta-large도 해보면 좋을듯   
  📌 학습이 진행됨에 따라 갑자기 accuracy 확 낮아지는 경우가 꽤 있는데 이럴 때마다 학습률 줄이는 방식 도입?!
***
- model: graph codebert
***
- model: DOBF

***
- model: CodeBERT

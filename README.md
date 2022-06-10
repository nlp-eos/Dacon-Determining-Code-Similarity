# Dacon 2022 코드 유사성 판단 NLP
### hyperparameter

- model: klue/roberta-base
  1. epoch_num=5, label_num=2, learning_rate=2e-5,train_test_split=0.2 ➡️ accuracy:0.97, public score:0.7924689297
  2. epoch_num=10, label_num=2, learning_rate=2e-5,train_test_split=0.2 ➡️ accuracy:0.97, public score:0.7943424226
  3. epoch_num=10, label_num=2, learning_rate=1e-5,train_test_split=0.1, seed=100 ➡️ accuracy:0.97, public score:0.8014654053  
  
  📌 label_num=1로 할 경우 RuntimeError: Found dtype Long but expected Float 발생 (참고: https://stackoverflow.com/questions/70490710/runtimeerror-found-dtype-long-but-expected-float-when-fine-tuning-using-trainer)   
  📌 klue/roberta-large도 해보면 좋을듯   
  📌 학습이 진행됨에 따라 갑자기 accuracy 확 낮아지는 경우가 꽤 있는데 이럴 때마다 학습률 줄이는 방식 도입?!   
  -> klue 경우 한국어에 대한 pretrained model 이기 때문에 code와는 맞지 않는다고 판단
***
- model: GraphCodeBERT  
  📌 default : label_num=2, learning_rate=2e-5,train_test_split=0.1, MAX_LEN = 256, batch_size = 16
  1. epoch_num=8, train_dataset = 46000?(sample_train.csv+custom 27000) ➡️ accuracy:0.975129, public score:
  2. epoch_num=7, train_dataset = 45088(custom) ➡️ accuracy:0., public score:  

  📌 MAX_LEN = 512 / batch_size = 32일 경우 RuntimeError: CUDA out of memory

***
- model: CodeBERT     
 -> codeBERT 경우 ml-pl pair에 대한 모델, pl에 대해서만 embedding -> cosineSimilarity를 통한 sequenceClassfication -> loss -> 학습??
  1. 기존 klue/roberta-base fine-tuning 시키는 모델에서 모델만 바꿈   
   model: microsoft/codeBERT-base, learning_rate = 1e-5, MAX_LEN = 512, epoch_num = 10, batch_size = 16 ➡️ accuracy: 0.97, public score:0.8968280467
  2. 6/8 model: microsoft/codeBERT-base, learning_rate = 1e-5, MAX_LEN = 512, epoch_num = 10, batch_size = 16, optimizer=AdamW(weight_decay=0.0), scheduler = transformers.get_cosine_schedule_with_warmup(optimizer, num_warmup_steps=5, num_training_steps=5), metric=accuarcy ➡️ accuracy: 0.97, public score:0.8627898349
  3. 6/9 model: microsoft/codeBERT-base, learning_rate = 1e-5, MAX_LEN = 512, epoch_num = 10, batch_size = 16, optimizer=AdamW(weight_decay=0.1), scheduler = transformers.get_cosine_schedule_with_warmup(optimizer, num_warmup_steps=5, num_training_steps=5), trainset=new_trainset  ➡️ accuracy: 0.96, public score: 0.9345019477
  4. 6/10 model: microsoft/codeBERT-base, learning_rate = 1e-5, MAX_LEN = 512, epoch_num = 10, batch_size = 16, optimizer=AdamW(weight_decay=0.1), scheduler = transformers.get_cosine_schedule_with_warmup(optimizer,num_warmup_steps=5, num_training_steps=5), trainset=new_trainset(40000), +preprocess(train_set) ➡️ accuracy: 0.96, pulbic score: 0.9528287887⭐️

***
### 개선 방안
- sentence BERT 사용
- MLM: DOBF 방식 사용
- 좀 더 많은 시도로 적절한 hyperparameter 찾기
- B25 등의 알고리즘으로 모델에 최적화된 큰 사이즈의 데이터셋 구축

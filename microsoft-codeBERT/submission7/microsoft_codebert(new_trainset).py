# -*- coding: utf-8 -*-
"""microsoft-CodeBERT(new_trainset).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tKRqcqrM0LXRjeKKfxy8IsjZX1lvgu67
"""

from google.colab import drive
drive.mount('/content/drive')

#optimization: AdamW
#model: microsoft/CodeBERT
#learning rate: 1e-5
#train_test_split=0.1, seed = 100
#batch_size = 16

!pip install torch
!pip install transformers
!pip install transformers datasets

import pandas as pd
import re
from transformers import AutoModel, AutoTokenizer, AutoModelForSequenceClassification, RobertaTokenizer, RobertaConfig, RobertaModel
from datasets import load_dataset
from pandas.core.common import random_state
import numpy as np
from datasets import load_metric
from transformers import TrainingArguments, Trainer
import logging
import sklearn.metrics as metric
from transformers import DataCollatorWithPadding
import torch,gc
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from torch.nn import CrossEntropyLoss

#Load Train dataset
train = pd.read_csv('new_train_sample.csv', encoding = 'utf-8')
df = pd.DataFrame(train)

#Define Model
model = AutoModelForSequenceClassification.from_pretrained("microsoft/codebert-base")
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
#tokenizer.truncation_side = 'left'

batch_size = 16
epoch_num = 10
MAX_LEN = 512
learning_rate = 1e-5

def preprocess(df,file_name):
  #preprocess_df = df.replace(re.compile('(^import.*|^from.*)',re.MULTILINE),"",regex=True) #import,from 없애기
  preprocess_df = df.replace(re.compile('(#.*)', re.MULTILINE),"",regex=True) #주석 한 줄
  preprocess_df = preprocess_df.replace(re.compile('[\'\"]{3}.*?[\'\"]{3}', re.DOTALL),"",regex=True) #주석 여러줄
  preprocess_df = preprocess_df.replace(re.compile('[\n]{2,}', re.MULTILINE),"\n",regex=True) #다중개행 한번으로
  preprocess_df = preprocess_df.replace(re.compile('[ ]{4}', re.MULTILINE),"\t",regex=True) #tab 변환
  preprocess_df = preprocess_df.replace(re.compile('[ ]{1,3}', re.MULTILINE)," ",regex=True) #공백 여러개 변환
  preprocess_df.to_csv(file_name)
  
def tokenized(examples):
  return tokenizer(examples['code1'],examples['code2'], padding=True, max_length=MAX_LEN,truncation=True, return_token_type_ids=True)

preprocess(df,"preprocess.csv")
dataset = load_dataset("csv",data_files="preprocess.csv")['train']
encoded_dataset = dataset.map(tokenized,remove_columns=['Unnamed: 0','code1','code2'],batched=True)
encoded_dataset=encoded_dataset.rename_column(original_column_name='similar',new_column_name='labels')
encoded_dataset
print(encoded_dataset[1])
print(len(encoded_dataset))
print(tokenizer.tokenize(dataset['code2'][1]))

encoded_dataset = encoded_dataset.train_test_split(0.1,seed=100)

from transformers import AdamW
import transformers
optimizer = torch.optim.AdamW(model.parameters(),
            lr = learning_rate, betas=(0.9,0.99), eps=1e-8, 
            weight_decay=0.1)
scheduler = transformers.get_cosine_schedule_with_warmup(optimizer,
                                        num_warmup_steps=5, num_training_steps=5)
optimizers = optimizer, scheduler

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

metric = load_metric("accuracy")

def compute_metrics(eval_pred): #이게 필요한가?
  predictions, labels = eval_pred
  predictions = np.argmax(predictions, axis=1)
  return metric.compute(predictions=predictions, references=labels)

'''
class TrainerModified(Trainer):
  def compute_loss(self,model,inputs,return_outputs=False):
    labels = inputs.get("labels")
    outputs = model()
'''

args = TrainingArguments("test", save_strategy="epoch",evaluation_strategy="epoch",logging_strategy="epoch", 
                         learning_rate=learning_rate,per_device_train_batch_size=batch_size,
                        per_device_eval_batch_size=batch_size,num_train_epochs=epoch_num,weight_decay=0.01,
                         do_train=True,do_eval=True,metric_for_best_model="accuracy",load_best_model_at_end=True)

trainer = Trainer(model,args,train_dataset=encoded_dataset['train'],eval_dataset=encoded_dataset['test'],
                  tokenizer=tokenizer, compute_metrics=compute_metrics, data_collator=data_collator,
                  optimizers=optimizers)

gc.collect()
torch.cuda.empty_cache()

trainer.train()

trainer.evaluate()

#test data preprocess 추가
TEST = "test.csv"
SAMPLE = "sample_submission.csv"

test = pd.read_csv('test.csv', encoding = 'utf-8')
df_test = pd.DataFrame(test)

preprocess(df_test,"preprocess_test.csv")

test_dataset = load_dataset("csv",data_files = "preprocess_test.csv")['train']
test_dataset = test_dataset.map(tokenized,remove_columns=['code1','code2'])

predictions = trainer.predict(test_dataset)

df = pd.read_csv(SAMPLE)
df['similar'] = np.argmax(predictions.predictions,axis=-1)
df.to_csv('/content/drive/MyDrive/submission.csv',index=False)
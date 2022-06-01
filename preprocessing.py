# -*- coding: utf-8 -*-
"""preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rUPWN82w4Ba_599N_C3uqhggPBNTT1NS
"""

!pip install -U pandas-Profiling

!pip install MarkupSafe==2.0.1

#Pandas-Profiling
import pandas as pd
import pandas_profiling

data = pd.read_csv('sample_train.csv', encoding = 'utf-8')
print(data[:5])

pr = data.profile_report()
pr.to_file('./pr_report.html')
print(pr)

import pandas as pd
import re

data = pd.read_csv('sample_train.csv', encoding = 'utf-8')
df = pd.DataFrame(data)
print(df)

preprocess_df = df.replace(re.compile('(^import.*|^from.*)',re.MULTILINE),"",regex=True) #import,from 없애기
preprocess_df = preprocess_df.replace(re.compile('(#.*)', re.MULTILINE),"",regex=True) #주석 한 줄
preprocess_df = preprocess_df.replace(re.compile('[\'\"]{3}.*?[\'\"]{3}', re.DOTALL),"",regex=True) #주석 여러줄
preprocess_df = preprocess_df.replace(re.compile('[\n]{2,}', re.MULTILINE),"\n",regex=True) #다중개행 한번으로
preprocess_df = preprocess_df.replace(re.compile('[ ]{4}', re.MULTILINE),"\t",regex=True) #tab 변환
preprocess_df = preprocess_df.replace(re.compile('[ ]{1,3}', re.MULTILINE)," ",regex=True) #공백 여러개 변환

print(preprocess_df)

preprocess_df.to_csv('preprocess2.csv')
import pandas as pd
import pickle
df = pd.DataFrame([['swiss','fist',0],['song','fist',0],['ohm','fist',0],['best','fist',0]], columns=['name', 'gesture','repetition'])
pickle.dump(df, open('database.p', "wb" ))
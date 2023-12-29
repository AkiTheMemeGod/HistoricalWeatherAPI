import pandas as pd
import matplotlib
df = pd.read_csv("data_small/TG_STAID000001.txt", skiprows=20)
print(df["18600102"])
df = df.loc[df['   TG'] != -9999]['    DATE']
print(df[1])

print("this is printing from hello-with-pandas from git!!!.py")

import pandas as pd

df = pd.DataFrame({"col1": ["a", "b"],
              "col2": ["c", "d"]}, index=[0,1]).to_csv("csvfrompandas_fromgit.csv")

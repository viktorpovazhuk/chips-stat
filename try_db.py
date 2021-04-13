from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://postgres@localhost:5432/linuxhint", echo=False)
df = pd.DataFrame({'id': [1, 2], 'text': ["abc", "bcd"]})
df.to_sql('phil_nlp', con=engine, if_exists="append")
print(engine.execute("SELECT * FROM phil_nlp").fetchone())
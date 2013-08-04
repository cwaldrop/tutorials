# Cabe Waldrop 8/3/13
# Python script from Chapter 2 of Python for Data Analysis by Wes McKinney

import pandas
import matplotlib
import json
import pylab
from pandas import DataFrame, Series

path = 'bitly.txt'

records = [json.loads(line) for line in open(path)]

frame = DataFrame(records)

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
counts = clean_tz.value_counts()

counts[:10].plot(kind='barh', rot=0)

pylab.show()
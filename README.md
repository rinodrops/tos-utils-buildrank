# Tree of Savior Utility Package
## Build Ranking: Obtain iToS Class Build Ranking

### Environment

~~~sh
$ python -V
Python 3.7.0

$ pip freeze
beautifulsoup4==4.6.3
python-dateutil==2.7.3
selenium==3.14.0
six==1.11.0
urllib3==1.23
~~~

### Functions

#### *buildrank.*get()
**Argument**: None  
**Return**: ```classbuild_date``` date string, ```title``` page title, ```ranking``` list of builds

~~~py
import buildrank
(classbuild_date, title, ranking) = buildrank.get()
print(title)
print('Last modified: ' + classbuild_date)
print(ranking)
~~~

Refer to an example implementation ```save_ranking.py```. It saves the ranking as a json file.

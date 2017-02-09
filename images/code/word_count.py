#!/usr/bin/env python
# encoding: utf-8

import re
from operator import add
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf().setAppName("building a warehouse")
sc = SparkContext(conf=conf)
sqlCtx = SQLContext(sc)

file_in = sc.textFile('/home/zhoubo/k-vim/vimrc')
# count lines
print('######number of lines in file: %s' % file_in.count())
# add up lengths of each line
chars = file_in.map(lambda s: len(s)).reduce(add)
print('#####number of characters in file: %s' % chars)
# words from the impofile
words = file_in.flatMap(lambda line:re.split('\W+', line.lower().strip()))
# get words from the input file
words = words.filter(lambda x: len(x) >3)
# set count 1 per word
words = words.map(lambda w: (w, 1))
# reduce phase - sum count all the words
words = words.reduceByKey(add)
print(words)
#	create	function	for	histogram	of	most	frequent	words
%	matplotlib	inline
import	matplotlib.pyplot	as	plt
#
def histogram(words):
	count = map(lambda x: x[1],	words)
	word = map(lambda x: x[0], words)
	plt.barh(range(len(count)),	count,color	= 'grey')
	plt.yticks(range(len(count)), word)
#	Change	order	of	tuple	(word,	count)	from	(count,	word)
words =	words.map(lambda x:(x[1], x[0]))
words.take(25)
#	display	histogram
histogram(words.take(25))

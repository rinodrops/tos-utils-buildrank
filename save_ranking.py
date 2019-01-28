#!/usr/bin/env python
# coding: UTF-8

# save iToS Class Build Ranking

import dateutil.parser
import json
import buildrank

if __name__ == '__main__':
    # obtain ranking
    (classbuild_date, _, ranking) = buildrank.get()

    # format date as YYYY-MM-DD to be used for filename
    date = dateutil.parser.parse(classbuild_date).strftime('%Y-%m-%d')

    # dump to the file
    with open('build-ranking_' + date + '.json', 'w') as f:
        json.dump(ranking, f, indent=4, separators=(',', ': '))

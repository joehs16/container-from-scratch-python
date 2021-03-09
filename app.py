#!/usr/bin/env python
import click

# @click.command()
# @click.option("--name")
# def hello(name):
#     click.echo(f'Hello {name}!')
# @click.pageview(name, granularity, start, end)
# def getNBAWikiPageViews()

from mwviews.api import PageviewsClient
import pandas as pd
import numpy as np
import os

import click

@click.command()
@click.option('--userinfo', type = str)
@click.option('--names', type = str)
@click.option('--granularity', type = str)
@click.option('--start', type = str)
@click.option('--end', type = str)
def nbaWikiPageViews(userinfo, names, granularity, start, end):
    '''
    Show wiki pageviews
    Inputs: userinfo - email address and usage for API logs. (example input: "<joseph.hsieh@duke.edu> NBA Popularity Analysis")
            names - list of NBA player names
            granularity - granularity of pageviews (e.g. 'yearly','monthly','daily')
            start - start of observation period. input is YYYYMMDD. Earliest date is July 01, 2015; the earliest data available in this API
            end - end of observation period output is YYYYMMDD.
    Output: cash on cash in percent
    '''
    
    name = list(names.split(","))
    
    p = PageviewsClient(user_agent= userinfo)
    dict_NBA_pageviews = p.article_views('en.wikipedia', name, granularity=granularity, start=start, end=end)
    df_NBA_pageviews = pd.DataFrame.from_dict(dict_NBA_pageviews).copy()
    #click.echo(df_NBA_pageviews)
    print("-*"*30,"Wikipedia Pageviews by month","-*"*30)
    print(df_NBA_pageviews)
if __name__ == '__main__':
    nbaWikiPageViews()

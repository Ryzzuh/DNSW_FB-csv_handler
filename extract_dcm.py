#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', 1000)

pd.options.display.max_rows = 500
import datetime
import os

cwd = os.getcwd()


def main():
  excel_files = [x for x in os.listdir() if 'csv' in x]
  print(excel_files)
  file = '{}/{}'.format(cwd, excel_files[0])
  print(file)
  df = pd.read_csv(file, header=10)
  #print(df.head)
  india = df[df['Campaign'].str.contains('Always On - International.*India.*') & \
             df['Site (DCM)'].str.contains('Facebook')]
  print('india ', india)



  print('Clicks', pd.Series(india['Clicks']).sum())
  print('Impressions', pd.Series(india['Impressions']).sum())
  removeHeaderList = ['Date', 'Campaign', 'Site (DCM)', 'Placement', 'Impressions', 'Clicks']
  leaddHeaders = list(df)
  for header in removeHeaderList:
    leaddHeaders.remove(header)
  print(leaddHeaders)
  print('Leads, ', india[leaddHeaders].values.sum())

  def get_io_in_NSW(dframe):
    new_df = df[dframe['Campaign'].str.contains('It\'s ON! in NSW')]
    return new_df

  def get_io_sports(dframe):
    new_df = df[dframe['Campaign'].str.contains('It\'s ON! Sport')]
    return new_df

  def get_io_in_sydney(dframe):
    new_df = df[dframe['Campaign'].str.contains('It\'s ON! .* Sydney.*(- Summer.*|.*Prog.*)') & \
      ~dframe['Campaign'].str.contains('.*NZ.*')]
    return new_df

  print(get_io_in_sydney(df))

  print('testy', get_io_in_sydney(df))

  def get_summer_in_sydney(dframe):
    new_df = df[dframe['Campaign'].str.contains('Sydney in Summer AU.*')]
    return new_df

  def get_summer_in_sydney_nz(dframe):
    new_df = df[dframe['Campaign'].str.contains('Sydney in Summer NZ 2017')]
    return new_df

  #for DBM Prospecting -> contains "Prospecting"
  #for DBM Retargeting -> contains "Retargeting"
  #for DBM Video -> contains "Video" - note, Leads for this is actually "Views"

  def get_dbm_prospecting(dframe):
    new_df = df[dframe['Site (DCM)'].str.contains('.*bidmanager.*') & \
                df['Placement'].str.contains('[P|p]rospecting')]
    return new_df

  def get_dbm_retargeting(dframe):
    new_df = df[dframe['Site (DCM)'].str.contains('.*bidmanager.*') & \
                df['Placement'].str.contains('[R|r]etargeting')]
    return new_df

  def get_dbm_video(dframe):
    new_df = df[dframe['Site (DCM)'].str.contains('.*bidmanager.*') & \
                df['Placement'].str.contains('[V|v]ideo')]
    return new_df

  def get_unique_campaigns(dframe):
    return dframe.Campaign.unique

  #print("test", get_dbm_video(df))
  def get_clicks_sum(dframe):
    return pd.Series(dframe['Clicks']).sum()

  def get_impressions_sum(dframe):
    return pd.Series(dframe['Impressions']).sum()

  def get_leads_sum(dframe):
    # create matrix for leads sum()
    remove_header_list = ['Date', 'Campaign', 'Site (DCM)', 'Placement', 'Impressions', 'Clicks']
    lead_headers = list(df)
    for header in remove_header_list:
      lead_headers.remove(header)
    # /create matrix
    return dframe[lead_headers].values.sum()

  def get_totals(dframe):
    unique_campaigns = get_unique_campaigns(dframe)
    clicks = get_clicks_sum(dframe)
    impressions = get_impressions_sum(dframe)
    leads = get_leads_sum(dframe)

    print('unique_campaigns', unique_campaigns)
    print('Clicks', clicks)
    print('Impressions', impressions)
    print('Leads, ', leads)

  #get_totals(get_dbm_video(df))
  test = get_io_in_NSW(df)
  get_totals(get_dbm_prospecting(get_io_in_NSW(df)))
  #print(df.Campaign.unique)


if __name__ == "__main__":
  main()
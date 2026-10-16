def read_pier_data(years, column_names):
    '''
    Load multi-year records from Scripps pier as one dataframe.
    
    To enter a range of years: use list(range(start, stop, step)) format.
    Default step = 1. Remember that the end ("stop") value is NOT inclusive! 
    
    To enter specific years: create a list such as [2005, 2010, 2015]
    
    column_names: enter list of column names as strings (case-sensitive)
    Example: ['temperature','pressure']
    '''
    
    data = []
    for year in years:
        url = f"https://thredds.sccoos.org/thredds/dodsC/autoss/scripps_pier-{year}.nc"
        df = xr.open_dataset(url).to_dataframe() # open url for each year and convert to dataframe
        df = df[column_names] # to save time, only save data from selected columns
        df.index = pd.to_datetime(df.index.astype(str)) # convert index to datetime format
        data.append(df)
    return pd.concat(data, axis=0) # add each year to the bottom of existing dataframe
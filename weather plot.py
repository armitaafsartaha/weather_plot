from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

def plot_weather_data(filepath):
    path=Path(filepath)
    try:
      lines=path.read_text().splitlines()
    except FileNotFoundError:
        print(f"file named {filepath} does not exist")
        return #exit from function
    reader=csv.reader(lines)
    header_row=next(reader)

    max_index=header_row.index('TMAX')
    min_index=header_row.index('TMIN')
    title=header_row.index('NAME')
    date_index=header_row.index('DATE')

    dates,mins,maxs=[],[],[]
    station_name=None
    for row in reader:
       if station_name is None:
          station_name=row[title]
       try:
          date=datetime.strptime(row[date_index],'%m/%d/%Y')
          tmax=int(row[max_index])
          tmin=int(row[min_index])
       except Exception:
          print(f"Missing data in row: {row} (file: {filepath})")
       else:
          dates.append(date)
          maxs.append(tmax)
          mins.append(tmin)
    
    plt.style.use('Solarize_Light2')
    fig,ax=plt.subplots()

    ax.plot(dates,maxs,color='red')
    ax.plot(dates,mins,color='blue')

    ax.set_title(station_name)
    ax.set_xlabel(header_row[date_index]+'S')
    ax.set_ylabel(f"{header_row[max_index]} - {header_row[min_index]} Temperature (F)")
    ax.fill_between(dates,maxs,mins,alpha=0.2,facecolor='purple')
    plt.show()
    
file_input=input("write path of file:")
if not file_input:
    print("No file path entered. Exiting.")
else:

    plot_weather_data(file_input)

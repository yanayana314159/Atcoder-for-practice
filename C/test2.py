import sys
from datetime import datetime
import numpy as np
import pandas as pd

def timeformat(time_str):
    if time_str.startswith('24:'):
        time_str = '00' + time_str[2:]
    time_obj = datetime.strptime(time_str, '%H:%M:%S.%f').time()
    total_milliseconds = (time_obj.hour * 60 * 60 + time_obj.minute * 60 + time_obj.second) * 1000 + time_obj.microsecond // 1000
    return total_milliseconds

def main(lines):
    try:
        data=[[timeformat(entry.split()[0]), float(entry.split()[1])] for entry in lines]
        data=np.array(data)
        # 時間の差
        diff_column = np.diff(data[:, 0], prepend=0)
        data = np.column_stack((data, diff_column))

        # 総走行距離
        sum_column = np.cumsum(data[:, 1])
        data = np.column_stack((data, sum_column))

        # 速度
        speed_column = (data[:, 1] / 1000) / (data[:, 2] / (60 * 60 * 1000))  #
        data = np.column_stack((data, speed_column))

        df=pd.DataFrame(data)
        df=df.fillna(0)
        df.columns = ['時間', '差分距離', '時間の差', '総走行距離','速度']
        
        #走り始めの時間で条件分岐
        if df['時間'].iloc[0]<=60*60*6:
            a=1.5
        elif 60*60*6<df['時間'].iloc[0]<=60*60*9.5:
            a=1.3
        elif 60*60*20<df['時間'].iloc[0]<=60*60*24:
            a=1.3
        else:
            a=1
        
        init=int(400*a)
        z=0
        if df['速度'].iloc[1]<10:
            x=df['時間の差'].iloc[-1]//(1000*45)
            if df['時間の差'].iloc[-1]%(1000*45)!=0:
                x=x+1
            
            z=x*40*a

        #走行距離で判別する
        if df['総走行距離'].iloc[-1]<1000:
            price=int(init+z)
            print(price)
        
        elif df['総走行距離'].iloc[-1]<=10200:
            x=(df['総走行距離'].iloc[-1]-1000)//400
            if (df['総走行距離'].iloc[-1]-1000)%400!=0:
                x=x+1
            m=x*40*a
            price=int(m+init)
            print(price)
        else:
            x=(df['総走行距離'].iloc[-1]-10200)//350
            if (df['総走行距離'].iloc[-1]-10200)%350!=0:
                x=x+1
            l=x*40*a
            m=(9200/400)*40*a
            price=int(init+m+l)
            print(price)
            

        #print(df)
        



        
       
    except Exception as e:
        print(e)
   

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

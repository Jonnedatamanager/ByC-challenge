
"""
Created on Wed Oct  9 15:37:55 2024

@author: Arend, Jonne, Roel, Stefan and Luka
"""
import numpy as np
def main():
    ''' Model settings '''
    dt = 0.5  # time step in minutes
    
    ''' area characteristics]'''
    ''' I=garden,II=roof,III=sidewalk,IV=road,V=berm'''
    CN = [60,100,95,98,60]  # Curve Number (assumed)
    area = [5, 8, 2, 8, 4]*5 # expressed in m2
    
    
    Q_sew = 0.2 #mm
    Q_run_out = 0 #mm, zero since assuming lowest elevation point
    Q_run_in = 1 #mm, water running from other areas to the street
    
    
    ''' Rainfall event '''
    rain_duration = 30  # total duration of the rain in minutes
    max_rain = 70  # total rainfall in mm
    P = max_rain / rain_duration  # rainfall rate (mm per minute)
    
    ''' CN Method Parameters '''
    timesteps = int(rain_duration/dt)
    excess_heights = np.zeros((len(CN), timesteps))
    excess_volumes = np.zeros((len(CN), timesteps))
    steps = int(rain_duration / dt) 
    
    excess_heights, excess_volumes = CN_METHOD_ITERATION(steps,P,CN,area,dt,excess_heights,excess_volumes)

def CN_METHOD_ITERATION(steps,P,CN,area,dt,excess_heights,excess_volumes):

    
    for t_index in range(steps):
        t = t_index * dt  # Current time in minutes
        rain = P*t
        
        for i in range(len(CN)):
            S = (25400 / CN[i]) - 254  # potential maximum retention (mm)
            I_a = 0.2 * S  # initial abstraction (mm)
            
            if rain > I_a:
                excess_height = ((rain - I_a) ** 2) / (rain - I_a + S) / 1000#m
            else:
                excess_height = 0
            
            excess_volume = excess_height * area[i] # m3
            #store for table
            excess_heights[i, t_index] = excess_height
            excess_volumes[i, t_index] = excess_volume
    
    return excess_heights, excess_volumes
        
main()
    
    
        
    
    

        
    





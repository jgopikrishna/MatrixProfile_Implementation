def stamp(Ta,Tb,m):
    na = len(Ta)
    nb = len(Tb)
    #initializing the values to a bigger numbers
    pab = 9999999999999 * np.ones((na-m)+1)
	#intializing the matrix profile index to all zeros.
    iab = np.zeros((na-m)+1)
    idx = [i for i in range(0, (na - m)+1)]
    i=0
    excZoneLen = int(np.round((m/2))+1)
    proLen = int((na-m+1))
    std_ta = Ta
    std_ta = pd.Series([(x-np.mean(Ta))/np.std(Ta) for x in Ta])
    
    for id in idx:
        D = mass_v2(std_ta.values,std_ta[id:id+m].values)
        #For any distance value calculated setting to bigger number if we have NAN or None
        D=np.array([999999999 if x is None or np.isnan(x) else x for x in D])
        
        excZoneStart = max(0, id - excZoneLen);
        excZoneEnd = min(proLen, id + excZoneLen);
        #exclusion zone to avoid the trivial match.
        D[excZoneStart:excZoneEnd] =999999999
        
		#setting up the minimum value for each run.
        pab = np.minimum(D,pab)
        
		#Updating the matrix profile index
        iab = np.where( pab == D ,id,iab)
        pab[id] = np.min(D)
        iab[id] = np.argmin(D)
        
    return pab, iab
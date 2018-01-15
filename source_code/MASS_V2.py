def mass_v2(x,y):
    m = len(y)
    n = len(x)
    
    meany = np.mean(y)
    sigmay = np.std(y,ddof=0)
	
	#this method of calculation is lot faster.
    meanx = pd.Series(x.ravel()).rolling(window=m,min_periods=0).mean().values
    sigmax = pd.Series(x.ravel()).rolling(window=m,min_periods=0).std(ddof=0).fillna(0).values
    y =  y[::-1]
    y=np.append(y,np.zeros(n-m))  #filling zeros to make same length as x
    
    X = np.fft.fft(x)
    Y = np.fft.fft(y)
    Z = X*Y
    z = np.real(np.fft.ifft(Z))
    
    dist = 2*(m-(z[m-1:n]-m*meanx[m-1:n]*meany)/(sigmax[m-1:n]*sigmay));
    
    dist = np.sqrt(np.abs(dist))
    
    
    return dist
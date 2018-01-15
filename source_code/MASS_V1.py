def mass_v1(x,y):
    n = len(x)
    y_mean = np.mean(y)
    y_std = np.std(y)
    m = len(y)
    ta = np.append(x,np.zeros(n))
    qr = y[::-1]
    qra = np.append(qr,np.zeros(2*n-m))
    qraf = np.fft.fft(qra)
    taf = np.fft.fft(ta)
    QT = np.multiply(qraf, taf)
    z = np.real(np.fft.ifft(QT))
    
    sumy = np.sum(qra)
    sumy2 = np.sum(qra**2)
    
    cum_sumx = np.cumsum(ta)
    cum_sumx2 = np.cumsum(ta**2)
    sumx2 = cum_sumx2[m:n]-cum_sumx2[0:n-m]
    sumx = cum_sumx[m:n]-cum_sumx[0:n-m]
    meanx = sumx/m
    sigmax2 = (sumx2/m)-(meanx**2)
    sigmax = np.sqrt(sigmax2)
    dist = (sumx2 - 2*sumx*meanx + m*(meanx**2))/sigmax2 - 2*(z[m:n] - sumy*meanx)/sigmax + sumy2;
    dist = np.sqrt(np.abs(dist))
    
    
    return dist
    

    
    
        

    
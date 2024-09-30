import numpy as np
import struct
import matplotlib.pyplot as plt


file_path = 'CapturedSignals/8FSK-RTL-SDR-20240701_104645-915MHz-2MSps-500KHz.complex16s'
fs = 2e6
endsample = 1500000

# Open the file

with open(file_path, 'rb') as fid:
    # Read the data from the file
    data = np.fromfile(fid, dtype=np.uint16, count=endsample)

    # Preallocate arrays for efficiency
    data_I_sgn = np.zeros(endsample, dtype=np.int8)
    data_Q_sgn = np.zeros(endsample, dtype=np.int8)

    for i in range(endsample):
        data_bin = f'{data[i]:016b}'
        data_I = np.uint8(int(data_bin[8:], 2))
        data_Q = np.uint8(int(data_bin[:8], 2))
        data_I_sgn[i] = data_I.view(np.int8)
        data_Q_sgn[i] = data_Q.view(np.int8)
        

# Combine I and Q into complex IQ data
signal = data_I_sgn + 1j * data_Q_sgn

IQ_data = np.column_stack((data_I_sgn, data_Q_sgn))
    
nbins = 64   
points = 256

start = 1
end = 1000000
cnt = 1
while cnt<2501:
    
    counts, xedges, yedges = np.histogram2d(IQ_data[start:start+(points-1),0], IQ_data[start:start+(points-1),1], bins=nbins)

    # Create a figure with a specific size and DPI
    fig = plt.figure(figsize=(2.24, 2.24), dpi=100)  # 224 pixels / 100 dpi = 2.24 inches
    ax = fig.add_subplot(111)

    # Plot the image
    ax.imshow(counts, cmap='hot')



    # Disable x-axis and y-axis
    ax.set_axis_off()

    # Adjust layout to make sure the size is accurate
    plt.tight_layout(pad=0)

    plt.savefig(f"ConstellationWithBins/64_256/newDQPSK/const_{5500+cnt}", bbox_inches='tight', pad_inches=0)


    #plt.show()
    plt.close(fig)

    
    start += points
    cnt+=1
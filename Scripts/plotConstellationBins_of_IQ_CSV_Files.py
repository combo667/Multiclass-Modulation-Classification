import numpy as np
import struct
import matplotlib.pyplot as plt
import pandas as pd


file_path = 'C:/Users/RD/Desktop/FSK_NOTFSK/rfd900_fsk_csv_files_fs_960KHz/rfd900_net133.csv'
fs = 960e3



IQ_data = pd.read_csv(file_path)
IQ_data = IQ_data.to_numpy()


nbins = 64
points = 128

start = 1
end = 480000
cnt = 1
while cnt<1500:
    
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

    plt.savefig(f"C:/Users/RD/Desktop/FSK_NOTFSK/const/rfd900_net133/xconst_{4500+cnt}", bbox_inches='tight', pad_inches=0)


    #plt.show()
    plt.close(fig)

    
    start += points
    cnt+=1
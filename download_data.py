import obspy
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
client = Client("IRIS")
t = UTCDateTime("2022-01-24 20:00:00") # UTC = +8 hrs from Tucson
[ sbef, saft ] = [ 0, 3600 ] # seconds before and after start time (t)
st = client.get_waveforms( "IU", "TUC", "00", "BH*", t - sbef, t + saft)
st.filter("bandpass", freqmin=1.0, freqmax=5.0, corners=2, zerophase=False)
st.plot( linewidth=0.75, equal_scale=False, starttime = t)

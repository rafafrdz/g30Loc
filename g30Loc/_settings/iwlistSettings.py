## Cell Field
Name_ = 'Name'
Quality_ = 'Quality'
Channel_ = 'Channel'
Frecuency_ = 'Frequency'
Encryption_ = 'Encryption'
Address_ = 'Address'
Signal_ = 'Signal'
ESSID_ = 'ESSID'

## iwList
iwListCommnd = "iwlist"
optionCmmnd = "scan"
## iwList Field
symb1 = ":"
symb2 = "="
wESSID = ESSID_+symb1
wQuality = Quality_+symb2
wFrecuency = Frecuency_+symb1
wChannel = Channel_+symb1
wSignal = "{} level{}".format(Signal_,symb2)
wEncryption = "{} key{}".format(Encryption_,symb1)
wAddress = Address_+symb1
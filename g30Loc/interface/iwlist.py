import subprocess
from g30Loc._settings.iwlistSettings import *

# You can add or change the functions to parse the properties of each AP (cell)
# below. They take one argument, the bunch of text describing one cell in iwlist
# scan and return a property of that cell.

def get_name(cell):
    return matching_line(cell, wESSID)[1:-1].strip()

def get_frecuency(cell):
    return 1/(float(matching_line(cell,wFrecuency).split()[0].strip())*(10**9))

def get_quality(cell):
    quality = matching_line(cell, wQuality).split()[0].split('/')
    return str(int(round(float(quality[0]) / float(quality[1]) * 100))).rjust(3) + " %".strip()


def get_channel(cell):
    return matching_line(cell, wChannel).strip()


def get_signal_level(cell):
    # Signal level is on same line as Quality data so a bit of ugly
    # hacking needed...
    return int(matching_line(cell, wQuality).split(wSignal)[1].split()[0].strip())


def get_encryption(cell):
    enc = ""
    if matching_line(cell, wEncryption) == "off":
        enc = "Open"
    else:
        for line in cell:
            matching = match(line, "IE:")
            if matching != None:
                wpa = match(matching, "WPA Version ")
                if wpa != None:
                    enc = "WPA v." + wpa
        if enc == "":
            enc = "WEP"
    return enc


def get_address(cell):
    return matching_line(cell, wAddress).strip()


# Here's a dictionary of rules that will be applied to the description of each
# cell. The key will be the name of the column in the table. The value is a
# function defined above.

rules = {Name_: get_name,
         Quality_: get_quality,
         Frecuency_: get_frecuency,
         Channel_: get_channel,
         Address_: get_address,
         Signal_: get_signal_level,
         Encryption_: get_encryption
         }



def matching_line(lines, keyword):
    """Returns the first matching line in a list of lines. See match()"""
    for line in lines:
        matching = match(line, keyword)
        if matching != None:
            return matching

    return None


def match(line, keyword):
    """If the first part of line (modulo blanks) matches keyword,
    returns the end of that line. Otherwise returns None"""
    line = line.lstrip()
    length = len(keyword)
    if line[:length] == keyword:
        return line[length:]
    else:
        return None


def parse_cell(cell):
    """Applies the rules to the bunch of text describing a cell and returns the
    corresponding dictionary"""
    parsed_cell = {}
    for key in rules:
        rule = rules[key]
        parsed_cell.update({key: rule(cell)})
    return parsed_cell


class Cell():
    def __init__(self, parsed):
        self.name = parsed[Name_]
        self.address = parsed[Address_]
        self.frecuency = parsed[Frecuency_]
        self.quality = parsed[Quality_]
        self.channel = parsed[Channel_]
        self.encryption = parsed[Encryption_]
        self.signal = parsed[Signal_]

class iwList():
    def __init__(self, interface):
        self.interface = interface
        self.cell = self.__parse()

    def __subprocess(self):
        return subprocess.Popen([iwListCommnd, self.interface, optionCmmnd],
                                stdout=subprocess.PIPE,
                                universal_newlines=True).communicate()
    def __parse(self):
        cells, cell = [[]], []
        out, err = self.__subprocess()
        for line in out.split("\n"):
            cell_line = match(line, "Cell ")
            if cell_line != None:
                cells.append([])
                line = cell_line[-27:]
            cells[-1].append(line.rstrip())
        cells = cells[1:]
        for c in cells:
            cell.append(Cell(parse_cell(c)))
        return cell

    def getCells(self):
        return self.cell

    def dataApi(self):
        wifiAccessPoints = [
            {"macAddress": c.address,
             "signalStrength": c.signal,
             # "age": c.frecuency, ## Revise this
             "channel": c.channel,
             "signalToNoiseRatio": 0} for c in self.cell]

        data = {
            "considerIP": "false",
            "wifiAccessPoints": wifiAccessPoints}
        return data

if __name__ == '__main__':
    print(iwList("wlp2s0").dataApi())
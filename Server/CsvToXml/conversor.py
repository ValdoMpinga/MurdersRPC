import csv

murdersFile = open('murders.csv')
csv_file = csv.reader(murdersFile)
murdersData = []

for row in csv_file:
    murdersData.append(row)
murdersFile.close()


def convert_row(row):
    return """
    <crime>
    <recordId id="%s">
        <agencyData>
            <agencyCode>%s</agencyCode>
            <agencyName>%s</agencyName>
            <agencyType>%s</agencyType>
        </agencyData>
        <crimeOccurence>
            <city>%s</city>
            <state>%s</state>
            <year>%s</year>
            <month>%s</month>
        </crimeOccurence>
        <crimeDetails>
            <incident>%s</incident>
            <crimeType>%s</crimeType>
            <crimeSolved>%s</crimeSolved>
        </crimeDetails>
        <VictimData>
            <victimSex>%s</victimSex>
            <victimAge>%s</victimAge>
            <victimRace>%s</victimRace>
            <victimEthnicity>%s</victimEthnicity>
        </VictimData>
        <perpetratorData>
            <perpetratorSex>%s</perpetratorSex>
            <perpetratorAge>%s</perpetratorAge>
            <perpetratorRace>%s</perpetratorRace>
            <perpetratorEthnicity>%s</perpetratorEthnicity>
            <relationship>%s</relationship>
            <weapon>%s</weapon>
            <victimCount>%s</victimCount>
            <perpetratorCount>%s</perpetratorCount>
        </perpetratorData>
        <recordSource>%s</recordSource>
    </recordId>
</crime>""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
               row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16],
               row[17], row[18], row[19], row[20], row[21], row[22], row[23])


with open('murders.xml', 'w') as file:
    file.write('\n'.join([convert_row(row) for row in murdersData]))

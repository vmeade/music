from mido import Message, MidiFile, MidiTrack
import csv

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
alltime=0
with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        
        mynote=round(float(row[1])*100)
        myvelo=round(float(row[2])*100)
        mytime=round(float(row[0])*100)

        alltime=mytime+alltime

        print(mynote,myvelo,mytime)
        track.append(Message('note_on', note=mynote, velocity=myvelo, time=alltime))
        track.append(Message('note_off', note=mynote, velocity=myvelo, time=alltime))
mid.save('data.mid')

import pretty_midi
from pathlib import Path

count = 0
total = 0
num_files = 0
num_files_with_drums = 0
def analyze(midi_filepath):
	LOG_PREFIX = "\t"
	global total 
	global count
	global num_files_with_drums
	total = total + 1
	# Load MIDI file into PrettyMIDI object
	try:
		midi_data = pretty_midi.PrettyMIDI(midi_filepath)
	except:
		print(LOG_PREFIX,"failed to read ",midi_filepath)
		return
	# Print an empirical estimate of its global tempo
	# print(midi_data.estimate_tempo())
	# Compute the relative amount of each semitone across the entire song, a proxy for key
	# total_velocity = sum(sum(midi_data.get_chroma()))
	# print([sum(semitone)/total_velocity for semitone in midi_data.get_chroma()])
	# Shift all notes up by 5 semitones
	# Synthesize the resulting MIDI data using sine waves
	# audio_data = midi_data.synthesize()
	total_instruments = midi_data.instruments
	drum_instruments = list(filter(lambda x: x.is_drum, total_instruments))
	if len(drum_instruments) > 0:
		num_files_with_drums = num_files_with_drums + 1
	count = count + len(drum_instruments)
	total = total + len(total_instruments)
	print(LOG_PREFIX,len(drum_instruments),"/",len(total_instruments))


# '**/*.midi'
pathlist = Path("../../poly/Drums").glob('**/*.mid')

for path in pathlist:
     # because path is object not string
     path_in_str = str(path)
     print(path_in_str)
     analyze(path_in_str)
     num_files = num_files + 1

percent = count / total
print
print("Drum Tracks: \t\t\t",count," / ",total, "\t(",round(count/total * 100),"% )")
print("Num Files with Drum Tracks: \t",num_files_with_drums,"/",num_files, "\t(",round(num_files_with_drums/num_files * 100),"% )")
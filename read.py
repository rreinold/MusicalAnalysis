import pretty_midi

def analyze(midi_filepath):
	# Load MIDI file into PrettyMIDI object
	midi_data = pretty_midi.PrettyMIDI(midi_filepath)
	# Print an empirical estimate of its global tempo
	# print(midi_data.estimate_tempo())
	# Compute the relative amount of each semitone across the entire song, a proxy for key
	# total_velocity = sum(sum(midi_data.get_chroma()))
	# print([sum(semitone)/total_velocity for semitone in midi_data.get_chroma()])
	# Shift all notes up by 5 semitones
	for instrument in midi_data.instruments:
	    # Don't want to shift drum notes
	    if not instrument.is_drum:
	        for note in instrument.notes:
	            note.pitch += 5
	# Synthesize the resulting MIDI data using sine waves
	# audio_data = midi_data.synthesize()
	print(len(list(filter(lambda x: x.is_drum, midi_data.instruments))),"/",len(midi_data.instruments))

from pathlib import Path

# '**/*.midi'
pathlist = Path("/Users/RobReinold/Documents/Projects/midi/poly/Drums").glob('**/*.mid')
for path in pathlist:
     # because path is object not string
     path_in_str = str(path)
     print(path_in_str)
     analyze(path_in_str)
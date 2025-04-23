# soundSynthesis

This experimental project dives into sound (audio) syntesis of waveforms

## Requirements

### For Ubuntu Linux:  
Unfortunatly, the required module `python3-sounddevice` does not exist and is not installable.  
Hence, the only way to use this module is to work with python "virtual environments" (venv).  
The following commands may be run from the directory path of this project.  
```bash
sudo apt install python3 python3-venv python3-pip
python3 -m venv synth-env
source synth-env/bin/activate
pip install -r requirements.txt
```

## Configuration
Edit the `audio_config.toml` to reflect your audio config.  
This script does not automatically "just play" on the default device.  

## How to run the script
Change directory to this project.  
Make sure there is a python venv installed in this directory.  
```bash
source synth-env/bin/activate
python soundSynthesis.py
```
You should hear a sound now.

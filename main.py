#!/usr/bin/env python
from main.alignment_by_row_channels import align

def main():
    osmosis1 = '/media/asigan/1AD0F286D0F26801/osmosis_audio_test_eng.wav'
    osmosis2 = '/media/asigan/1AD0F286D0F26801/osmosis_audio_test_esp.wav'
    wav1 = '/media/asigan/1AD0F286D0F26801/wasabi_audio_test_eng.wav'
    wav2 = '/media/asigan/1AD0F286D0F26801/wasabi_audio_test_esp.wav'
    #print align(wav1=wav1, wav2=wav1, dir='')
    result = align(wav1=osmosis1, wav2=osmosis2, dir='')
    print
    print result
    return




if __name__ == '__main__':
    main()
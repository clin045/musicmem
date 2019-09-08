import pydub
import os


if __name__ == '__main__':
    music_file = './test_data/in_heaven.mp3'
    music = pydub.AudioSegment.from_mp3(music_file)
    os.mkdir('./audio_data')
    start_point = 0
    end_point = 30 * 1000
    prompt_len = 5 * 1000
    ans_len = 5 * 1000
    end_len = 5 * 1000
    for i in range(start_point, end_point, prompt_len):
        prompt_clip = music[i:i+prompt_len]
        ans_clip = music[i:i+prompt_len+ans_len

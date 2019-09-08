import pydub
import os


if __name__ == '__main__':
    music_file = './test_data/in_heaven.mp3'
    music = pydub.AudioSegment.from_mp3(music_file)
    music_name = music_file.split('/')[-1].split('.')[0]
    os.makedirs('./audio_data', exist_ok=True)
    start_point = 0
    end_point = 30 * 1000
    prompt_len = 5 * 1000
    ans_len = 5 * 1000
    end_len = 5 * 1000
    for i in range(start_point, end_point, prompt_len):
        prompt_clip = music[i:i+prompt_len]
        prompt_clip.fade_in(20).fade_out(20)
        prompt_clip.export('./audio_data/' + music_name+'_' + str(i)+'_prompt.mp3',format='mp3')
        ans_clip = music[i:i+prompt_len+ans_len]
        prompt_clip.fade_in(20).fade_out(20)
        ans_clip.export('./audio_data/'+music_name+'_' + str(i) +'_ans.mp3', format='mp3')




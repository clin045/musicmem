import pydub
import genanki as ga
import os
import argparse
import random

def make_cloze(start_point, end_point, prompt_len, ans_len, music_name, out_path):
    clips = []
    for i in range(start_point, end_point, prompt_len):
            prompt_clip = music[i:i+prompt_len]
            prompt_clip.fade_in(20).fade_out(20)
            prompt_clip_path = (out_path+"/"+music_name+"_"+str(i)+"_prompt.mp3")
            prompt_clip.export(prompt_clip_path,format='mp3')
            ans_clip = music[i:i+prompt_len+ans_len]
            ans_clip.fade_in(20).fade_out(20)
            ans_clip_path = (out_path+"/"+music_name+"_"+str(i)+"_ans.mp3")
            ans_clip.export(ans_clip_path, format='mp3')

            clips.append((prompt_clip_path, ans_clip_path))
    return(clips)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('music_file')
    parser.add_argument('start_point', type=int)
    parser.add_argument('end_point', type=int)
    parser.add_argument('prompt_len', type=int)
    parser.add_argument('ans_len', type=int)
    parser.add_argument('music_name')
    args = parser.parse_args()



    music_file = args.music_file
    music = pydub.AudioSegment.from_mp3(music_file)
    music_name = music_file.split('/')[-1].split('.')[0]
    os.makedirs('./audio_data', exist_ok=True)
    start_point = args.start_point * 1000
    end_point = args.end_point * 1000
    prompt_len = args.prompt_len * 1000
    ans_len = args.ans_len * 1000
    clip_list = make_cloze(start_point, end_point, prompt_len, ans_len, music_name, './audio_data')
    song_name = args.music_name
    # define anki deck params
    my_model = ga.Model(
        1607392319,
        'Simple Model',
        fields=[
        {'name': 'SongName'},
        {'name': 'Prompt'},
        {'name': 'Answer'},
        ],
        templates=[
        {
          'name': 'Card 1',
          'qfmt': '{{SongName}}{{Prompt}}',
          'afmt': '{{Answer}}',
        },
        ])
    my_deck = ga.Deck(
        random.randrange(1 << 30, 1 << 31),
        music_name)
    my_package = ga.Package(my_deck)
    clip_list_flat = []
    for tup in clip_list:
        clip_list_flat.append(tup[0])
        clip_list_flat.append(tup[1])
    my_package.media_files = clip_list_flat
    for tup in clip_list:
        my_note = ga.Note(
            model = my_model,
            fields = [ song_name,
                '[sound:' + tup[0].split('/')[-1]+ ']'
                ,'[sound:' + tup[1].split('/')[-1]+ ']'
                ])
        my_deck.add_note(my_note)
    my_package.write_to_file(music_name+'.apkg')


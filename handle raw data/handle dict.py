import pandas as pd
import pickle

dir = 'D:/lab_data/kkbox-music-recommendation-challenge/'
output_data = './data/'

member_df = pd.read_csv(dir + 'members.csv')
song_df = pd.read_csv(dir + 'songs.csv')
train_df = pd.read_csv(dir + 'train.csv')

handle_names = ['song_person', 'person_song', 'song_type', 'type_song']

# Todo: 轉成 dictionary
song_person = train_df.groupby('song_id')['msno'].apply(list).to_dict()
person_song = train_df.groupby('msno')['song_id'].apply(list).to_dict()

# 切割開 |
new_df = pd.DataFrame(song_df.genre_ids.str.split('|').fillna('').tolist(), index=song_df.song_id).stack()
# Split column into multiple rows
new_df.index.name = 'song_id'
new_df = new_df.reset_index().drop('level_1', axis=1)
new_df.rename(columns={0: 'genre_ids'}, inplace=True)
song_type = new_df.groupby('song_id')['genre_ids'].apply(list).to_dict()
type_song = new_df.groupby('genre_ids')['song_id'].apply(list).to_dict()

# 從train取出msno, song_id
# save song_person.dict
file = open(output_data + handle_names[0] + '.dict', 'wb')
pickle.dump(song_person, file)
file.close()
# save person_song.dict
file = open(output_data + handle_names[1] + '.dict', 'wb')
pickle.dump(person_song, file)
file.close()
# save song_type.dict
file = open(output_data + handle_names[2] + '.dict', 'wb')
pickle.dump(song_type, file)
file.close()
# save type_song.dict
file = open(output_data + handle_names[3] + '.dict', 'wb')
pickle.dump(type_song, file)
file.close()

# load dict
# with open(output_data + handle_names[0] + '.dict', 'rb') as file:
#     a_dict1 = pickle.load(file)

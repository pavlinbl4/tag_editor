# pip install music-tag

import music_tag

mp3_file = '/Volumes/big4photo/Music/Audiobooks/Сомерсет Моэм - Санаторий.mp3'
m4a_file = '/Volumes/big4photo/Music/Audiobooks/Привидение в доходном доме_Брама Эрнест.m4a'
m4b_file = '/Volumes/big4photo/Music/Audiobooks/Бабель Исаак/01 Как это делалось в Одессе.m4b'


f = music_tag.load_file(mp3_file)

# dict access returns a MetadataItem
title_item = f['title']
# print(title_item)

# MetadataItems keep track of multi-valued keys
title_item.values  # -> ['440Hz']

# A single value can be extracted
title_item.first  # -> '440Hz'
title_item.value  # -> '440Hz'

# MetadataItems can also be cast to a string
str(title_item)  # -> '440Hz'

# tags can be set as if the file were a dictionary
f['title'] = 'Санаторий'

# additional values can be appended to the tags
f.append_tag('title', 'subtitle')
f.save()
# title_item.values  # -> ['440Hz', 'subtitle']
# title_item.first  # -> '440Hz'
# title_item.value  # -> '440Hz, subtitle'
# str(title_item)  # -> '440Hz, subtitle'


def read_data(audio_file):
    return music_tag.load_file(audio_file)


def write_tags(file):
    tags = read_data(file)
    tags.remove_tag('tracktitle')
    tags.append_tag('tracktitle', tracktitle)
    tags.remove_tag('artist')
    tags.append_tag('artist', artist)
    tags.remove_tag('genre')
    tags.append_tag('genre', genre)
    tags.save()


if __name__ == '__main__':
    tracktitle = 'Санаторий'
    artist = 'Сомерсет Моэм'
    genre = 'Audiobook'

    # write_tags(tracktitle)
    file = m4a_file
    write_tags(file)
    print(read_data(file))

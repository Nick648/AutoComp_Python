from pytube import YouTube


def display_info_stream(stream):
    print(f'{stream=}; Type: {type(stream)}')
    # stream=
    # <Stream: itag="22" mime_type="video/mp4"
    # res="720p" fps="30fps" vcodec="avc1.64001F"
    # acodec="mp4a.40.2" progressive="True" type="video">;
    print(f'{stream.default_filename=}; {stream.filesize=}; \n{stream.__dict__}')


def video_download(link='https://www.youtube.com/shorts/ben_PYvAWhs'):  # Only audio???!
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        # display_info_stream(stream)
        print('\tDownload successful!')
        print(f'Name: {stream.default_filename}\nSize: {stream.filesize}')
        print(f'Url video: {stream.url}')
    except Exception as ex:
        print(f'Error Name: {type(ex).__name__}; type: {type(ex)} -> {ex}')


if __name__ == '__main__':
    link = input('Enter video link(or just press Enter): ').strip()
    video_download(link)

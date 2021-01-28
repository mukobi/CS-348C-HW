import os
import argparse

def main():
    """Turn numbered images into a video."""
    parser = argparse.ArgumentParser(description='Turn numbered images into a video.')
    parser.add_argument('file', nargs='?', default='', help='Path to one of the input images to convert. Input image must end in ".{number}.{extension}", e.g. C:/render/beauty.final.0002.png')
    
    parser.add_argument('-f', '-r', '--framerate', default='24', help='Output frame rate (default: 24)')
    parser.add_argument('-b', '--bitrate', default='4', help='Output bit rate in Mbps (default: 4)')
    parser.add_argument('-e', '--extension', default='mov', help='Output file extension (default: mp4)')
    parser.add_argument('-p', '--promptoverwrite', action='store_false', help='Prompt before overwriting an existing file (default: false)')
    args = parser.parse_args()
    
    while (args.file == ''):
        args.file = input('Enter the path to one of the input images to convert.\nInput image must end in ".{number}.{extension}", e.g. C:/render/beauty.final.0002.png\n\n')

    split_file = args.file.strip('\'\"& ').split('.')
    split_file[-2] = f'%0{len(split_file[-2])}d' # 0001 to %04d
    formatted_source_file = '.'.join(split_file)
    output_file = '.'.join(split_file[:-2]) + '.' + args.extension.strip('.')

    command = (f'ffmpeg '
               f'{"-y " if args.promptoverwrite else ""}'
               f'-r {args.framerate} '
               f'-i "{formatted_source_file}" '
               f'-b:v {args.bitrate}M '
               f'"{output_file}" ')

    print(command)
    os.system(command)

if __name__ == "__main__":
    main()

import sys
import reports


def sys_args():
    ''' `python3 export.py source_file_name target_file_name input_year input_genre input_title` '''
    args = []
    n = len(sys.argv)
    for i in range(1, n):
        args.append(sys.argv[i])
        # print(sys.argv[i], end=" ")

    return args[0]


if __name__ == '__main__':
    print(sys_args())

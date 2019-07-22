from sys import version_info as vi


if int(f'{vi.major}{vi.minor}') < 37:
    raise Exception("incorrect version")
print("Hello ;P")

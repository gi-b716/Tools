import os
import sys

_ver_ = '1.0'

VERINFO = f"""
cpp-build-tool v{_ver_}
  --by GavinCQTD
"""
ABOUT = f"""
cpp-build-tool v{_ver_}
  --by GavinCQTD

使用 cb --h 获取命令帮助
"""
HELP = """
使用 cb [命令] 执行命令
命令列表：
    --h 显示此帮助
    --v 显示版本信息
"""

if len(sys.argv) == 1:
    print(ABOUT)

elif len(sys.argv) == 2:
    command = sys.argv[1]

    if command == "--v":
        print(VERINFO)
    elif command == "--h":
        print(HELP)
    else:
        print(f"未找到的命令：{command}")

elif len(sys.argv) >= 3:
    if sys.argv[1] == "--b":
        filename = sys.argv[2]
        filepath = os.getcwd()+'\\'+filename
        outputFilename = filename+".exe"
        os.system(f"g++ {filepath} -o {outputFilename}")
    elif sys.argv[1] == "--s":
        if sys.argv[2] == "-bs":
            pass

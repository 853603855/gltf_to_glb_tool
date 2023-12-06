import os


def execute_commands(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # 去掉行尾的换行符
            path = line.strip()
            # 空行跳过
            if path == "":
                continue
            # 拼装命令 gltf-pipeline -i modelNew.gltf -o model.glb
            origin_file_path = os.path.join(path, "modelNew.gltf")
            glb_file_path = os.path.join(path, "model.glb")
            # 加单引号是为了避免路径中的部分词组被系统识别为命令参数
            command = "gltf-pipeline -i '{}' -o '{}'".format(origin_file_path, glb_file_path)
            print(command)


if __name__ == "__main__":
    # 将下面的路径替换为你的命令文本文件路径
    file_path = r'file_list.txt'
    execute_commands(file_path)

import os
import re
import shutil
import subprocess
import socket
import svn.remote
import random, threading, webbrowser
from flask import Flask, request, jsonify, render_template, send_from_directory, url_for
from r3 import r3
from log import create_logger

app = Flask(__name__)

create_logger()
svn_url = 'http://7.185.114.218/svn/localversion/TigreVersion'
svn_user = 'lwx1193922'
svn_password = 'Test12345@'
# 本地文件夹
base_path = r'D:\AlphaPVersion\Tiger'
# 本地上传OTA文件夹
base_path_ota = r'D:\AlphaPVersion\TigreVersion'
# 本地文件OTA升级文件夹
remote_path = r'D:\localversion\TigreVersion'
# 版本文件夹
tiger_dir = []
# 获取当前ip
ip_adds = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
# 工具位置
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')


@app.route('/download_svn_tool', methods=['GET'])
def download_svn_tool():
    r3.info('开始下载SVN工具')
    return send_from_directory(UPLOAD_PATH, 'TortoiseSVN-1.13.1.28686-x64-svn-1.13.0.msi')


@app.route('/download_file', methods=['POST', 'GET'])
def download_file():
    if request.method == 'POST':
        result = request.form
        print(result, '--------------')
        # 获取请求参数
        svn_url = request.form.get('site')
        local_path = request.form.get('sites0')
        s = svn.remote.RemoteClient(svn_url, username=svn_user, password=svn_password)
        # 从 SVN 下载文件
        if not os.path.exists(local_path):
            os.mkdir(local_path)
        r3.info('下载地址为：', svn_url)
        r3.info('文件选择完成：下载地址为：', local_path)
        s.checkout(local_path)
        r3.info('文件下载完成')
        print('文件下载完成')
        # 返回结果
        # return jsonify({'msg': 'success'})
        return '文件选择完成：下载地址为：{}'.format(local_path)
    dir_lists = ['http://7.185.114.218/svn/localversion/DeviceTestTools',
                 'http://7.185.114.218/svn/kitty/KidWatchDeviceTest_Kitty',
                 'http://7.185.114.218/svn/tiger/KidWatchDeviceTest_Tiger',
                 'http://7.185.114.218/svn/localversion/TigreVersion/DeviceTestTools',
                 'http://7.185.114.218/svn/localversion/TigreVersion/脚本',
                 ]
    result_all = [r'D:\DeviceTestTools', r'D:\KidWatchDeviceTest_Kitty', r'D:\KidWatchDeviceTest_Tiger', r'D:\testSvn']
    return render_template('test_svn.html', dir_lists=dir_lists, result_all=result_all)


@app.route('/', methods=['POST', 'GET'])
def home_page():
    return render_template('ota_svn.html')


@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


# @app.get("/message")
@app.route('/message', methods=['GET'])
def get_message():
    count = request.args.get("count", 50)
    data = r3.get(count)
    return {"code": 200, "data": data, "msg": "ok"}


@app.route('/ota_upload_file', methods=['POST', 'GET'])
def ota_upload_file():
    # 上传文件到 SVN
    s = svn.remote.RemoteClient(svn_url, username=svn_user, password=svn_password)
    svn_list = []
    for i in s.list():
        svn_list.append(i.replace('/', ''))
    print('svn存在的文件夹：', svn_list)
    dir = r'D:\AlphaPVersion\Tiger'
    for i in os.listdir(dir):
        if i.startswith('Tiger-L10'):
            tiger_dir.append(i)
    file_lists = tiger_dir
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn) if os.path.isdir(dir + "\\" + fn) else 0)
    new_file = file_lists[-1]
    print('最新生成文件夹', new_file)
    r3.info('本次查询路径下的最新文件夹为：{}'.format(new_file))
    # 获取文件夹路径，进行移动上传
    start_dir = os.path.join(base_path_ota, new_file.replace(' ', ''))
    print(start_dir)
    if not os.path.exists(start_dir):
        os.mkdir(start_dir)
        print('创建文件夹成功', start_dir)
        r3.debug('文件夹创建成功:{}'.format(start_dir))
    end_dir = ''
    for root, dir, files in os.walk(dir):
        if 'ota_update' in root and root.endswith('OTA本地测试升级包') and new_file in root and 'log' in root:
            end_dir = root
    if 'OTA本地测试升级包' in os.listdir(start_dir):
        print('文件夹已经到对应版本路径下了！！！')
        r3.debug('文件夹已经到对应版本路径下了！！！')
    else:
        if end_dir:
            shutil.move(end_dir, start_dir)
            print('文件夹移动成功！！！')
            r3.debug('原始文件夹的路径为:{}'.format(end_dir))
            r3.debug('文件移动成功路径为:{}'.format(start_dir))
        else:
            r3.error('对应版本路径下不存在本地OTA升级文件夹')
            raise Exception('对应版本路径下不存在本地OTA升级文件夹')
    # 将升级文件复制到版本升级文件中
    update_ota_file = 'upgrade_dynamic_new.bat'
    version_ota_file = os.path.join(start_dir, 'OTA本地测试升级包')
    if update_ota_file not in os.listdir(version_ota_file):
        if os.path.exists(os.path.join(base_path_ota, update_ota_file)):
            shutil.copy(os.path.join(base_path_ota, update_ota_file), version_ota_file)
            print('升级文件复制成功！！！')

    new_path_version_dir_name = start_dir.rsplit('\\', 1)[1]
    if new_path_version_dir_name in svn_list:
        r3.info('文件:{}已经上传到SVN了'.format(new_path_version_dir_name))
        print('文件:{}已经上传到SVN了'.format(new_path_version_dir_name))
        # return '文件:{}已经上传到SVN了'.format(new_path_version_dir_name)
        return render_template('index.html')
    else:
        # # 创建文件夹
        # svn_sub_command = 'mkdir'
        # subDir = new_file
        # command_args = ["--parents", "-m", "创建svn文件夹："+subDir, str(svn_url+"/"+subDir).replace(' ', '%20')]
        # s.run_command(svn_sub_command, command_args)
        # 文件上传
        print('开始文件上传')
        r3.info('文件开始向svn上传')
        target_localfilePath = start_dir
        print(target_localfilePath)
        # 先执行add操作 --parents
        svn_sub_command_add = 'add'
        command_args_add = ["--parents", "--force", target_localfilePath]
        s.run_command(svn_sub_command_add, command_args_add)
        r3.info('文件svn添加成功')
        # 再执行commit操作
        svn_sub_command_commit = 'commit'
        command_args_commit = [target_localfilePath, '-m',
                               '本次提交的版本OTA文件：' + os.path.split(target_localfilePath)[-2]]
        s.run_command(svn_sub_command_commit, command_args_commit)
        print('文件上传完成:{}'.format(target_localfilePath))
        r3.info('SVN文件上传完成:{}'.format(target_localfilePath))
        return render_template('index.html')



progress_bar_ratio = 0
#供前端访问
def get_bar_ratio():
    global progress_bar_ratio
    return progress_bar_ratio


@app.route('/ota_download_file', methods=['POST', 'GET'])
def ota_download_file():
    local_path_dir = {}
    # 从 SVN 下载文件
    r3.info('OTA开始更新本地工程：{}'.format(svn_url))
    s = svn.remote.RemoteClient(svn_url, username=svn_user, password=svn_password)
    s.checkout(remote_path)
    r3.info('本地工程更新成功:{}'.format(remote_path))
    dir = remote_path
    for i in os.listdir(dir):
        if i.startswith('Tiger-L10'):
            tiger_dir.append(i)
    file_lists = tiger_dir
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn) if os.path.isdir(dir + "\\" + fn) else 0)
    new_file = file_lists[-1]
    end_dir = ''
    print('最新生成文件夹', new_file)
    # D:\localversion\TigreVersion\Tiger-L10 4.2.0.11(C00M00log)\OTA本地测试升级包
    for root, dir, files in os.walk(dir):
        if 'TigreVersion' in root and root.endswith('OTA本地测试升级包') and new_file in root:
            end_dir = root
            r3.info('本次OTA升级路径：{}'.format(end_dir))
    progress = 0
    # 获取设备sn号
    sn = []
    dir_lists = []
    dir_path = []
    sn_y = ['2SBYD23B21400875', '2SBYD23B21400843', '2SBYD23B21400847', '2SBYD23B21400846', '2SBYD23B21400856',
            '2SBYD24113400317', '2SBYD23B21400943', '2SBYD24218400388']
    list_device = {}
    fdout = os.popen('adb devices')
    devices = fdout.read()[:-1]
    if len(devices) != 0:
        lineList = (devices.split("\n"))
        for i in lineList:
            if len(str(i).split()) == 2:
                list_device[str(i).split()[0]] = str(i).split()[1]
        for i in list_device:
            if list_device[str(i)] == "device":
                sn.append(i)
                if i in sn_y:
                    sn_m = i
    dir_lists.append(new_file)
    dir_path.append(end_dir)
    local_path_dir[new_file] = end_dir

    if request.method == 'POST':
        result = request.form
        print(result)
        sn = request.form.get('sites0')
        if sn not in sn_y:
            r3.error('选择的Sn号不符合要求')
            return "选择的Sn号不符合要求"
        local_paths = request.form.get('site')
        cmd = 'adb -s {}  shell getprop ro.build.display.id'.format(sn)
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        stdout = result.stdout.read()
        st = str(stdout).split(' ')[-1]
        version_num = st.split(')')[0]
        local_paths_num = local_paths.split('L10')[-1].replace(')', '')
        r3.info('获取到的手表版本为：', version_num)
        r3.info('本次将要升级的版本：', local_paths_num)
        print(version_num)
        print(local_paths_num, '-------------------------------------------')
        # 检查版本是否一致
        # if local_paths_num == version_num:
        #     return "升级版本和本机版本相同"
        # else:
        #     print('*' * 100)
        #     print('手表版本为{}，升级版本为{}'.format(version_num, local_paths_num))
        #     r3.info('手表版本为{}，升级版本为{}'.format(version_num, local_paths_num))

        if len(local_paths_num) == len(version_num):
            if version_num <= local_paths_num:
                print('正常升级')
            else:
                r3.error("升级版本{}比,本机{}版本号低，".format(local_paths_num, version_num))
                return "升级版本{}比,本机{}版本号低，".format(local_paths_num, version_num)
        local_path = local_path_dir.get(local_paths)
        # print(sn, local_path, '----------------------------')
        if sn != '' and local_path != '':
            update = ''
            for i in os.listdir(local_path):
                if i.endswith('.zip'):
                    update = os.path.join(local_path, i)
            r3.info('1：开始为设备升级：{}'.format(sn))
            if r'D:\localversion\TigreVersion' not in update and local_paths not in update:
                r3.error('本地ota升级文件路径异常，请查看：{}'.format(update))
                raise Exception('本地ota升级文件路径异常，请查看：', update)
            print('升级路径：', local_path)
            print('文件路径为：', update)
            os.system('adb -s {} wait-for-device'.format(sn))
            os.system('adb -s {} root'.format(sn))
            os.system('adb -s {} wait-for-device'.format(sn))
            print('2：开始推送文件')
            r3.info('2：开始推送文件')
            if ' ' in update:
                raise Exception('文件路径中存在空格，不能进行文件推送')
            cmd_file = 'adb -s {} push {} /data/ota_package/update.zip'.format(sn, update)
            r3.debug('执行命令：{}'.format(cmd_file))
            result01 = subprocess.Popen(cmd_file, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
            for i in iter(result01.stdout.readline, 'b'):
                zc = r'\d+'
                if i in 'data/ota_package/update.zip':
                    progress = re.findall(zc, i)[0]
                if i == '':
                        break
            #     r3.info('文件推送进度：{}'.format(i))
            stdout01 = result01.stdout.read()
            if '100%' in str(stdout01):
                r3.info('3：文件推送完成开始OTA升级')
                os.system('adb -s {} shell "uncrypt /data/ota_package/update.zip /cache/recovery/block.map"'.format(sn))
                os.system('adb -s {} shell "echo --locale=zh-CN>>/cache/recovery/command"'.format(sn))
                os.system(
                    'adb -s {} shell "echo --update_package=@/cache/recovery/block.map>>/cache/recovery/command"'.format(
                        sn))
                os.system('adb -s {} shell sync'.format(sn))
                os.system('adb -s {} reboot recovery'.format(sn))
                os.system('adb -s {} wait-for-recovery'.format(sn))
                r3.info('4：手表进入recovery模式')
                os.system('adb -s {} wait-for-device'.format(sn))
                r3.info('5：手表升级完成')
                os.system('adb -s {} root'.format(sn))
                os.system('adb -s {} wait-for-device'.format(sn))
                r3.info('6：设备OTA升级成功')
                # return render_template('index.html')
            else:
                print('OTA包上传失败', stdout01)
                r3.error('OTA上传失败{}'.format(stdout01))
    return render_template('ota_svn_download.html', dir_lists=dir_lists, sn=sn,progress=progress)
    # return render_template('ota_svn_download.html')


if __name__ == '__main__':
    # port = 5000 + random.randint(0, 999)
    port = 5000
    url = "http://{}:{}".format(ip_adds, port)
    url_index = url + '/' + 'index'
    threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    # threading.Timer(1.25, lambda: webbrowser.open(url_index)).start()
    app.run(host=ip_adds, port=port, debug=True)

    # app.run(host=ip_adds, port=5000, debug=True)
"""
port = 5000 + random.randint(0, 999)
    url = "http://127.0.0.1:{0}".format(port)
    threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    app.run(port=port, debug=False)

"""
# svn = svn.remote.RemoteClient(svn_url, username=svn_user, password=svn_password)
# 创建文件夹
# svn_sub_command = 'mkdir'
# subDir = '4.2.0.12(C00M00log)'
# command_args = ["--parents", "-m", "python程序创建svn子目录："+subDir, str(svn_url+"/"+subDir).replace(' ', '%20')]
# svn.run_command(svn_sub_command, command_args)
# 文件上传
# target_localfilePath = r'D:\AlphaPVersion\TigreVersion\Tiger-L10 4.2.0.11(C00M00log)'
# # 先执行add操作
# svn_sub_command_add = 'add'
# command_args_add = ["--force", target_localfilePath]
# svn.run_command(svn_sub_command_add, command_args_add)
# # 再执行commit操作
# svn_sub_command_commit = 'commit'
# command_args_commit = [target_localfilePath, '-m', 'python3程序提交文件：'+os.path.split(target_localfilePath)[-1]]
# svn.run_command(svn_sub_command_commit, command_args_commit)
# print('上传完成')
# svn.run_command('update',['update'])

# svn.checkout(r'D:\AlphaPVersion\TigreVersion')

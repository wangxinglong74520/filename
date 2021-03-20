from flask import Flask, render_template
import setting

app = Flask(__name__)
app.config.from_object(setting)


@app.route('/')
def hello_world():
    msg = 'hello everyone hello world'
    li = [2, 3, 4, 7, 9, 10]
    return render_template('define.html', msg=msg, li=li)


# 过滤器本质也是函数
def replace_hello(value):
    print('--->', value)
    value = value.replace('hello', '')  # 替换
    print('2', value)
    return value.strip()  # 去除两边空格    将替换的结果返回


app.add_template_filter(replace_hello, 'replace')  # 第一种  自定义模板过滤器


# 第二中方式 装饰器
@app.template_filter('listreverse')
def reverse_list(li):
    temp_li = list(li)
    temp_li.reverse()  # 翻转
    return temp_li


if __name__ == '__main__':
    app.run()

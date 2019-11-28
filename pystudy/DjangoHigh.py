import os
#如果需要在一个单独的PY脚本文件中导入Django模块，下面是固定代码 booksystem1 是你的项目名，bookAPP是你的settings.py所在文件夹名

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booksystem.settings")
    import django
    django.setup()
    from bookAPP import models  #此处导入，必须在django.setup()后，因为只有启动Django才能执行，否则会报错

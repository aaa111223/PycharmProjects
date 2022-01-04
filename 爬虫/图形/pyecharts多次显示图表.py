from pyecharts import Bar, Line
from pyecharts.engine import create_default_environment

bar = Bar("�ҵĵ�һ��ͼ��", "�����Ǹ�����")
bar.add("��װ", ["����", "��ë��", "ѩ����", "����", "�߸�Ь", "����"], [5, 20, 36, 10, 75, 90])

line = Line("�ҵĵ�һ��ͼ��", "�����Ǹ�����")
line.add("��װ", ["����", "��ë��", "ѩ����", "����", "�߸�Ь", "����"], [5, 20, 36, 10, 75, 90])

env = create_default_environment("html")
# Ϊ��Ⱦ����һ��Ĭ�����û���
# create_default_environment(filet_ype)
# file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'

env.render_chart_to_file(bar, path='bar.html')
env.render_chart_to_file(line, path='line.html')
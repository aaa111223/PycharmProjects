from pyecharts import Bar

bar = Bar("�ҵĵ�һ��ͼ��", "�����Ǹ�����")
bar.use_theme('dark')
bar.add("��װ", ["����", "��ë��", "ѩ����", "����", "�߸�Ь", "����"], [5, 20, 36, 10, 75, 90])
bar.render()
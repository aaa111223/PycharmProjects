from pyecharts import Bar

bar = Bar("�ҵĵ�һ��ͼ��", "�����Ǹ�����")
bar.add("��װ", ["����", "��ë��", "ѩ����", "����", "�߸�Ь", "����"], [5, 20, 36, 10, 75, 90])
# bar.print_echarts_options() # ����ֻΪ�˴�ӡ������������ʱʹ��
bar.render()    # ���ɱ��� HTML �ļ�
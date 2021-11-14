"""
Программ для проекта Agrotech
Содержание:
Подключение базы данных
Логические блоки
пдкючение анализа фото 
Блок аботы интерфейса
"""
    
"""_______________________________________________________________________________________________________"""

# Логические блоки разделяются и принимают на себя определённые части расчётов
# Логический блок 1 принимает расчёт количества семечек, при вызове функции на её вход подаётся значение 
# площади круга и семечки взятые из расчётов Pytorch
def logical_block_1(area_circle, med_seed):
	# блок учёта отдельно взятой головы
	# Просчёт количества семян из положения (кол.сем = Sкруга /Sср.сем
	num_seeds = area_circle / med_seed
	if (area_circle % med_seed)>= 0.6:
		print(int(num_seeds+1))
	else:
		print(int(num_seeds))
"""_______________________________________________________________________________________________________"""
# Блок отвечающий за работу анализа фотографии с использование готовой библиотеке Pixellib 
# Особенноесть окружения: работает на версии Python 3.5-3.7.
import os
os.environ["TF_CCP_MIN_LOG_LEVEL"] = "3"

from pixellib.instance import instance_segmentation


def object_detection_on_an_image():
	segment_image = instance_segmentation()
	segment_image.load_model("C:\Users\Mavis\mask_rcnn_coco.h5")
    segment_image.segmentimage(
	    # В imade_path указывается путь к изображению для анализа
	    # Он будет братья из хранилища мобильного устройста и хранится в переменных
	    # Image_analit_path и Image_output_path
		image_path="Image_analit_path",
		show_bboxes=True,
		output_image_name="Image_output_path"
    )


def main():
	object_detection_on_an_image()
	
if __name__ == '__main__':
	main()
	
"""_______________________________________________________________________________________________________"""
# Логический блок 2. Предназначен для логики пользовательского интерфейса, предназначени для сбора 
# первичных данных
def logical_block_2():
    Hello_message = ("


"""_______________________________________________________________________________________________________"""

# Логический блок 3. Предназначение высчитывание средних значений урожайности со всех кубов
# 
def logic_block_3(


"""_______________________________________________________________________________________________________"""
#Подключение базы данных
#Подключение библиотеки
# Создание функции 
def get_database():
	from pymongo import MongoClient 
	import pymongo 
	
	# Создание переменной для подключения к базе данных
	CONNECTION_STRING = "mongodb+srv://mavisqwert:mavisqwert@agrotech.yqgql.mongodb.net/product_parametersDB?retryWrites=true&w=majority"
	
	client = MongoClient(CONNECTION_STRING)
	# создание базы данных (параметры продуктаДБ)
	dbname = client['product_parametersDB']
	# создание коллекций 
	collection_name =dbname["product_parametrs"]
	"""!!! Добавить блок проверки на содержание информации"""

class Memento:
	"""Класс снимка"""

	def __init__(self, state: str):
		"""
		Инициализируем объект снимка
		со всеми полями класса создателя
		"""
		self.__state = state

	def get_state(self) -> str:
		"""Возвращает состояние, хранящееся в снимке"""
		return self.__state


class Caretaker:
	"""Класс опекуна"""

	def __init__(self, memento: Memento):
		"""
		Инициализируем объект опекуна, передавая в него
		последний снимок (состояние) объекта создателя
		"""
		self.__memento = memento

	def get_memento(self) -> Memento:
		"""
		Полчуение последнего сохраненного
		снимка (состояния) объекта создателя
		"""
		return self.__memento


class Originator:
	"""Класс создателя"""

	def __init__(self, state: str):
		"""
		Инициализируем объект создателя
		(указываем все состояния, для которых может
		потребоваться снимок)
		"""
		self.__state = state

	@property
	def state(self) -> str:
		"""Геттер"""
		return self.__state

	@state.setter
	def state(self, state: str) -> None:
		"""Сеттер"""
		self.__state = state

	def save_state(self) -> Memento:
		"""Создание снимка"""
		return Memento(self.__state)

	def restore_state(self, memento: Memento) -> None:
		"""Возврат к предыдущему состоянию (через опекуна)"""
		self.__state = memento.get_state()


if __name__ == '__main__':

	# Объект создателя с состоянием "on"
	originator = Originator(state='on')
	print(originator.state)

	# Объект опекуна, хранящий последний снимок (состояние) создателя
	caretaker = Caretaker(originator.save_state())

	# Меняем состояние объекта
	originator.state = 'off'
	print(originator.state)

	# "Откатываемся" до предыдущего сосотяния
	originator.restore_state(caretaker.get_memento())
	print(originator.state)
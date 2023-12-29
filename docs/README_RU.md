
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=МЕНЕДЖЕР+ПРОЕКТИРОВАНИЯ+СТРУКТУР)](https://github.com/komanch7/projectstructuremanager)
---

### 🔥 Моя статистика:
[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=komanch7&theme=dark&background=0d1117)](https://github.com/komanch7/projectstructuremanager/pulse)

- Информация представлена ​​на нескольких языках:
    
    | [German](https://github.com/komanch7/projectstructuremanager/blob/main/docs/README_DE.md) |
    [Russian](https://github.com/komanch7/projectstructuremanager/blob/main/docs/README_RU.md) |
    [Ukrainian](https://github.com/komanch7/projectstructuremanager/blob/main/docs/README_UA.md) |


# projectstructuremanager
ProjectStructureManager — это проект Python для создания структур папок и файлов точно так, как разработчик смоделировал проект.

## ProjectStructureManager Структура
Проект имеет следующую структуру:
```
|--docs/
||--__init__.py
||--README_DE.md
||--README_RU.md
||--README_UA.md
|--psmanager/
||--__init__.py
||--project_structure_manager.py
|--tests/
||--__init__.py
||--test_psmanager.py
||--test_structure.json
|--LICENSE
|--main.py
|--README.md
|--requirements.txt
|--structure.json
```
## Технический стек

**Server:** Python 3.9^

---

# Клонировать этот репозиторий

```sh
gh repo clone komanch7/projectstructuremanager psm-pro

cd psm-cli

  или

git clone https://github.com/komanch7/projectstructuremanager psm-pro

cd psm-pro
```
## Создать и активировать виртуальную среду
```python
python -m venv venv

venv\Scripts\activate

python -m pip install --upgrade pip
  или
python3 -m pip install --upgrade pip
```
## Usage
```python
# main.py

from psmanager.project_structure_manager import ProjectStructureManager

if __name__ == "__main__":
    path = "."
    file_struct = "structure.json"
    manager = ProjectStructureManager(path, file_struct)
    manager.create_structure()
```
### Установка модулей из requirements.txt
- Если файл requirements.txt содержит модули, введите в терминале следующую команду:
```
pip install -r requirements.txt
```
## Команда запуска тестов
```
python -m unittest discover -s tests 
```
## Ответ
```bash
>> test_create_structure (test_psmanager.TestProjectStructureManager) ... ok
>> test_create_structure_with_content (test_psmanager.TestProjectStructureManager) ... ok
>> test_load_structure_from_json (test_psmanager.TestProjectStructureManager) ... ok
>> 
>> ----------------------------------------------------------------------
>> Ran 3 tests in 0.425s
>> 
>> OK
```

# Создать структуру
```python
python main.py
  или
python3 main.py
```
## Деактивировать среду
- Команда деактивации виртуальной среды по завершении работы
```
deactivate
```
### JSON модель тестового проекта
```json
{
    "mypackage": {
        "mypackage": {
            "controllers": {
                "__init__.py": "",
                "control_one.py": "",
                "control_two.py": "",
                "control_three.py": "",
                "control_four.py": ""
            },
            "__init__.py": "",
            "models": {
                "__init__.py": "",
                "model_one.py": "",
                "model_two.py": "",
                "model_three.py": "",
                "model_four.py": ""
            }
        },
        "__init__.py": "# None",
        "tests": {
            "__init__.py": "",
            "test_one.py": "",
            "test_two.py": "",
            "test_three.py": "",
            "test_four.py": ""
        },
        "docs": {
            "__init__.py": "",
            "README.md": ""
        },
        "main.py": "# main()",
        "requirements.txt": "# requirements.txt"
    }
}
```
## Тестовая структура
Структура папок и файлов будущего проекта:
```
|--mypackage/
||--mypackage/
|||--__init__.py
|||--controllers/
||||--__init__.py
||||--control_one.py
||||--control_two.py
||||--control_three.py
||||--control_four.py
|||--models/
||||--__init__.py
||||--model_one.py
||||--model_two.py
||||--model_three.py
||||--model_four.py
||--tests/
||||--__init__.py
||||--test_one.py
||||--test_two.py
||||--test_three.py
||||--test_four.py
||--__init__.py
||--docs/
||||--__init__.py
||||--README.md
||--main.py
||--requirements.txt
||--LICENSE
```
## 🚀 Обо мне
- Я новичок в разработке Python. Спасибо за понимание и поддержку.

## Лицензия
[MIT](https://github.com/komanch7/projectstructuremanager/LICENSE)


[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=МЕНЕДЖЕР+ПРОЕКТУВАННЯ+СТРУКТУР)](https://github.com/komanch7/projectstructuremanager)
---

### 🔥 My Stats:
[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=komanch7&theme=dark&background=0d1117)](https://github.com/komanch7/projectstructuremanager/pulse)

- Інформація представлена ​​кількома мовами:
    
    | [German](https://github.com/komanch7/projectstructuremanager/blob/main/docs/README_DE.md) |
    [Russian](https://github.com/komanch7/projectstructuremanager/blob/main/docs/README_RU.md) |
    [Ukrainian](https://github.com/komanch7/projectstructuremanager/blob/main/docs/README_UA.md) |


# projectstructuremanager
ProjectStructureManager це проект на Python для створення структур папок і файлів саме так, як розробник моделював проект.

## ProjectStructureManager Структур
Проект має таку структуру:
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
## Технічний стек

**Server:** Python 3.9^

---

# Клонуйте це сховище

```sh
gh repo clone komanch7/projectstructuremanager psm-pro

cd psm-cli

  або

git clone https://github.com/komanch7/projectstructuremanager psm-pro

cd psm-pro
```
## Створіть і активуйте віртуальне середовище
```python
python -m venv venv

venv\Scripts\activate

python -m pip install --upgrade pip
  or
python3 -m pip install --upgrade pip
```
## Використання
```python
# main.py

from psmanager.project_structure_manager import ProjectStructureManager

if __name__ == "__main__":
    path = "."
    file_struct = "structure.json"
    manager = ProjectStructureManager(path, file_struct)
    manager.create_structure()
```
### Встановлення модулів з requirements.txt
- Якщо файл requirements.txt містить моделі, введіть наступну команду в терміналі
```
pip install -r requirements.txt
```
## Команда для запуску тестів
```
python -m unittest discover -s tests 
```
## Відповідь
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

# Створіть структуру
```python
python main.py
  або
python3 main.py
```
## Деактивувати середовище
- Команда деактивації віртуального середовища після завершення роботи
```
deactivate
```
### JSON тестова модель проекту
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
## Структура тесту
Структура папок і файлів майбутнього проекту:
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
## 🚀 Про мене
– Я новачок у розробці Python. Дякуємо за розуміння та підтримку.

## Ліцензія
[MIT](https://github.com/komanch7/projectstructuremanager/LICENSE)

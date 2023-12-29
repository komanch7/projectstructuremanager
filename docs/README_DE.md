
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=PROJEKT+STRUKTUR+MANAGER)](https://github.com/komanch7/projectstructuremanager)
---

### 🔥 Meine Statistiken:
[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=komanch7&theme=dark&background=0d1117)](https://github.com/komanch7/projectstructuremanager/pulse)

- Die Informationen werden in mehreren Sprachen präsentiert:
    
    | [German](https://github.com/komanch7/projectstructuremanager/blob/main/docs/README_DE.md) |
    [Russian](https://github.com/komanch7/projectstructuremanager/blob/main/docs/README_RU.md) |
    [Ukrainian](https://github.com/komanch7/projectstructuremanager/blob/main/docs/README_UA.md) |


# projectstructuremanager
ProjectStructureManager ist ein Python-Projekt zum Erstellen von Ordner- und Dateistrukturen genau so, wie der Entwickler das Projekt modelliert hat.

## ProjectStructureManager-Struktur
Das Projekt hat die folgende Struktur:
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
## Tech-Stack

**Server:** Python 3.9^

---
# Klonen Sie dieses Repository

```sh
gh repo clone komanch7/projectstructuremanager psm-pro

cd psm-cli

  oder

git clone https://github.com/komanch7/projectstructuremanager psm-pro

cd psm-pro
```
## Erstellen und Aktivieren einer virtuellen Umgebung
```python
python -m venv venv

venv\Scripts\activate

python -m pip install --upgrade pip
  oder
python3 -m pip install --upgrade pip
```
## Verwendung
```python
# main.py

from psmanager.project_structure_manager import ProjectStructureManager

if __name__ == "__main__":
    path = "."
    file_struct = "structure.json"
    manager = ProjectStructureManager(path, file_struct)
    manager.create_structure()
```
### Module aus „requirements.txt“ installieren
- Wenn die Datei „requirements.txt“ Modelle enthält, geben Sie den folgenden Befehl im Terminal ein
```
pip install -r requirements.txt
```
## Befehl zum Ausführen von Tests
```
python -m unittest discover -s tests 
```
## Antwort
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

# Erstellen Sie die Struktur
```python
python main.py
  oder
python3 main.py
```
## Umgebung deaktivieren
- Befehl zum Deaktivieren der virtuellen Umgebung nach Abschluss der Arbeiten
```
deactivate
```
### JSON-Testprojektmodell
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
## Teststruktur
Ordner- und Dateistruktur für das zukünftige Projekt:
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
## 🚀 Über mich
- Ich bin ein Anfänger in der Python-Entwicklung. Vielen Dank für Ihr Verständnis und Ihre Unterstützung.

## Lizenz
[MIT](https://github.com/komanch7/projectstructuremanager/LICENSE)

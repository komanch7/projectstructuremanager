# main.py

from psmanager.project_structure_manager import ProjectStructureManager

if __name__ == "__main__":
    path = "."
    file_struct = "structure.json"
    manager = ProjectStructureManager(path, file_struct)
    manager.create_structure()

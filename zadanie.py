import sys
import json
import yaml
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox


def json_to_xml(json_data):
    root = ET.Element('root')
    json_to_xml_recursive(json_data, root)
    return root


def json_to_xml_recursive(json_data, parent):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if isinstance(value, (dict, list)):
                element = ET.SubElement(parent, key)
                json_to_xml_recursive(value, element)
            else:
                ET.SubElement(parent, key).text = str(value)
    elif isinstance(json_data, list):
        for item in json_data:
            json_to_xml_recursive(item, parent)


def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f'Błąd podczas wczytywania pliku JSON: {e}')
        return None


def save_to_xml_file(root, file_path):
    try:
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print(f'Dane zostały zapisane do pliku {file_path}')
    except Exception as e:
        print(f'Błąd podczas zapisywania do pliku XML: {e}')


def load_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except Exception as e:
        print(f'Błąd podczas wczytywania pliku YAML: {e}')
        return None


def save_to_json_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f'Dane zostały zapisane do pliku {file_path}')
    except Exception as e:
        print(f'Błąd podczas zapisywania do pliku JSON: {e}')


def save_to_yaml_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.safe_dump(data, file)
        print(f'Dane zostały zapisane do pliku {file_path}')
    except Exception as e:
        print(f'Błąd podczas zapisywania do pliku YAML: {e}')


class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Konwerter danych')
        self.layout = QVBoxLayout()

        self.file_label = QLabel('Wybierz plik do konwersji:')
        self.layout.addWidget(self.file_label)

        self.file_button = QPushButton('Wybierz plik')
        self.file_button.clicked.connect(self.choose_file)
        self.layout.addWidget(self.file_button)

        self.name_label = QLabel('Podaj nazwę pliku wynikowego:')
        self.layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)

        self.format_label = QLabel('Wybierz format wynikowy:')
        self.layout.addWidget(self.format_label)

        self.format_input = QComboBox()
        self.format_input.addItem('json')
        self.format_input.addItem('xml')
        self.format_input.addItem('yaml')
        self.layout.addWidget(self.format_input)

        self.convert_button = QPushButton('Konwertuj')
        self.convert_button.clicked.connect(self.convert_file)
        self.layout.addWidget(self.convert_button)

        self.status_label = QLabel()
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        self.file_button.setText(file_path)

    def convert_file(self):
        input_file = self.file_button.text()
        output_file = self.name_input.text() + '.' + self.format_input.currentText()

        input_format = input_file.split('.')[-1]

        if input_format == 'json':
            data = load_json_file(input_file)
        elif input_format == 'xml':
            data = load_yaml_file(input_file)
        elif input_format == 'yaml':
            data = load_yaml_file(input_file)
        else:
            self.status_label.setText('Nieprawidłowy format wejściowy')
            return

        if self.format_input.currentText() == 'json':
            save_to_json_file(data, output_file)
        elif self.format_input.currentText() == 'xml':
            save_to_xml_file(json_to_xml(data), output_file)
        elif self.format_input.currentText() == 'yaml':
            save_to_yaml_file(data, output_file)
        else:
            self.status_label.setText('Nieprawidłowy format wynikowy')

        self.status_label.setText('Konwersja udana')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter_app = ConverterApp()
    converter_app.show()
    sys.exit(app.exec_())

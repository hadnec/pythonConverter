import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
import asyncio

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f'Błąd podczas wczytywania pliku JSON: {e}')
        return None

async def save_to_json_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            await asyncio.sleep(0.1)
            print(f'Dane zostały zapisane do pliku {file_path}')
    except Exception as e:
        print(f'Błąd podczas zapisywania do pliku JSON: {e}')

def load_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except Exception as e:
        print(f'Błąd podczas wczytywania pliku YAML: {e}')
        return None

async def save_to_yaml_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file)
            await asyncio.sleep(0.1)
            print(f'Dane zostały zapisane do pliku {file_path}')
    except Exception as e:
        print(f'Błąd podczas zapisywania do pliku YAML: {e}')

def load_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except Exception as e:
        print(f'Błąd podczas wczytywania pliku XML: {e}')
        return None

async def save_to_xml_file(root, file_path):
    try:
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        await asyncio.sleep(0.1)
        print(f'Dane zostały zapisane do pliku {file_path}')
    except Exception as e:
        print(f'Błąd podczas zapisywania do pliku XML: {e}')

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    return file_path

def save_file_dialog():
    file_path = filedialog.asksaveasfilename()
    return file_path

async def handle_load_json():
    file_path = open_file_dialog()
    if file_path:
        data = load_json_file(file_path)
        if data:
            print(f'Wczytano dane z pliku JSON: {data}')

async def handle_save_json():
    file_path = save_file_dialog()
    if file_path:
        data = {'example': 'data'}
        await save_to_json_file(data, file_path)

async def handle_load_yaml():
    file_path = open_file_dialog()
    if file_path:
        data = load_yaml_file(file_path)
        if data:
            print(f'Wczytano dane z pliku YAML: {data}')

async def handle_save_yaml():
    file_path = save_file_dialog()
    if file_path:
        data = {'example': 'data'}
        await save_to_yaml_file(data, file_path)

async def handle_load_xml():
    file_path = open_file_dialog()
    if file_path:
        root = load_xml_file(file_path)
        if root:
            print(f'Wczytano dane z pliku XML')

async def handle_save_xml():
    file_path = save_file_dialog()
    if file_path:
        root = ET.Element('root')
        await save_to_xml_file(root, file_path)

async def main():
    root = tk.Tk()

    btn_load_json = tk.Button(root, text='Wczytaj JSON', command=lambda: asyncio.create_task(handle_load_json()))
    btn_load_json.pack()

    btn_save_json = tk.Button(root, text='Zapisz JSON', command=lambda: asyncio.create_task(handle_save_json()))
    btn_save_json.pack()

    btn_load_yaml = tk.Button(root, text='Wczytaj YAML', command=lambda: asyncio.create_task(handle_load_yaml()))
    btn_load_yaml.pack()

    btn_save_yaml = tk.Button(root, text='Zapisz YAML', command=lambda: asyncio.create_task(handle_save_yaml()))
    btn_save_yaml.pack()

    btn_load_xml = tk.Button(root, text='Wczytaj XML', command=lambda: asyncio.create_task(handle_load_xml()))
    btn_load_xml.pack()

    btn_save_xml = tk.Button(root, text='Zapisz XML', command=lambda: asyncio.create_task(handle_save_xml()))
    btn_save_xml.pack()

    root.mainloop()

if __name__ == '__main__':
    asyncio.run(main())
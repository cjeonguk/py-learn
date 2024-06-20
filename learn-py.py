template_list_complex = [
    {
        "name": "learn-py.py",
        "path": "learn-py.py",
        "type": "file",
        "content": "print('Hello, Python!')",
    },
    {
        "name": "mod.py",
        "path": "mod.py",
        "type": "file",
        "content": "...",
    },
]

# template_list_complex.sort(key=lambda x: x["name"], reverse=True)
print(sorted(template_list_complex, key=lambda x: x["name"], reverse=True))
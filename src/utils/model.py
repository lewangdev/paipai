#coding=utf8
import json

models = {}
with open('models.json', "r") as modelsfile:
    content = modelsfile.read()
    models = json.loads(content)

if __name__ == '__main__':
    print models

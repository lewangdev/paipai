#coding=utf8
import json

models = {}
try:
    with open('models.json', "r") as modelsfile:
        content = modelsfile.read()
    models = json.loads(content)
except:
    import pre_models
    models = pre_models.pre_win_models

if __name__ == '__main__':
    print models

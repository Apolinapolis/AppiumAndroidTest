import os

device_name = os.getenv('deviceName')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
app = os.getenv('app', './app-gms-release_test.2.19.0.1414.apk')
run_on_bstack = app.startswith('bs://')
bstack_userName = os.getenv('bstack_userName', 'iakivkramarenko_sKlOLN')
bstack_accessKey = os.getenv('bstack_accessKey', 'FSHAmKdKHs3XsDkg35zT')
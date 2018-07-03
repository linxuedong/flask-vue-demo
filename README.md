# flask-vue-demo
两种全栈单页面应用 Demo：
- Flask-AppBuilder + Vue 前后端不分离应用，保留 Flask-AppBuilder 菜单
- Flask + Vue 前后端分离的单页面应用


# Flask-appbuilder + Vue
```bash
# 如果没使用过 virtualenvwrapper ，请参见官方文档  https://virtualenvwrapper.readthedocs.io/en/latest/
workon venv
pip install -r requirements.txt

# 在 flask-vue-demo 目录下
cd fab

# Create superuser
fabmanager create-admin

# Run server
fabmanager run
```



# Flask + Vue
### Backend
```bash
workon venv
pip install -r requirements.txt

# 在 flask-vue-demo 目录下
cd backend

# Run server
export FLASK_APP=run.py
flask run
```

### Frontend
```bash
# 在 flask-vue-demo 目录下
cd frontend
# Install front-end
npm install

# Build production static files
npm run build

# Run server
npm run dev
```

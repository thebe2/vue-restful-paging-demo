# 一个前后端分离的列表示例，支持动态翻页

## 前端使用jquery+bootstrap+vue2.0

## 后端使用Restful API 提供服务
* Python 版由Flask提供服务
* Node 版由express提供服务

## Python版服务
项目依赖
-flask
-flask-restful

使用方法：
1. 安装Python2.7和pip
2. pip python > requirements.txt
3. 命令行运行 <code>python app.py</code>
4. 浏览器中打开<code>127.0.0.1:5000 </code>

## Node版服务
### Keywords

- Vue
- Express
- Nodemon
- Webpack
- Npm


### Structure

```
.
├── LICENSE
├── README.md
├── index.js
├── nodemon.json
├── package.json
├── src
│   ├── client
│   │   ├── App.vue
│   │   ├── components
│   │   │   └── Hello.vue
│   │   └── index.js
│   └── server
│       ├── index.js
│       ├── public
│       │   └── favicon.ico
│       ├── router.js
│       └── views
│           ├── error.jade
│           └── index.jade
└── webpack.config.js
```

### Usage

1. Install dependencies

   `npm install`

2. Run the application

   `npm run dev`
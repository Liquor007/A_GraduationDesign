在这里我假设您没有直接下载我的项目，而是准备按照步骤一步一步部署。  
开始之前请先完成[这里](https://hooray.gitee.io/fantastic-admin/guide/ready.html)的准备工作，直接下载example以及前端需要的工具。  
做好准备工作后，可以用vscode打开项目  
在vscode里打开terminal（不会的可以百度orGoogle）
在terminal里输入下面的代码，切换到example文件夹
```
cd example
```
进入example文件夹后，继续在下一行输入
```
pnpm install
pnpm run dev
```
就可以看到登陆页面
# npm简介
npm，全名 node package manger。

npm 是Node的开放式模块登记和管理系统，是Node.js包的标准发布平台，用于Node.js包的发布、传播、依赖控制，网址：https://www.npmjs.com/
## npm run
npm 不仅可以用于模块管理，还可以用于执行脚本。**package.json** 文件有一个 **scripts** 字段，可以用于指定**脚本命令**，供npm直接调用。

刚刚我们在命令行里输入了
```
pnpm run dev
```
我们找到example文件夹下的package.json文件，打开后可以看到下面的代码：
```
"scripts": {
    "dev": "vite",
    "build:example": "vue-tsc --noEmit && vite build --mode example",
    "serve:example": "http-server ./dist-example -o",
    "svgo": "svgo -f src/assets/icons",
    "new": "plop",
    "lint": "npm-run-all -s lint:tsc lint:eslint lint:stylelint",
    "lint:tsc": "vue-tsc --noEmit",
    "lint:eslint": "eslint src/**/*.{ts,tsx,vue} --cache --fix --no-ignore --no-error-on-unmatched-pattern",
    "lint:stylelint": "stylelint src/**/*.{css,scss,vue} --cache --fix --allow-empty-input",
    "postinstall": "simple-git-hooks && esno scripts/prepare.js",
    "preinstall": "npx only-allow pnpm"
  },
```
其中，第一行就有dev键，而它对应的值vite就是对应的shell命令

npm run 命令会自动在环境变量 $PATH 添加 node_modules/.bin 目录，所以 scripts 字段里面调用命令时不用加上路径，这就避免了全局安装 NPM 模块。

npm run 如果不加任何参数，直接运行，会列出 package.json 里面所有可以执行的脚本命令。

npm内置了两个命令简写，npm test 等同于执行 npm run test，npm start 等同于执行 npm run start。

## package.json 脚本命令
npm 脚本的原理非常简单。每当执行npm run，就会自动新建一个 Shell，在这个 Shell 里面执行指定的脚本命令。

因此，只要是 Shell（Bash）可以运行的命令，就可以写在 npm 脚本里面。

比较特别的是，npm run新建的这个 Shell，会将当前目录的node_modules/.bin子目录加入PATH变量，执行结束后，再将PATH变量恢复原样。

这意味着，当前目录的node_modules/.bin子目录里面的所有脚本，都可以直接用脚本名调用，而不必加上路径。比如，当前项目的依赖里面有 Mocha，只要直接写mocha test就可以了。
```
"test": "mocha test"
```
而不是下面这样：
```
"test": "./node_modules/.bin/mocha test"
```
更多关于shell的语法知识可以看[这里](https://www.runoob.com/linux/linux-shell.html)
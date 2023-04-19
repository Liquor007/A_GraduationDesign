# 修改 页面标题
![1](.\img\1.png)
查看[这里](https://hooray.gitee.io/fantastic-admin/guide/configure.html)

可以看到有三套环境配置

开发环境下的文件.enc.development是这样的
```
# 页面标题
VITE_APP_TITLE = Fantastic-admin
# 接口请求地址，会设置到 axios 的 baseURL 参数上
VITE_APP_API_BASEURL = /
# 调试工具，可设置 eruda 或 vconsole，如果不需要开启则留空
VITE_APP_DEBUG_TOOL =

# 是否开启代理
VITE_OPEN_PROXY = false
```
其中 VITE_APP_TITLE VITE_APP_API_BASEURL VITE_APP_DEBUG_TOOL 为必要配置，即不管是在开发、测试，还是生产环境都需要使用到。而其余配置则在不同环境下有不同用途，例如开发环境用于本地开发使用，测试环境和生产环境用于构建使用。


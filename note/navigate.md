# 相关文件
\src\router\routes.ts,修改成这样
```
import MultilevelMenuExample from './modules/multilevel.menu.example'
import BreadcrumbExample from './modules/breadcrumb.example'
// 动态路由（异步路由、导航栏路由）
const asyncRoutes: Route.recordMainRaw[] = [
  {
    meta: {
      title: '介绍',
      icon: 'sidebar-default',
    },
    children: [
      MultilevelMenuIntro,
    ],
  },
  {
    meta: {
      title: '数据',
      icon: 'sidebar-default',
    },
    children: [
      MultilevelMenuPerInfo,
      MultilevelMenuTeamInfo,
    ],
  },
  {
    meta: {
      title: '搜索',
      icon: 'sidebar-default',
    },
  },
]
```
# 数据
数据模块逻辑：
点击数据，载入用户个人文件夹以及图表
点击左侧具体的表，载入表格内容  
admin\src\router\modules\multilevel.menu.PerInfo.ts
## 文件夹、数据表的增删改利用右键实现：
Vue中有很多内置指令，例如：v-if、v-for、v-model，它除了这些内置指令外，还允许我们开发者自己注册指令，来实现我们想实现的效果，对Vue自定义指令不熟悉的开发者可以先看一下文档：[自定义指令](https://cn.vuejs.org/guide/reusability/custom-directives.html#introduction)。  
实现思路：  
布局右键菜单，编写样式  
将右键菜单需要的用到的数据在vuex中进行定义  
全局注册一个指令，命名为rightClick  
拦截被绑定元素的oncontextmenu事件，对组件传过来的值进行处理  
更新vuex里的右键菜单数据，触发右键菜单显示  

新增admin\src\components\RightClick文件夹


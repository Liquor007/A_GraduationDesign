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
点击数据，载入文件夹增删改(admin\src\views\multilevel_menu_PerInfo\folders.vue)  
点击文件夹，载入表格增删改(admin\src\views\multilevel_menu_PerInfo\forms.vue)
点击表格，载入图片数据项增删改查(admin\src\views\multilevel_menu_PerInfo\images.vue)
点击图片，显示图片  
admin\src\router\modules\multilevel.menu.PerInfo.ts


# 工作台菜单设置-er_workbench_setting

## 工作台菜单设置-多语言表 t_er_workbench_setting_l

- **表名称：** 工作台菜单设置-多语言表
- **表名：** t_er_workbench_setting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 功能/菜单名称 | varchar | 200 |  | √ | ' ' | 功能/菜单名称 |
| 3 | fmenutypename | fmenutypename | varchar | 200 |  | √ | ' ' |  |
| 4 | fappnumname | 所属应用名称 | varchar | 200 |  | √ | ' ' | 所属应用名称 |
| 5 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 6 | fbilltypename | 单据类型名称 | varchar | 200 |  | √ | ' ' | 单据类型名称 |
| 7 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 8 | fmenugroupname | 上级菜单名称 | varchar | 200 |  | √ | ' ' | 上级菜单名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_workbench_setting_l |  | fpkid |
| 2 | idx_er_workbench_setting_l |  | fid,flocaleid |

---

## 工作台菜单设置-主表 t_er_workbench_setting

- **表名称：** 工作台菜单设置-主表
- **表名：** t_er_workbench_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparameter | 入口参数 | varchar | 500 |  | √ | ' ' | 入口参数 |
| 3 | fcolor | 颜色 | varchar | 50 |  | √ | ' ' | 颜色 |
| 4 | fmenuorder | 菜单序号(预留字段) | int4 | 32 |  | √ | 0 | 菜单序号(预留字段) |
| 5 | fappnum | 所属应用或特性 | varchar | 50 |  | √ | ' ' | 所属应用或特性,枚举: tra :人人差旅 exp :人人费用 cexp :对公费用 report :看板&报表 trip :外部应用 other :其他 |
| 6 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | ficon | 菜单图标URL | varchar | 500 |  | √ | ' ' | 菜单图标URL |
| 10 | fsupplier | 第三方服务商 | varchar | 50 |  | √ | ' ' | 第三方服务商,枚举: ALI :阿里商旅 ALIQIYEMA :阿里企业码 CHAILVYIHAO :差旅壹号 DIDI :滴滴 FANJIA :泛嘉 GAODE :高德 MEITUAN_NEW :美团商企通 MEIYA :美亚 QICHENG :企橙 TONGCHENG :同城 XIECHENG :携程 mscanquickreim :一键报销 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | foperationtype | 第三方服务类型 | varchar | 50 |  | √ | ' ' | 第三方服务类型,枚举: home :首页 list :订单 car :用车 plane :机票 hotel :酒店 train :火车 dinner :用餐 |
| 14 | fopentype | 打开方式 | varchar | 50 |  | √ | ' ' | 打开方式,枚举: form :表单 list :列表 |
| 15 | fappnumname | 所属应用名称 | varchar | 100 |  | √ | ' ' | 所属应用名称 |
| 16 | fformid | 业务实体 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fmenugroupname | 上级菜单名称 | varchar | 100 |  | √ | ' ' | 上级菜单名称 |
| 18 | fname | 功能/菜单名称 | varchar | 100 |  | √ | ' ' | 功能/菜单名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fismobile | 移动端 | bpchar | 1 |  | √ | '0' | 移动端 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fmenugroup | 上级功能/菜单 | varchar | 50 |  | √ | ' ' | 上级功能/菜单,枚举: quickiniate :快速发起 trip :商旅&消费 query :查询 |
| 23 | fmenutype | 菜单类型 | varchar | 50 |  | √ | ' ' | 菜单类型,枚举: 1 :业务对象 2 :外部url |
| 24 | fbilltypename | 单据类型名称 | varchar | 100 |  | √ | ' ' | 单据类型名称 |
| 25 | fisvisible | 首页默认可见 | bpchar | 1 |  | √ | '0' | 首页默认可见 |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | furl | URL | varchar | 255 |  | √ | ' ' | URL |
| 28 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_workbench_setting |  | fid |
| 2 | idx_er_workbench_setting |  | fnumber |

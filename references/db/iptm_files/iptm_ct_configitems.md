# 传输对象-iptm_ct_configitems

## 传输对象-主表 t_iptm_ct_configitems

- **表名称：** 传输对象-主表
- **表名：** t_iptm_ct_configitems

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forderfield | 实施排序码 | varchar | 50 |  | √ | ' ' | 实施排序码 |
| 3 | fgroupid | 配置项分组 | int8 | 64 |  | √ | 0 | [传输对象左树 iptm_ct_configtree](../iptm_files/iptm_ct_configtree.md) |
| 4 | fcustparampage | 添加传输自定义页面标识 | varchar | 50 |  | √ | ' ' | 添加传输自定义页面标识 |
| 5 | fcustompage | 自定义列表表单模板 | varchar | 50 |  | √ | ' ' | 自定义列表表单模板 |
| 6 | fpageenterparam | 列表页面入口参数 | varchar | 2000 |  | √ | ' ' | 列表页面入口参数 |
| 7 | fcanexportall | 允许批量打包 | bpchar | 1 |  | √ | ' ' | 允许批量打包 |
| 8 | frightpage | 验权页面 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 9 | fispreset | 是否系统预置 | bpchar | 1 |  | √ | ' ' | 是否系统预置 |
| 10 | frelylevel | 依赖级次 | int8 | 64 |  | √ | 0 | 依赖级次 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fplugin | 参数 | varchar | 2000 |  | √ | ' ' | 参数 |
| 16 | fimporttemplateid | 导入导出模板id | varchar | 50 |  | √ | ' ' | 导入导出模板id |
| 17 | fimporttype | 传输方式 | varchar | 50 |  | √ | ' ' | 传输方式,枚举: excel :Excel导入导出 json :JSONl导入导出 custom :插件l导入导出 microService :微服务l导入导出 |
| 18 | fconfigtype | 配置类型 | varchar | 50 |  | √ | ' ' | 配置类型,枚举: A :基础配置 B :基础数据 |
| 19 | fname | 配置项名称 | varchar | 255 |  | √ | ' ' | 配置项名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fpagetype | 列表表单类型 | varchar | 50 |  | √ | ' ' | 列表表单类型,枚举: bos_list :标准列表(bos_list) bos_templatetreelist :标准树列表(bos_templatetreelist) bos_treelist :树形列表(bos_treelist) bos_dynamicform :动态表单 custom :自定义 |
| 22 | fpage | 配置表单 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fsupportaddtopacket | 支持传输 | bpchar | 1 |  | √ | ' ' | 支持传输 |
| 25 | fcontrolled | 是否受控 | bpchar | 1 |  | √ | ' ' | 是否受控 |
| 26 | fisoverrideentry | 导入是否覆盖分录 | bpchar | 1 |  | √ | ' ' | 导入是否覆盖分录 |
| 27 | fhelptext | 帮助信息后台字段 | varchar | 2000 |  | √ | ' ' | 帮助信息后台字段 |
| 28 | fexplain_tag | 备注_详情 | text | 0 |  |  | ' ' | 备注_详情 |
| 29 | fexportfilters | 条件 | varchar | 255 |  | √ | ' ' | 条件 |
| 30 | fexportfilters_tag | 条件_详情 | text | 0 |  |  | ' ' | 条件_详情 |
| 31 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fdataimporttype | 导入数据更新方式 | varchar | 50 |  | √ | ' ' | 导入数据更新方式,枚举: new :添加新数据 override :更新已有数据 overridenew :更新已有数据并添加新数据 |
| 33 | fkeyfields | 数据替换规则的唯一值 | varchar | 2000 |  | √ | ' ' | 数据替换规则的唯一值,枚举: |
| 34 | fnumber | 配置项编码 | varchar | 100 |  | √ | ' ' | 配置项编码 |
| 35 | fexplain | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 36 | fexportfiltersdesc | 默认过滤条件 | varchar | 2000 |  | √ | ' ' | 默认过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_ct_configitems |  | fid |
| 2 | idx_iptm_ct_configitems_fnum |  | fnumber |

---

## 配置依赖分录-子表 t_iptm_ct_itemrelyentry

- **表名称：** 配置依赖分录-子表
- **表名：** t_iptm_ct_itemrelyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelyrelationfield | 依赖关联字段 | varchar | 500 |  | √ | ' ' | 依赖关联字段,枚举: |
| 3 | fdeclare | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | frelyitem | 依赖配置项 | int8 | 64 |  | √ | 0 | [传输对象 iptm_ct_configitems](../iptm_files/iptm_ct_configitems.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbasedatapropfield | fbasedatapropfield | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_ct_itemrelyentry |  | fentryid |
| 2 | idx_iptm_ct_itemrelyentry_fid |  | fid |

---

## 传输对象-多语言表 t_iptm_ct_configitems_l

- **表名称：** 传输对象-多语言表
- **表名：** t_iptm_ct_configitems_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 配置项名称 | varchar | 255 |  | √ | ' ' | 配置项名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_ct_configitems_l |  | fpkid |
| 2 | idx_iptm_ct_configitems_l_fid |  | fid |

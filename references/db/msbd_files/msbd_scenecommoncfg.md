# 场景工作台表单通用配置-msbd_scenecommoncfg

## 场景工作台表单通用配置-主表 t_msbd_sccomcfg

- **表名称：** 场景工作台表单通用配置-主表
- **表名：** t_msbd_sccomcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbizdatekey | 业务日期标识 | varchar | 50 |  | √ | ' ' | 业务日期标识 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fbizorgkey | 业务组织标识 | varchar | 50 |  | √ | ' ' | 业务组织标识 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | finvokemenukey | 场景菜单触发字段 | varchar | 50 |  | √ | ' ' | 场景菜单触发字段 |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fbilllistformid | 单据列表页面 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fbelongformid | 所属页面 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msbd_sccomcfg |  | fid |
| 2 | idx_msbd_sccomcfg_m0 |  | fmasterid |

---

## 工具栏按钮配置-子表 t_msbd_sccomcfg_toolbar

- **表名称：** 工具栏按钮配置-子表
- **表名：** t_msbd_sccomcfg_toolbar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbaritemcheckisselect | 校验是否有选择行 | bpchar | 1 |  | √ | '0' | 校验是否有选择行 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbaritemkey | 标识 | varchar | 50 |  | √ | ' ' | 标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_sccomcfg_toolbar_fk |  | fid |
| 2 | pk_msbd_sccomcfg_toolbar |  | fentryid |

---

## 工具栏按钮执行操作配置-子表 t_msbd_sccomcfg_toolbarop

- **表名称：** 工具栏按钮执行操作配置-子表
- **表名：** t_msbd_sccomcfg_toolbarop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaritemopignore | 忽略失败结果 | bpchar | 1 |  | √ | '0' | 忽略失败结果 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fbaritemopkey | 标识 | varchar | 50 |  | √ | ' ' | 标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_sccomcfg_toolbarop_fk |  | fentryid |
| 2 | pk_msbd_sccomcfg_toolbarop |  | fdetailid |

---

## 场景工作台表单通用配置-多语言表 t_msbd_sccomcfg_l

- **表名称：** 场景工作台表单通用配置-多语言表
- **表名：** t_msbd_sccomcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msbd_sccomcfg_l |  | fpkid |
| 2 | idx_msbd_sccomcfg_l_0 |  | fid,flocaleid |

---

## 场景菜单清单执行操作配置-子表 t_msbd_sccomcfg_menuop

- **表名称：** 场景菜单清单执行操作配置-子表
- **表名：** t_msbd_sccomcfg_menuop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmenuitemopkey | 标识 | varchar | 50 |  | √ | ' ' | 标识 |
| 2 | fmenuitemopignore | 忽略失败结果 | bpchar | 1 |  | √ | '0' | 忽略失败结果 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msbd_sccomcfg_menuop |  | fdetailid |
| 2 | idx_msbd_sccomcfg_menuop_fk |  | fentryid |

---

## 场景菜单清单配置-多语言表 t_msbd_sccomcfg_menu_l

- **表名称：** 场景菜单清单配置-多语言表
- **表名：** t_msbd_sccomcfg_menu_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmenuitemname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msbd_sccomcfg_menu_l |  | fpkid |
| 2 | idx_msbd_sccomcfg_menu_l_0 |  | fentryid,flocaleid |

---

## 场景菜单清单配置-子表 t_msbd_sccomcfg_menu

- **表名称：** 场景菜单清单配置-子表
- **表名：** t_msbd_sccomcfg_menu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmenuitemname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fmenuitemkey | 标识 | varchar | 50 |  | √ | ' ' | 标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msbd_sccomcfg_menu |  | fentryid |
| 2 | idx_msbd_sccomcfg_menu_fk |  | fid |

---

## 过滤控件配置-子表 t_msbd_sccomcfg_filter

- **表名称：** 过滤控件配置-子表
- **表名：** t_msbd_sccomcfg_filter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilterbizfieldkey | 业务字段标识 | varchar | 50 |  | √ | ' ' | 业务字段标识 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ffilterctrlkey | 控件标识 | varchar | 50 |  | √ | ' ' | 控件标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_sccomcfg_filter_fk |  | fid |
| 2 | pk_msbd_sccomcfg_filter |  | fentryid |

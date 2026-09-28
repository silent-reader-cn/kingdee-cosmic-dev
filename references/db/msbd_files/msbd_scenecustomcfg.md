# 场景工作台配置-msbd_scenecustomcfg

## 场景工作台配置-主表 t_msbd_sccustcfg

- **表名称：** 场景工作台配置-主表
- **表名：** t_msbd_sccustcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fbelongappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 13 | fisdefault | 默认配置 | bpchar | 1 |  | √ | '0' | 默认配置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msbd_sccustcfg |  | fid |
| 2 | idx_msbd_sccustcfg_m0 |  | fmasterid |

---

## 导航栏信息-多语言表 t_msbd_sccustcfg_nav_l

- **表名称：** 导航栏信息-多语言表
- **表名：** t_msbd_sccustcfg_nav_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fnavname | 名称 | varchar | 155 |  | √ | ' ' | 名称 |
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
| 1 | idx_msbd_sccustcfg_nav_l_0 |  | fentryid,flocaleid |
| 2 | pk_msbd_sccustcfg_nav_l |  | fpkid |

---

## 页签信息-多语言表 t_msbd_sccustcfg_tab_l

- **表名称：** 页签信息-多语言表
- **表名：** t_msbd_sccustcfg_tab_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftabname | 名称 | varchar | 155 |  | √ | ' ' | 名称 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_sccustcfg_tab_l_0 |  | fdetailid,flocaleid |
| 2 | pk_msbd_sccustcfg_tab_l |  | fpkid |

---

## 导航栏信息-子表 t_msbd_sccustcfg_nav

- **表名称：** 导航栏信息-子表
- **表名：** t_msbd_sccustcfg_nav

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnavisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 3 | fnavname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fnavtargetformid | 目标页面 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 6 | fnavicon | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: 1 :定位 2 :订单 3 :文档 4 :日历 5 :仓库 6 :货车 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msbd_sccustcfg_nav |  | fentryid |
| 2 | idx_msbd_sccustcfg_nav_fk |  | fid |

---

## 数据卡片-多语言表 t_msbd_sccustcfg_card_l

- **表名称：** 数据卡片-多语言表
- **表名：** t_msbd_sccustcfg_card_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fdatacardname | 名称 | varchar | 155 |  | √ | ' ' | 名称 |
| 5 | fdatacardtips | 帮助文本 | varchar | 399 |  | √ | ' ' | 帮助文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_sccustcfg_card_l_0 |  | fentryid,flocaleid |
| 2 | pk_msbd_sccustcfg_card_l |  | fpkid |

---

## 页签信息-子表 t_msbd_sccustcfg_tab

- **表名称：** 页签信息-子表
- **表名：** t_msbd_sccustcfg_tab

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftabname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 2 | ftabtargetformid | 目标页面 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | ftabisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msbd_sccustcfg_tab |  | fdetailid |
| 2 | idx_msbd_sccustcfg_tab_fk |  | fentryid |

---

## 场景工作台配置-多语言表 t_msbd_sccustcfg_l

- **表名称：** 场景工作台配置-多语言表
- **表名：** t_msbd_sccustcfg_l

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
| 1 | pk_msbd_sccustcfg_l |  | fpkid |
| 2 | idx_msbd_sccustcfg_l_0 |  | fid,flocaleid |

---

## 数据卡片-子表 t_msbd_sccustcfg_card

- **表名称：** 数据卡片-子表
- **表名：** t_msbd_sccustcfg_card

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdatacardnumcolor | 数值颜色 | varchar | 50 |  | √ | ' ' | 数值颜色,枚举: 1 :黑色 2 :红色 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdatacardbelongformid | 所属页面 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 5 | fdatacardsrc | 数据来源 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fdatacardname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 7 | fdatacardbgcolor | 背景色 | varchar | 50 |  | √ | ' ' | 背景色,枚举: 1 :蓝色 2 :黄色 3 :紫色 4 :浅蓝 5 :绿色 |
| 8 | fdatacardisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 9 | fdatacardfilter_tag | 数据过滤条件_详情 | text | 0 |  |  | null | 数据过滤条件_详情 |
| 10 | fdatacardfilter | 数据过滤条件 | varchar | 255 |  | √ | ' ' | 数据过滤条件 |
| 11 | fdatacardicon | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: 1 :蓝色1 2 :蓝色2 3 :蓝色3 4 :蓝色4 11 :黄色1 12 :黄色2 13 :黄色3 14 :黄色4 21 :紫色1 22 :紫色2 23 :紫色3 31 :绿色1 32 :绿色2 33 :绿色3 34 :绿色4 35 :绿色5 |
| 12 | fdatacardtype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 1 :过滤方案 2 :数据指标 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fdatacardtips | 帮助文本 | varchar | 255 |  | √ | ' ' | 帮助文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msbd_sccustcfg_card |  | fentryid |
| 2 | idx_msbd_sccustcfg_card_fk |  | fid |

# 流程引导图-srm_portal_comptodo

## 流程引导图-主表 t_srm_component

- **表名称：** 流程引导图-主表
- **表名：** t_srm_component

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 组件类型 | int8 | 64 |  | √ | 0 | [门户组件类型 srm_portal_compgroup](../srm_files/srm_portal_compgroup.md) |
| 3 | faddress | faddress | varchar | 200 |  | √ | ' ' |  |
| 4 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | frightbidtype | frightbidtype | varchar | 50 |  | √ | ' ' |  |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fregquerybutton | fregquerybutton | varchar | 255 |  | √ | ' ' |  |
| 9 | fregbuttonname | fregbuttonname | varchar | 255 |  | √ | ' ' |  |
| 10 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 11 | ficplink | ficplink | varchar | 255 |  | √ | ' ' |  |
| 12 | flogopicture | flogopicture | varchar | 512 |  | √ | ' ' |  |
| 13 | fisfilter | fisfilter | bpchar | 1 |  | √ | '0' |  |
| 14 | fswitchtime | fswitchtime | int8 | 64 |  | √ | 0 |  |
| 15 | ftransparency | ftransparency | int8 | 64 |  | √ | 0 |  |
| 16 | fnoticeshowtime | fnoticeshowtime | int8 | 64 |  | √ | 0 |  |
| 17 | fname | 组件名称 | varchar | 100 |  | √ | ' ' | 组件名称 |
| 18 | fphone | fphone | varchar | 50 |  | √ | ' ' |  |
| 19 | femail | femail | varchar | 100 |  | √ | ' ' |  |
| 20 | flrightpicture | flrightpicture | varchar | 512 |  | √ | ' ' |  |
| 21 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 22 | fbidtype | fbidtype | varchar | 100 |  | √ | ' ' |  |
| 23 | fnetdata | fnetdata | varchar | 512 |  | √ | ' ' |  |
| 24 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fleftbidtype | fleftbidtype | varchar | 50 |  | √ | ' ' |  |
| 26 | fnumber | 组件编码 | varchar | 80 |  | √ | ' ' | 组件编码 |
| 27 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 28 | fversiondata | fversiondata | varchar | 512 |  | √ | ' ' |  |
| 29 | frightnoticetype | frightnoticetype | varchar | 50 |  | √ | ' ' |  |
| 30 | fbotcololr | fbotcololr | varchar | 100 |  | √ | ' ' |  |
| 31 | fleftnoticetype | fleftnoticetype | varchar | 50 |  | √ | ' ' |  |
| 32 | ftopcololr | ftopcololr | varchar | 100 |  | √ | ' ' |  |
| 33 | fleftname | fleftname | varchar | 255 |  | √ | ' ' |  |
| 34 | frightname | frightname | varchar | 255 |  | √ | ' ' |  |
| 35 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 38 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 39 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fcomponentsys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fnetlink | fnetlink | varchar | 255 |  | √ | ' ' |  |
| 44 | fleftpicture | fleftpicture | varchar | 512 |  | √ | ' ' |  |
| 45 | fportalname | fportalname | varchar | 255 |  | √ | ' ' |  |
| 46 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 47 | ficpdata | ficpdata | varchar | 512 |  | √ | ' ' |  |
| 48 | floginbutton | floginbutton | varchar | 255 |  | √ | ' ' |  |
| 49 | fallthemecololr | fallthemecololr | varchar | 100 |  | √ | ' ' |  |
| 50 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 51 | fnoticetype | fnoticetype | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_component |  | fid |
| 2 | idx_t_srm_component_createorg |  | fcreateorgid |
| 3 | idx_t_srm_component_master |  | fmasterid |
| 4 | idx_srm_component_number |  | fnumber |

---

## 插图配置分录-子表 t_srm_processentry

- **表名称：** 插图配置分录-子表
- **表名：** t_srm_processentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocessname | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |
| 3 | fprocesspic | 节点图片 | varchar | 512 |  | √ | ' ' | 节点图片 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_processentry |  | fentryid |
| 2 | idx_srm_processentry_fid |  | fid |

---

## 流程引导图-多语言表 t_srm_component_l

- **表名称：** 流程引导图-多语言表
- **表名：** t_srm_component_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 组件名称 | varchar | 100 |  | √ | ' ' | 组件名称 |
| 3 | faddress | faddress | varchar | 200 |  | √ | ' ' |  |
| 4 | fleftname | fleftname | varchar | 255 |  | √ | ' ' |  |
| 5 | frightname | frightname | varchar | 255 |  | √ | ' ' |  |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 8 | fportalname | fportalname | varchar | 255 |  | √ | ' ' |  |
| 9 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 10 | fnetdata | fnetdata | varchar | 512 |  | √ | ' ' |  |
| 11 | fregquerybutton | fregquerybutton | varchar | 255 |  | √ | ' ' |  |
| 12 | ficpdata | ficpdata | varchar | 512 |  | √ | ' ' |  |
| 13 | fregbuttonname | fregbuttonname | varchar | 255 |  | √ | ' ' |  |
| 14 | floginbutton | floginbutton | varchar | 255 |  | √ | ' ' |  |
| 15 | fversiondata | fversiondata | varchar | 512 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_component_l |  | fpkid |
| 2 | idx_srmcomponent_l_fid |  | fid |

---

## 流程引导图-使用范围表 t_srm_component_u

- **表名称：** 流程引导图-使用范围表
- **表名：** t_srm_component_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_component_u |  | fdataid,fuseorgid |
| 2 | idx_t_srm_component_u_uo |  | fuseorgid |

---

## 插图配置分录-多语言表 t_srm_processentry_l

- **表名称：** 插图配置分录-多语言表
- **表名：** t_srm_processentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprocessname | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |
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
| 1 | pk_t_srm_processentry_l |  | fpkid |
| 2 | idx_srm_processentry_l_fenid |  | fentryid |

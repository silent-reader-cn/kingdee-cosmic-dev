# 会议模块配置(废弃)-sfc_meetmodconfig

## 单据体-子表 t_sfc_meetmodconfigentry

- **表名称：** 单据体-子表
- **表名：** t_sfc_meetmodconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fchilditem | 子项 | varchar | 50 |  | √ | ' ' | 子项 |
| 4 | fdatasrc | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconf_sfc |
| 5 | fdescription | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_meetmodconfigentry |  | fentryid |
| 2 | idx_sfc_meetmodconfigentry_fk |  | fid |

---

## 会议模块配置(废弃)-主表 t_sfc_meetmodconfig

- **表名称：** 会议模块配置(废弃)-主表
- **表名：** t_sfc_meetmodconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fismeetcontent | 是否会议内容 | bpchar | 1 |  | √ | '0' | 是否会议内容 |
| 5 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fsortcode | 排序码 | int8 | 64 |  | √ | 0 | 排序码 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fispreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fmatchitem | 匹配维度 | varchar | 50 |  | √ | ' ' | 匹配维度,枚举: XM :项目 KH :客户 HY :行业 JXSBNO :检修设备注册号 XHL1 :型号L1 XHLIMPD :型号L1-MPD XHL2 :型号L2 XHL3 :型号L3 HYFQBM :会议发起部门 |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fisallowedmodify | 是否允许手工修改 | bpchar | 1 |  | √ | '0' | 是否允许手工修改 |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fresource | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconf_sfc |
| 24 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_meetmodconfig |  | fid |
| 2 | idx_t_sfc_meetmodconfig_master |  | fmasterid |
| 3 | idx_sfc_meetmod_createorg |  | fcreateorgid |
| 4 | idx_sfc_meetmod_number |  | fnumber |
| 5 | idx_t_sfc_meetmodconfig_createorg |  | fcreateorgid |
| 6 | idx_sfc_meetmod_master |  | fmasterid |

---

## 会议模块配置(废弃)-多语言表 t_sfc_meetmodconfig_l

- **表名称：** 会议模块配置(废弃)-多语言表
- **表名：** t_sfc_meetmodconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_meetmodconfig_l |  | fpkid |
| 2 | idx_sfc_meetmodconfig_l_0 |  | fid,flocaleid |

---

## 会议模块配置(废弃)-使用范围表 t_sfc_meetmodconfig_u

- **表名称：** 会议模块配置(废弃)-使用范围表
- **表名：** t_sfc_meetmodconfig_u

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
| 1 | pk_t_sfc_meetmodconfig_u |  | fdataid,fuseorgid |
| 2 | idx_t_sfc_meetmodconfig_u_uo |  | fuseorgid |

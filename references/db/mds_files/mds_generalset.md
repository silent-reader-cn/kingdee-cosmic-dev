# 通用备货方案-mds_generalset

## 通用备货方案-主表 t_mds_generalset

- **表名称：** 通用备货方案-主表
- **表名：** t_mds_generalset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcusandactype | 客户+检修设备类型 | bpchar | 1 |  | √ | '0' | 客户+检修设备类型 |
| 3 | fcustomercount | 客户≥ | int8 | 64 |  | √ | 0 | 客户≥ |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fusecountmax | 到 | int8 | 64 |  | √ | 0 | 到 |
| 6 | fspecialreq | 启用特殊备货需求 | bpchar | 1 |  | √ | '0' | 启用特殊备货需求 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | factypecount | 检修设备类型≥ | int8 | 64 |  | √ | 0 | 检修设备类型≥ |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fplanid | 任务号 | varchar | 50 |  | √ | ' ' | 任务号 |
| 11 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fusecountmin | 使用频率 | int8 | 64 |  | √ | 0 | 使用频率 |
| 17 | fisall | 全选 | bpchar | 1 |  | √ | '0' | 全选 |
| 18 | fsetval | 设置数据 | varchar | 2000 |  | √ | ' ' | 设置数据 |
| 19 | fgeneralplan | 通用备货计划 | int8 | 64 |  | √ | 0 | 取数方案定义 mds_datafetchset |
| 20 | frepeatcal | 重运算 | bpchar | 1 |  | √ | '0' | 重运算 |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fcustomer | 客户 | bpchar | 1 |  | √ | '0' | 客户 |
| 25 | fchecktypecount | 检修级别≥ | int8 | 64 |  | √ | 0 | 检修级别≥ |
| 26 | fhisuseset | 历史用量运算方案 | int8 | 64 |  | √ | 0 | 历史用量运算方案定义 mds_hisuseset |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fjobid | 作业号 | varchar | 50 |  | √ | ' ' | 作业号 |
| 29 | factype | 检修设备类型 | bpchar | 1 |  | √ | '0' | 检修设备类型 |
| 30 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | fissys | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 32 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 34 | fspecialcond | 特定条件 | bpchar | 1 |  | √ | '0' | 特定条件 |
| 35 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mds_generalset_master |  | fmasterid |
| 2 | idx_mds_generalset_number |  | fnumber |
| 3 | pk_mds_generalset |  | fid |
| 4 | idx_t_mds_generalset_createorg |  | fcreateorgid |

---

## 通用备货方案-使用范围表 t_mds_generalset_u

- **表名称：** 通用备货方案-使用范围表
- **表名：** t_mds_generalset_u

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
| 1 | pk_t_mds_generalset_u |  | fdataid,fuseorgid |
| 2 | idx_t_mds_generalset_u_uo |  | fuseorgid |

---

## 通用备货方案-多语言表 t_mds_generalset_l

- **表名称：** 通用备货方案-多语言表
- **表名：** t_mds_generalset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_generalset_l_id |  | fid,flocaleid |
| 2 | pk_mds_generalset_l |  | fpkid |

---

## 物料分类-多选基础资料表 t_mds_generalset_group

- **表名称：** 物料分类-多选基础资料表
- **表名：** t_mds_generalset_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_generalset_group_id |  | fid |
| 2 | pk_mds_generalset_group |  | fpkid |

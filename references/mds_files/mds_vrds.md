# 版本定义-mds_vrds

## 版本定义-多语言表 t_mds_vrds_l

- **表名称：** 版本定义-多语言表
- **表名：** t_mds_vrds_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 版本名称 | varchar | 100 |  | √ | ' ' | 版本名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mds_vrds_l_pkey |  | fpkid |
| 2 | idx_mds_vrds_l |  | fid,flocaleid |

---

## 版本定义-使用范围位图表 t_mds_vrds_m

- **表名称：** 版本定义-使用范围位图表
- **表名：** t_mds_vrds_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_vrds_m |  | forgid |

---

## 版本定义-使用范围表 t_mds_vrds_u

- **表名称：** 版本定义-使用范围表
- **表名：** t_mds_vrds_u

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
| 1 | idx_t_mds_vrds_u_uo |  | fuseorgid |
| 2 | t_mds_vrds_u_pkey |  | fdataid,fuseorgid |

---

## 版本定义-主表 t_mds_vrds

- **表名称：** 版本定义-主表
- **表名：** t_mds_vrds

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 版本定义分组 | int8 | 64 |  | √ | 0 | 版本定义分组 mds_vrdsgroup |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | finputcontrol | 录入控制 | varchar | 30 |  | √ | ' ' | 录入控制,枚举: material :物料 material_org :物料-供应组织 no :不控制 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fauditordate | fauditordate | timestamp | 0 |  |  | null |  |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fvertype | 版本类型 | varchar | 30 |  | √ | ' ' | 版本类型,枚举: 0 :预测 1 :需求计划 2 :日生产计划 |
| 14 | fcytype | 周期类型 | varchar | 30 |  | √ | ' ' | 周期类型,枚举: 0 :日 1 :周 2 :自定义周期 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fdayofweek | 时间点 | varchar | 5 |  | √ | 'Mon' | 时间点,枚举: Mon :星期一 Tue :星期二 Wed :星期三 Thu :星期四 Fri :星期五 Sat :星期六 Sun :星期天 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fplandm | 计划维度 | varchar | 30 |  | √ | ' ' | 计划维度,枚举: 0 :物料编码 1 :物料编码-客户 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fperiods | 期数 | int8 | 64 |  | √ | 0 | 期数 |
| 22 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 版本编码 | varchar | 30 |  | √ | ' ' | 版本编码 |
| 24 | flosedate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 25 | fdefaultorg | 默认供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 27 | fdtype | 需求类型 | int8 | 64 |  | √ | 0 | 需求类型 mds_dmtp |
| 28 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_vrds_fnumber |  | fnumber,fcreateorgid |
| 2 | idx_t_mds_vrds_master |  | fmasterid |
| 3 | idx_t_mds_vrds_createorg |  | fcreateorgid |
| 4 | t_mds_vrds_pkey |  | fid |

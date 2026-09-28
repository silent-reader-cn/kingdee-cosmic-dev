# 星空制造基础资料带组织模板-mpdm_mergecycle

## 星空制造基础资料带组织模板-使用范围表 t_mpdm_mergecycle_u

- **表名称：** 星空制造基础资料带组织模板-使用范围表
- **表名：** t_mpdm_mergecycle_u

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
| 1 | idx_t_mpdm_mergecycle_u_uo |  | fuseorgid |
| 2 | t_mpdm_mergecycle_u_pkey |  | fdataid,fuseorgid |

---

## 星空制造基础资料带组织模板-多语言表 t_mpdm_mergecycle_l

- **表名称：** 星空制造基础资料带组织模板-多语言表
- **表名：** t_mpdm_mergecycle_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_mergecycle_l |  | fid,flocaleid |
| 2 | t_mpdm_mergecycle_l_pkey |  | fpkid |

---

## 星空制造基础资料带组织模板-使用范围位图表 t_mpdm_mergecycle_m

- **表名称：** 星空制造基础资料带组织模板-使用范围位图表
- **表名：** t_mpdm_mergecycle_m

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
| 1 | pk_t_mpdm_mergecycle_m |  | forgid |

---

## 单据体-子表 t_mpdm_mergecycleentry

- **表名称：** 单据体-子表
- **表名：** t_mpdm_mergecycleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymergedate | 区间合并日期 | timestamp | 0 |  |  | null | 区间合并日期 |
| 3 | fentryenddate | 区间结束日期 | timestamp | 0 |  |  | null | 区间结束日期 |
| 4 | fentrystartdate | 区间开始日期 | timestamp | 0 |  |  | null | 区间开始日期 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_mergecycleentry_pkey |  | fentryid |
| 2 | idx_mpdm_mergecycleentry |  | fid,fseq |

---

## 星空制造基础资料带组织模板-主表 t_mpdm_mergecycle

- **表名称：** 星空制造基础资料带组织模板-主表
- **表名：** t_mpdm_mergecycle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcycleunit | 周期单位 | varchar | 30 |  | √ | ' ' | 周期单位,枚举: A :天 B :月 C :年 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 15 | fmergedatetype | 合并日期类型 | varchar | 30 |  | √ | ' ' | 合并日期类型,枚举: A :固定日期 B :周期最早 C :周期最晚 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | foffsetdays | 区间合并偏移天数 | int8 | 64 |  | √ | 0 | 区间合并偏移天数 |
| 21 | fcyclenum | 周期 | int8 | 64 |  | √ | 0 | 周期 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_mergecycle |  | fnumber,fcreateorgid |
| 2 | idx_t_mpdm_mergecycle_createorg |  | fcreateorgid |
| 3 | idx_t_mpdm_mergecycle_master |  | fmasterid |
| 4 | t_mpdm_mergecycle_pkey |  | fid |

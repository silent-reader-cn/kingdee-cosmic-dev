# 经营组织架构版本-xkoac_orgsystem

## 经营组织架构版本-多语言表 t_xkoac_orgsystem_l

- **表名称：** 经营组织架构版本-多语言表
- **表名：** t_xkoac_orgsystem_l

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
| 1 | pk_t_xkoac_orgsystem_l |  | fpkid |
| 2 | idx_xkoac_orgsystem_l |  | fid,flocaleid |

---

## 经营组织架构单据体-子表 t_xkoac_orgsystementry

- **表名称：** 经营组织架构单据体-子表
- **表名：** t_xkoac_orgsystementry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartupstatus | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 3 | fambunit | 经营单元名称 | int8 | 64 |  | √ | 0 | 经营单元 xkoac_unit |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 6 | fambforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 7 | flastlevel | 是否底层 | bpchar | 1 |  | √ | '1' | 是否底层,枚举: 1 :是 0 :否 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_orgsystementry |  | fid |
| 2 | pk_t_xkoac_orgsystementry |  | fentryid |

---

## 经营组织架构版本-主表 t_xkoac_orgsystem

- **表名称：** 经营组织架构版本-主表
- **表名：** t_xkoac_orgsystem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fendperiod | 失效期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fgroupid | 经营组织架构 | int8 | 64 |  | √ | 0 | 经营组织架构 xkoac_orgsystemgroup |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fstartperiod | 生效期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fversionnumber | 版本号 | varchar | 100 |  | √ | ' ' | 版本号 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fperiodtype | 经营会计日历 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 17 | fversionflag | 版本标识 | int4 | 32 |  | √ | 0 | 版本标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_orgsystem |  | fid |
| 2 | idx_xkoac_orgsystem |  | fversionnumber |

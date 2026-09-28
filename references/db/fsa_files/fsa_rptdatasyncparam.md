# 同步参数-fsa_rptdatasyncparam

## 同步参数-多语言表 t_fsa_rptdatasyncparam_l

- **表名称：** 同步参数-多语言表
- **表名：** t_fsa_rptdatasyncparam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 同步参数名称 | varchar | 100 |  | √ | ' ' | 同步参数名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_syncpa_l |  | fid |
| 2 | pk_t_fsa_rptdatasyncparam_l |  | fpkid |

---

## 同步参数-主表 t_fsa_rptdatasyncparam

- **表名称：** 同步参数-主表
- **表名：** t_fsa_rptdatasyncparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmappingsrctype | 取数来源 | bpchar | 1 |  | √ | ' ' | 取数来源,枚举: 0 :苍穹总账 1 :苍穹合并报表 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | facctperiodtype | 期间类型 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 同步参数编码 | varchar | 30 |  | √ | ' ' | 同步参数编码 |
| 11 | frpttype | 源报表类型 | bpchar | 1 |  | √ | ' ' | 源报表类型,枚举: 0 :资产负债表 1 :利润表 2 :现金流量表 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_syncpa_maprpt |  | fmappingsrctype,frpttype |
| 2 | pk_t_fsa_rptdatasyncparam |  | fid |
| 3 | idx_syncpa_numacc |  | fnumber,facctperiodtype |

---

## 同步参数分录-子表 t_fsa_rptdatasyncparament

- **表名称：** 同步参数分录-子表
- **表名：** t_fsa_rptdatasyncparament

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctorgview | 统计视图 | int8 | 64 |  | √ | 0 | 新增视图 bd_accountingsysviewsch |
| 3 | frptmapping | 映射报表名称 | int8 | 64 |  | √ | 0 | 映射报表 fsa_rptmappings |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_rptdatasyncparament |  | fentryid |
| 2 | idx_syncpa_ent_id |  | fid |
| 3 | idx_syncpa_ent_1 |  | facctorgview |

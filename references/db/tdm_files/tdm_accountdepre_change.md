# 资产变更记录-tdm_accountdepre_change

## 单据体-子表 t_tdm_acctdeprechange_e

- **表名称：** 单据体-子表
- **表名：** t_tdm_acctdeprechange_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangefieldname | 变更字段 | varchar | 50 |  | √ | ' ' | 变更字段 |
| 3 | foldvalue | 变更前 | varchar | 255 |  | √ | ' ' | 变更前 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fchangefield | 变更字段标识 | varchar | 50 |  | √ | ' ' | 变更字段标识 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fnewvalue | 变更后 | varchar | 255 |  | √ | ' ' | 变更后 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_acctdeprechange_e |  | fentryid |
| 2 | idx_tdm_acctdeprechange_e_fk |  | fid |

---

## 资产变更记录-主表 t_tdm_acctdeprechange

- **表名称：** 资产变更记录-主表
- **表名：** t_tdm_acctdeprechange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountdepreid | 本期会计折旧id | int8 | 64 |  | √ | 0 | 本期会计折旧id |
| 3 | fassetname | 资产名称 | varchar | 50 |  | √ | ' ' | 资产名称 |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fassetcode | 资产编码 | varchar | 50 |  | √ | ' ' | 资产编码 |
| 6 | faccountingperiod | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 7 | fpreaccountdepreid | 上期会计折旧id | int8 | 64 |  | √ | 0 | 上期会计折旧id |
| 8 | forg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_acctdeprechange |  | fid |
| 2 | idx_kjzjbg_02 |  | faccountingperiod,forg,fassetcode |
| 3 | idx_kjzjbg_01 |  | faccountdepreid |

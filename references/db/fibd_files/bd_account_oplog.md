# 会计科目操作日志-bd_account_oplog

## 单据体-子表 t_bd_accountoplogentry

- **表名称：** 单据体-子表
- **表名：** t_bd_accountoplogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 3 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 4 | ffullname | 科目.名称 | varchar | 255 |  | √ | ' ' | 科目.名称 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | foptype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fnumber | 科目.编码 | varchar | 30 |  | √ | ' ' | 科目.编码 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | flog | 日志 | varchar | 1000 |  |  | ' ' | 日志 |
| 11 | faccountid | 科目 | varchar | 50 |  | √ | ' ' | 科目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_accountoplogentry |  | fentryid |
| 2 | idx_bd_accountoplogentry_fid |  | fid |

---

## 组织-多选基础资料表 t_bd_accoplogorg

- **表名称：** 组织-多选基础资料表
- **表名：** t_bd_accoplogorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_accoplogorg |  | fpkid |
| 2 | idx_bd_accoplogorg_fid |  | fid |

---

## 会计科目操作日志-主表 t_bd_accountoplog

- **表名称：** 会计科目操作日志-主表
- **表名：** t_bd_accountoplog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foptime | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 3 | foplog | 日志 | varchar | 1000 |  |  | ' ' | 日志 |
| 4 | foporgid | 操作组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | foldaccount | 源科目 | text | 0 |  |  | null | 源科目 |
| 6 | fopaccountids | 科目 | text | 0 |  |  | null | 科目 |
| 7 | fopuserid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | foptype | 操作类型 | varchar | 32 |  | √ | ' ' | 操作类型 |
| 9 | frequestid | requestid | varchar | 32 |  | √ | ' ' | requestid |
| 10 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 11 | fnewaccount | 新科目 | text | 0 |  |  | null | 新科目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_accountoplog_foptime |  | foptime |
| 2 | pk_t_bd_accountoplog |  | fid |
| 3 | idx_bd_accountoplog_forgdate |  | foporgid,foptime |
| 4 | idx_bd_accountoplog_frequestid |  | frequestid |

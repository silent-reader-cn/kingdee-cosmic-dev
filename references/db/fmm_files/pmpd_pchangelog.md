# 项目变更日志-pmpd_pchangelog

## 单据体-子表 t_fmm_pchangelog_entry

- **表名称：** 单据体-子表
- **表名：** t_fmm_pchangelog_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangebefore | 变更前 | varchar | 50 |  | √ | ' ' | 变更前 |
| 3 | fchangeafter | 变更后 | varchar | 50 |  | √ | ' ' | 变更后 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpfield | 项目字段 | varchar | 50 |  | √ | ' ' | 项目字段 |
| 6 | fentryseq | 分录行 | int8 | 64 |  | √ | 0 | 分录行 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_pcglog_entry_fseq |  | fseq |
| 2 | pk_fmm_pchangelog_entry |  | fentryid |
| 3 | idx_fmm_pcglog_entry_fid |  | fid |

---

## 项目变更日志-主表 t_fmm_pchangelog

- **表名称：** 项目变更日志-主表
- **表名：** t_fmm_pchangelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 5 | freason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 6 | fpcnumber | 变更单单据编码 | varchar | 30 |  | √ | ' ' | 变更单单据编码 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fchangeperid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fstatus | 变更状态 | varchar | 30 |  | √ | ' ' | 变更状态,枚举: A :变更中 B :变更完成 |
| 10 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 11 | fpnumber | 项目编号 | varchar | 30 |  | √ | ' ' | 项目编号 |
| 12 | fpname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_pchangelog_fpnumber |  | fpnumber |
| 2 | pk_fmm_pchangelog |  | fid |

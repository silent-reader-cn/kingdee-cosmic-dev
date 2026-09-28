# 银行对账单导入日志-cas_bankstatement_imlog

## 单据体-子表 t_cas_bankstatementlog_e

- **表名称：** 单据体-子表
- **表名：** t_cas_bankstatementlog_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fbankstatementid | 对账单内码 | int8 | 64 |  | √ | 0 | 对账单内码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cas_bankstatementlog_fid |  | fid |
| 2 | pk_cas_bankstatementlog_e |  | fentryid |

---

## 银行对账单导入日志-主表 t_cas_bankstatement_imlog

- **表名称：** 银行对账单导入日志-主表
- **表名：** t_cas_bankstatement_imlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fbatchno | 源文件编码 | varchar | 150 |  | √ | ' ' | 源文件编码 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fenddatetime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fimportresult | 导入状态 | varchar | 50 |  | √ | ' ' | 导入状态,枚举: 1 :成功 2 :失败 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbegindatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | ffilename | 文件名 | varchar | 150 |  | √ | ' ' | 文件名 |
| 14 | fcount | 流水笔数 | int8 | 64 |  | √ | 0 | 流水笔数 |
| 15 | fbillno | 日志编码 | varchar | 80 |  | √ | ' ' | 日志编码 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fimportdetail | 导入结果详情 | varchar | 500 |  | √ | ' ' | 导入结果详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bstate_imlog_createtime |  | fcreatetime |
| 2 | pk_cas_bankstatement_imlog |  | fid |

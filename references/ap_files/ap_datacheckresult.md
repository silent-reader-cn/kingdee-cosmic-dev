# 数据巡查结果-ap_datacheckresult

## 单据体-子表 t_ap_checkresultentry

- **表名称：** 单据体-子表
- **表名：** t_ap_checkresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 3 | fbillcount | 巡查条数 | int4 | 32 |  | √ | 0 | 巡查条数 |
| 4 | fexception_tag | 执行异常信息_详情 | text | 0 |  |  | null | 执行异常信息_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcheckitemid | 巡查项 | int8 | 64 |  | √ | 0 | 数据巡查项 ap_datacheck_item |
| 7 | fexecbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fexecstatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 1 :执行完成 2 :执行中 3 :待执行 4 :执行失败 |
| 9 | fexecendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fcheckresult | 巡查结果 | varchar | 30 |  | √ | ' ' | 巡查结果,枚举: normal :正常 abnormal :异常 |
| 11 | ferrorcount | 异常条数 | int4 | 32 |  | √ | 0 | 异常条数 |
| 12 | fexception | 执行异常信息 | varchar | 255 |  | √ | ' ' | 执行异常信息 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcost | 耗时(s) | numeric | 23 | 10 | √ | 0 | 耗时(s) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_checkentry_fid |  | fid |
| 2 | idx_ap_checkentry_traceid |  | ftraceid |
| 3 | pk_t_ap_checkresultentry |  | fentryid |

---

## 子单据体-子表 t_ap_checkresultsubentry

- **表名称：** 子单据体-子表
- **表名：** t_ap_checkresultsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ferrormsg | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 2 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_checksub_billno |  | fbillno |
| 2 | pk_t_ap_checkresultsubentry |  | fdetailid |
| 3 | idx_ap_checksub_entryid |  | fentryid |

---

## 数据巡查结果-主表 t_ap_checkresult

- **表名称：** 数据巡查结果-主表
- **表名：** t_ap_checkresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 4 | fbizenddate | 巡查日期范围.结束 | timestamp | 0 |  |  | null | 巡查日期范围.结束 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 应付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcheckendtime | 巡查结束时间 | timestamp | 0 |  |  | null | 巡查结束时间 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbizbegindate | 巡查日期范围.开始 | timestamp | 0 |  |  | null | 巡查日期范围.开始 |
| 12 | fexecstatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 1 :执行完成 2 :执行中 3 :待执行 4 :执行失败 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcheckresult | 巡查结果 | varchar | 30 |  | √ | ' ' | 巡查结果,枚举: normal :正常 abnormal :异常 |
| 15 | fcheckbegintime | 巡查开始时间 | timestamp | 0 |  |  | null | 巡查开始时间 |
| 16 | fcheckdate | 巡查日期 | timestamp | 0 |  |  | null | 巡查日期 |
| 17 | fbizobj | 巡查对象 | varchar | 30 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 18 | fbillno | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_checkresult_traceid |  | ftraceid |
| 2 | pk_t_ap_checkresult |  | fid |
| 3 | idx_ap_checkresult_billno |  | fbillno |
| 4 | idx_ap_checkresult_dateorg |  | fcheckdate,forgid |

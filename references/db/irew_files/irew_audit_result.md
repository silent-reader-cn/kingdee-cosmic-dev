# 发票预警结果-irew_audit_result

## 发票预警结果-主表 t_irew_audit_result

- **表名称：** 发票预警结果-主表
- **表名：** t_irew_audit_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcustomize_engine | 自定义引擎 | int8 | 64 |  | √ | 0 | 发票校验引擎 irew_engine |
| 3 | fcheck_type | fcheck_type | varchar | 8 |  | √ | ' ' |  |
| 4 | fverify_basis | fverify_basis | varchar | 200 |  | √ | ' ' |  |
| 5 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 6 | fserial_no | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fhandle_status | 异常处理状态 | varchar | 50 |  | √ | ' ' | 异常处理状态,枚举: 0 :未处理 1 :已处理 |
| 9 | fhelp_info | fhelp_info | varchar | 200 |  | √ | ' ' |  |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fhandle_explain | 异常处理说明 | varchar | 400 |  | √ | ' ' | 异常处理说明 |
| 12 | forg_id | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | ftotal_amount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 15 | fbillstatus | 单据状态 | varchar | 4 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 发票审计时间 | timestamp | 0 |  |  | null | 发票审计时间 |
| 17 | ftotal_tax_amount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 18 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fwarning_scheme | 预警方案 | int8 | 64 |  | √ | 0 | 发票预警方案 irew_scheme |
| 21 | fsaler_name | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 22 | fhandle_count | 异常批注次数 | int4 | 32 |  | √ | 0 | 异常批注次数 |
| 23 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 24 | fverify_level | 风险等级 | varchar | 4 |  | √ | ' ' | 风险等级,枚举: 0 :高风险 1 :中风险 2 :低风险 |
| 25 | fauditorid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_irew_audit_result |  | fid |
| 2 | idx_irew_audit_result |  | fwarning_scheme,fcustomize_engine,fserial_no |

---

## 单据体-子表 t_irew_audit_result_item

- **表名称：** 单据体-子表
- **表名：** t_irew_audit_result_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhandle_time | 异常处理时间 | timestamp | 0 |  |  | null | 异常处理时间 |
| 3 | fcomment | 异常处理说明 | varchar | 400 |  | √ | ' ' | 异常处理说明 |
| 4 | fhandler | 异常处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_irew_audit_result_item |  | fid |
| 2 | pk_irew_audit_result_item |  | fentryid |

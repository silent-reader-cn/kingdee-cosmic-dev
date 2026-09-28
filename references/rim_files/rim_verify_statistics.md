# 合规性校验统计-rim_verify_statistics

## 合规性校验统计-主表 t_rim_verify_statistic

- **表名称：** 合规性校验统计-主表
- **表名：** t_rim_verify_statistic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forg_id | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftotal_amount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 4 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 8 | fcompliance | 是否合规 | varchar | 2 |  | √ | ' ' | 是否合规,枚举: 0 :不合规 1 :合规 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_verify_statistic |  | fid |
| 2 | idx_rim_verify_statistic |  | fcreatetime |

---

## 单据体-子表 t_rim_verify_detail

- **表名称：** 单据体-子表
- **表名：** t_rim_verify_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | frisk_grade | 风险等级 | varchar | 50 |  | √ | ' ' | 风险等级,枚举: 1 :低 2 :中 3 :高 |
| 4 | fverify_description | 描述 | varchar | 50 |  | √ | ' ' | 描述,枚举: check_status :增值税普票、增值税专用发票、增值税卷票、机动车销售统一发票或二手车发票未查验 original_state :电子发票缺少原件 red_invoice :采集已红冲的发票 invalid_invoice :采集已作废的发票 continuous_no :存在串号的发票 company_seal :发票缺少专用章 repeat_expense :同一发票多次报销 person_invoice :发票抬头为个人 buyer_name :增值税发票购方抬头与企业抬头不一致 buyer_tax_no :增值税发票购方税号与企业税号不一致 deadline_date :超过企业设置的报销期限 sequence_no :发票与企业已采集的其他发票连号 modify_invoice :采集人手工修改发票信息 tax_black :发票销方为税局公布的涉税黑名单主体 black_list :发票销方为企业设置的黑名单主体 custom_config :企业自定义配置的其他校验项 expense_next_year :跨年报销 sensitive_word :发票明细包含企业设定的敏感词 next_year_month :超过企业设置的报销跨年期限 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fverify_name | 名称 | varchar | 50 |  | √ | ' ' | 名称,枚举: check_status :增值税发票查验 original_state :电子发票源文件校验 red_invoice :发票红冲校验 invalid_invoice :发票作废校验 continuous_no :发票串号校验 company_seal :发票专用章校验 repeat_expense :发票重复报销校验 person_invoice :个人抬头发票 buyer_name :增值税发票购方抬头校验 buyer_tax_no :增值税发票购方税号校验 deadline_date :超过企业设置的报销期限 sequence_no :发票连号校验 modify_invoice :发票信息手工修改校验 tax_black :涉税黑名单校验 black_list :自定义黑名单 custom_config :自定义校验项 expense_next_year :跨年报销 sensitive_word :发票敏感词校验 next_year_month :超过企业设置的报销跨年期限 buyer_name_and_tax_no :增值税发票购方多抬头税号校验 tax_blacklist :税务黑名单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_verify_detail |  | fid |
| 2 | pk_rim_verify_detail |  | fentryid |

# 智能单据体记录-er_intel_agent_record

## 智能单据体记录-主表 t_er_intel_agent_record

- **表名称：** 智能单据体记录-主表
- **表名：** t_er_intel_agent_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fsessionid | sessionid | varchar | 255 |  | √ | ' ' | sessionid |
| 4 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 5 | fextra_info_tag | 自定义信息_详情 | text | 0 |  |  | null | 自定义信息_详情 |
| 6 | fbilltype | 单据类型 | varchar | 100 |  | √ | ' ' | 单据类型,枚举: er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 er_tripreimbursebill :差旅报销单 er_checkingpaybill :商旅付款申请单 er_dailyloanbill :借款单 er_dailyapplybill :费用申请单 er_prepaybill :预付单 er_applyprojectbill :立项单 er_costestimatebill :暂估单 er_withholdingbill :费用预提单 er_contractbill :合同台账单 er_tripreqbill :出差申请单 er_dailyvehiclebill :用车申请单 er_applypaybill :挂账付款申请单 er_expensesharebill :费用分摊单 er_repaymentbill :还款单 |
| 7 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 8 | fextra_info | 自定义信息 | varchar | 255 |  | √ | ' ' | 自定义信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_intel_agent_record |  | fbillid |
| 2 | pk_er_intel_agent_record |  | fid |

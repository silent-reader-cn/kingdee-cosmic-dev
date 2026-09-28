# 发票集成日志-er_invoiceasynclog

## 发票集成日志-主表 t_er_invoiceasynclog

- **表名称：** 发票集成日志-主表
- **表名：** t_er_invoiceasynclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparam | 请求参数 | varchar | 50 |  | √ | ' ' | 请求参数 |
| 3 | freqtime | 请求时间 | timestamp | 0 |  |  | null | 请求时间 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbilloperid | 单据操作 | int8 | 64 |  | √ | 0 | [操作配置 er_operation](../em_files/er_operation.md) |
| 6 | freqstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :失败 1 :成功 |
| 7 | ficpid | 发票云服务商 | int8 | 64 |  | √ | 0 | [发票云服务商 er_invoicecloudprovider](../em_files/er_invoicecloudprovider.md) |
| 8 | fisworkflow | 工作流调用 | bpchar | 1 |  | √ | '0' | 工作流调用 |
| 9 | fxhtraceid | 星瀚traceid | varchar | 36 |  | √ | ' ' | 星瀚traceid |
| 10 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 11 | fbizobjid | 业务对象 | varchar | 36 |  | √ | ' ' | 业务对象,枚举: er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 er_tripreimbursebill :差旅报销单 er_checkingpaybill :商旅付款申请单 er_dailyloanbill :借款单 er_dailyapplybill :费用申请单 er_prepaybill :预付单 er_applyprojectbill :立项单 er_costestimatebill :暂估单 er_withholdingbill :费用预提单 er_contractbill :合同台账单 er_tripreqbill :出差申请单 er_dailyvehiclebill :用车申请单 er_applypaybill :挂账付款申请单 er_expensesharebill :费用分摊单 er_repaymentbill :还款单 |
| 12 | fresponse | 发票云返回信息 | varchar | 255 |  | √ | ' ' | 发票云返回信息 |
| 13 | fparam_tag | 请求参数_详情 | text | 0 |  |  | null | 请求参数_详情 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | finvoicecloudoper | 发票云调用类型 | varchar | 10 |  | √ | ' ' | 发票云调用类型,枚举: update :更新状态 delete :删除关联 validate :发票查验 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invlog_time |  | freqtime |
| 2 | idx_er_invlog_bizobj |  | fbizobjid |
| 3 | idx_er_invlog_status |  | freqstatus |
| 4 | pk_t_er_invoiceasynclog |  | fid |
| 5 | idx_er_invlog_billoper |  | fbilloperid |
| 6 | idx_er_invlog_org |  | forgid |

# 跨区域涉税报告合同信息-tcvat_base_contract_info

## 跨区域涉税报告合同信息-主表 t_tcvat_contract_info

- **表名称：** 跨区域涉税报告合同信息-主表
- **表名：** t_tcvat_contract_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpartnername | 合同相对方名称 | varchar | 50 |  | √ | ' ' | 合同相对方名称 |
| 3 | fpartnertaxno | 合同相对方税号 | varchar | 50 |  | √ | ' ' | 合同相对方税号 |
| 4 | ftotalamount | 累计报验金额 | numeric | 23 | 10 | √ | 0 | 累计报验金额 |
| 5 | fsigndate | 合同签订时间 | timestamp | 0 |  |  | null | 合同签订时间 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fcontractname | 合同名称 | varchar | 200 |  | √ | ' ' | 合同名称 |
| 8 | famount | 合同签订金额（元） | numeric | 23 | 10 | √ | 0.0000000000 | 合同签订金额（元） |
| 9 | fplanend | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcontractno | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 12 | fplanstart | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_contract_info |  | fentryid |
| 2 | idx_tcvat_contract_info_fk |  | fid |

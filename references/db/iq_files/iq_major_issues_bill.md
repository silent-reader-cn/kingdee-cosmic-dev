# 重大事项单据-iq_major_issues_bill

## 重大事项单据-主表 t_iq_major_issues

- **表名称：** 重大事项单据-主表
- **表名：** t_iq_major_issues

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fmajorarbitrate | 不存在重大仲裁 | bpchar | 1 |  | √ | '0' | 不存在重大仲裁 |
| 4 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fmajorbusy | 不存在重大或有事项 | bpchar | 1 |  | √ | '0' | 不存在重大或有事项 |
| 7 | fmajorcase | 不存在重大诉讼 | bpchar | 1 |  | √ | '0' | 不存在重大诉讼 |
| 8 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fmajorrisk | 不存在重大偿债风险 | bpchar | 1 |  | √ | '0' | 不存在重大偿债风险 |
| 11 | fmajorassure | 不存在重大担保 | bpchar | 1 |  | √ | '0' | 不存在重大担保 |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fdetailid | 原子指标 | int8 | 64 |  | √ | 0 | 智测测评明细 iq_intelligence_detail |
| 14 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 15 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_major_issues_bill_no |  | fbillno |
| 2 | pk_iq_major_issues |  | fid |

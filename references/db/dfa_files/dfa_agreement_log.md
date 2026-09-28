# 协议签署记录-dfa_agreement_log

## 协议签署记录-主表 t_dfa_agreementlog

- **表名称：** 协议签署记录-主表
- **表名：** t_dfa_agreementlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsigntime | 签署时间 | timestamp | 0 |  |  | null | 签署时间 |
| 3 | fsignstatus | 签署状态 | varchar | 50 |  | √ | ' ' | 签署状态,枚举: 0 :解除 1 :签署 |
| 4 | fagreement | 协议 | varchar | 50 |  | √ | ' ' | 协议 |
| 5 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 6 | ftelephonefield | 手机号码 | varchar | 1024 |  | √ | ' ' | 手机号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_agreementlog_m0 |  | fuserid |
| 2 | pk_dfa_agreementlog |  | fid |

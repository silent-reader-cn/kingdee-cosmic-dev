# RFM评估历史-ocdbd_chlrfmrecord

## RFM评估历史-主表 t_ocdbd_chlrfmrecord

- **表名称：** RFM评估历史-主表
- **表名：** t_ocdbd_chlrfmrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 评估时间 | timestamp | 0 |  |  | null | 评估时间 |
| 3 | forderamount | 交易金额 | numeric | 23 | 10 | √ | 0 | 交易金额 |
| 4 | frecentorderdate | 最近交易时间 | timestamp | 0 |  |  | null | 最近交易时间 |
| 5 | frfmresult | RFM评估结果 | bpchar | 1 |  | √ | ' ' | RFM评估结果,枚举: 0 :一般挽留客户 1 :一般保持客户 2 :一般发展客户 3 :一般价值客户 4 :重要挽留客户 5 :重要保持客户 6 :重要发展客户 7 :重要价值客户 |
| 6 | fmetric1 | 指标1 | bpchar | 1 |  | √ | ' ' | 指标1,枚举: 2 :近 0 :远 |
| 7 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 8 | fdaysbetween | 最近交易时间（天） | int4 | 32 |  | √ | 0 | 最近交易时间（天） |
| 9 | fordercount | 交易频率（次） | int4 | 32 |  | √ | 0 | 交易频率（次） |
| 10 | fmetric2 | 指标2 | bpchar | 1 |  | √ | ' ' | 指标2,枚举: 1 :高 0 :低 |
| 11 | fmetric3 | 指标3 | bpchar | 1 |  | √ | ' ' | 指标3,枚举: 4 :高 0 :低 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_chlrfmrecord |  | fid |
| 2 | idx_ocdbd_chlrfmrecord |  | fchannelid |

# 渠道指标数据-ocdbd_chlmetrics_data

## 渠道指标数据-主表 t_ocdbd_chlmetrics_data

- **表名称：** 渠道指标数据-主表
- **表名：** t_ocdbd_chlmetrics_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmetricsid | 渠道指标 | int8 | 64 |  | √ | 0 | [渠道指标 ocdbd_chlmetrics](../ocdbd_files/ocdbd_chlmetrics.md) |
| 3 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 4 | fmetricsdata | 指标数据 | numeric | 23 | 10 | √ | 0 | 指标数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_chlmetrics_data |  | fmetricsid,fchannelid |
| 2 | pk_ocdbd_chlmetrics_data |  | fid |

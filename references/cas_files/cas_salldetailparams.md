# 核销订单返回报文-cas_salldetailparams

## 核销订单返回报文-主表 t_cas_salldetailparam

- **表名称：** 核销订单返回报文-主表
- **表名：** t_cas_salldetailparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbatchnumber | 批次号 | varchar | 80 |  | √ | ' ' | 批次号 |
| 3 | fmessage | 报文 | text | 0 |  |  | null | 报文 |
| 4 | fsuccessflag | 成功标识 | bpchar | 1 |  | √ | '0' | 成功标识 |
| 5 | fmessage_tag | 报文_详情 | text | 0 |  |  | null | 报文_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_sallparam_fid |  | fbatchnumber |
| 2 | pk_t_cas_salldetailparam |  | fid |

# 通道定义-privacy_transchannel

## 通道定义-主表 t_privacy_transchannel

- **表名称：** 通道定义-主表
- **表名：** t_privacy_transchannel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsender | 发出方(国家地区) | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 3 | fstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 7 | fistransmission | 允许传输 | bpchar | 1 |  | √ | '1' | 允许传输 |
| 8 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | frecipient | 接收方(国家地区) | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_privacy_transchannel |  | fid |
| 2 | idx_privacy_channel_num |  | fnumber |

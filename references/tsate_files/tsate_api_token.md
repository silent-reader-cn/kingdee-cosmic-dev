# 通道token数据-tsate_api_token

## 通道token数据-主表 t_tsate_api_token

- **表名称：** 通道token数据-主表
- **表名：** t_tsate_api_token

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | ftoken | 认证码 | varchar | 255 |  | √ | ' ' | 认证码 |
| 9 | fenable | 是否生效（异常情况手动修改） | varchar | 50 |  | √ | ' ' | 是否生效（异常情况手动修改）,枚举: 1 :生效 0 :失效 |
| 10 | ftoken_tag | 认证码_详情 | text | 0 |  |  | null | 认证码_详情 |
| 11 | ftimeout | 超时时间(单位小时) | varchar | 50 |  | √ | ' ' | 超时时间(单位小时) |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fchannel | 通道 | int8 | 64 |  | √ | 0 | 申报通道 tsate_channel |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_api_token |  | fid |
| 2 | idx_tsate_apitok_num |  | fbillno |

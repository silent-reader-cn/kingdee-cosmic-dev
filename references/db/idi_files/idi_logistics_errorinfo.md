# 物流查询失败信息-idi_logistics_errorinfo

## 物流查询失败信息-主表 t_idi_logisticserrorinfo

- **表名称：** 物流查询失败信息-主表
- **表名：** t_idi_logisticserrorinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessage | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 3 | fcompanyname | 快递公司名称 | varchar | 100 |  | √ | ' ' | 快递公司名称 |
| 4 | fcompnaynum | 快递公司简码 | varchar | 30 |  | √ | ' ' | 快递公司简码 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forder | 快递单号 | varchar | 50 |  | √ | ' ' | 快递单号 |
| 7 | fbillid | 单据id | varchar | 36 |  | √ | ' ' | 单据id |
| 8 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 9 | fmobile | 联系人手机号码 | varchar | 30 |  | √ | ' ' | 联系人手机号码 |
| 10 | fbilltypeid | 单据类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fcode | 错误码 | varchar | 5 |  | √ | ' ' | 错误码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_idi_logisticserrorinfo |  | fbillid,fbilltypeid |
| 2 | pk_t_idi_logisticserrorinfo |  | fid |

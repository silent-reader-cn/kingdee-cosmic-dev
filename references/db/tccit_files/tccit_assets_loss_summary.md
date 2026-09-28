# 资产损失扣除底稿-tccit_assets_loss_summary

## 资产损失扣除底稿-主表 t_tccit_assets_loss_sum

- **表名称：** 资产损失扣除底稿-主表
- **表名：** t_tccit_assets_loss_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 4 | fdamagesincome | 资产赔偿收入 | numeric | 23 | 10 | √ | 0.0000000000 | 资产赔偿收入 |
| 5 | foriginal | 资产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 资产原值 |
| 6 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :行号 count :合计 |
| 7 | fincomesum | 收入总额 | numeric | 23 | 10 | √ | 0.0000000000 | 收入总额 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 9 | fabnormalincome | 非正常损失进项转出 | numeric | 23 | 10 | √ | 0.0000000000 | 非正常损失进项转出 |
| 10 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 11 | fassetslossamount | 资产损失税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 资产损失税收金额 |
| 12 | fsumdepreciate | 税务累计折旧摊销 | numeric | 23 | 10 | √ | 0.0000000000 | 税务累计折旧摊销 |
| 13 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |
| 14 | fitemtype | 资产损失类型 | varchar | 50 |  | √ | ' ' | 资产损失类型 |
| 15 | freserveverify | 资产损失准备金核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 资产损失准备金核销金额 |
| 16 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 17 | fzzje | 资产损失账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 资产损失账载金额 |
| 18 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 19 | fassetsbase | 资产计税基础 | numeric | 23 | 10 | √ | 0.0000000000 | 资产计税基础 |
| 20 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 21 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 22 | fdisposalincome | 资产处置收入 | numeric | 23 | 10 | √ | 0.0000000000 | 资产处置收入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_assets_loss_sum |  | fid |
| 2 | idx_tccit_assets_loss_sum |  | forgid,fskssqq,fskssqz,fitemtype |

# 货补池余额-occba_supplement

## 货补池余额-主表 t_occba_supplement

- **表名称：** 货补池余额-主表
- **表名：** t_occba_supplement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 7 | flastupdatetime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 8 | fsupqty | 货补数量 | numeric | 23 | 10 | √ | 0 | 货补数量 |
| 9 | foccupyqty | 占用数量 | numeric | 23 | 10 | √ | 0 | 占用数量 |
| 10 | favailableqty | 可用货补数量 | numeric | 23 | 10 | √ | 0 | 可用货补数量 |
| 11 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 12 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 13 | frebateaccountid | 资金池账户 | int8 | 64 |  | √ | 0 | [资金池余额 ocdbd_rebateaccount](../occba_files/ocdbd_rebateaccount.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_supplement |  | fid |
| 2 | idx_occba_supplement_no |  | fnumber |

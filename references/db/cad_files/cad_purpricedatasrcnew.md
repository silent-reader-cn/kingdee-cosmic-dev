# 取价来源数据-cad_purpricedatasrcnew

## 取价来源数据-主表 t_cad_purpricedatasrc

- **表名称：** 取价来源数据-主表
- **表名：** t_cad_purpricedatasrc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsettlecurrency | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fauxptyid | 物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 12 | fbillsource | 单据来源 | varchar | 60 |  | √ | ' ' | 单据来源,枚举: contract :采购合同 order :采购订单 |
| 13 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_purpricedatasrc |  | fid |
| 2 | idx_cad_purpricedatasrc |  | fpurorgid |

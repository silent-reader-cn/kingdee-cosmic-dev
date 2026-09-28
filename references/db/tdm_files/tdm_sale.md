# 销售数据-tdm_sale

## 销售数据-主表 t_tdm_saleinfo

- **表名称：** 销售数据-主表
- **表名：** t_tdm_saleinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsourcemethod | 来源方式 | varchar | 50 |  | √ | ' ' | 来源方式,枚举: new :手工新增 excel :excel导入 sys :系统生成 |
| 4 | fmaterielid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 8 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 9 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fcustomername | 采购方名称 | varchar | 50 |  | √ | ' ' | 采购方名称 |
| 14 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | fsourcesys | 来源单据 | varchar | 50 |  | √ | ' ' | 来源单据 |
| 17 | funitname | 计量单位名称 | varchar | 100 |  | √ | ' ' | 计量单位名称 |
| 18 | fmaterielname | 物料名称 | varchar | 50 |  | √ | ' ' | 物料名称 |
| 19 | funtaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 20 | fspec | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 21 | fpurchasertxt | 采购方(废弃) | varchar | 100 |  | √ | ' ' | 采购方(废弃) |
| 22 | fsourcesysno | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 23 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 24 | ftaxorgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | funtaxprice | 不含税单价 | numeric | 23 | 10 | √ | 0 | 不含税单价 |
| 26 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fcustomerid | 采购方 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_saleinfo_org |  | forgid |
| 2 | pk_tdm_saleinfo |  | fid |

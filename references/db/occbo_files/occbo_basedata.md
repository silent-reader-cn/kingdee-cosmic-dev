# 渠道出库数据-occbo_basedata

## 渠道出库数据-主表 t_occbo_basedata

- **表名称：** 渠道出库数据-主表
- **表名：** t_occbo_basedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsaleunitid | 销售计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 4 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fsrcbillentryseq | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 8 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 11 | fsaleqty | 销售数量 | numeric | 23 | 10 | √ | 0 | 销售数量 |
| 12 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 13 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 15 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 18 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 19 | fmonthname | 月份 | varchar | 80 |  | √ | ' ' | 月份 |
| 20 | fbizdate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 21 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 23 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 25 | fsrcbillentityid | 来源单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_basedata_midci |  | fmonthname,fitemid,fdepartmentid,fchannelid,fispresent |
| 2 | pk_occbo_basedata |  | fid |

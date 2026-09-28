# 销量开单-occbo_salevolume

## 分录信息-子表 t_occbo_salevolume_e

- **表名称：** 分录信息-子表
- **表名：** t_occbo_salevolume_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fserialunitid | 序列号单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fserialno | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 7 | foutstockqty | 出库数量 | numeric | 23 | 10 | √ | 0 | 出库数量 |
| 8 | funitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fserialid | 序列号 | int8 | 64 |  | √ | 0 | 商品序列号 ococic_snmainfile |
| 11 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 12 | fwarehouseid | 渠道仓库 | int8 | 64 |  | √ | 0 | 渠道仓库 ococic_warehouse |
| 13 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 14 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 15 | fenableserial | 启用序列号管理 | bpchar | 1 |  | √ | '0' | 启用序列号管理 |
| 16 | foutstockbaseqty | 出库基本数量 | numeric | 23 | 10 | √ | 0 | 出库基本数量 |
| 17 | flocationid | 渠道仓位 | int8 | 64 |  | √ | 0 | 渠道仓位 ococic_location |
| 18 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 19 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_salevolume_e_id |  | fid |
| 2 | pk_occbo_salevolume_e |  | fentryid |

---

## 销量开单-主表 t_occbo_salevolume

- **表名称：** 销量开单-主表
- **表名：** t_occbo_salevolume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalqty | 开单数量 | numeric | 23 | 10 | √ | 0 | 开单数量 |
| 3 | ftotalamount | 开单金额 | numeric | 23 | 10 | √ | 0 | 开单金额 |
| 4 | fup2channelid | 所属二级 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 5 | fsaleoption | 开单方向 | bpchar | 1 |  | √ | 'A' | 开单方向,枚举: A :正向 B :反向 |
| 6 | fdepartid | 所属部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fparentchannelid | 上级渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 9 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fchannelid | 开单门店 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fvipphone | 会员电话 | varchar | 15 |  | √ | ' ' | 会员电话 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fvipname | 会员名称 | varchar | 100 |  | √ | ' ' | 会员名称 |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fvipid | 会员 | int8 | 64 |  | √ | 0 | 会员档案 ocdbd_user |
| 23 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fup1channelid | 所属一级 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 25 | fsellerid | 销售员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 27 | fbizdate | 开单日期 | timestamp | 0 |  |  | null | 开单日期 |
| 28 | fstockorgid | 渠道库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fcurrencyid | 开单币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_salevolume |  | fid |
| 2 | idx_occbo_salevolume_fbillno |  | fbillno |

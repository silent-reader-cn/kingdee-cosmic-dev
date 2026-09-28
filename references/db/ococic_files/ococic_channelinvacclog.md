# 渠道即时库存更新日志2-ococic_channelinvacclog

## 渠道即时库存更新日志2-主表 t_ococic_chlinvacclog

- **表名称：** 渠道即时库存更新日志2-主表
- **表名：** t_ococic_chlinvacclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchannelstockid | 渠道仓库 | int8 | 64 |  | √ | 0 | 渠道仓库 ococic_warehouse |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fstockqty | 库存单位数量 | numeric | 23 | 10 | √ | 0 | 库存单位数量 |
| 6 | fsalechannelid | 销售组织渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 7 | fproductdate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fchannelstockstatusid | 渠道库存状态 | int8 | 64 |  | √ | 0 | 渠道库存状态 ococic_stockstatus |
| 10 | feffectivedate | 有效日期至 | timestamp | 0 |  |  | null | 有效日期至 |
| 11 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 12 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 13 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fassistunitid | 主辅单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 17 | flotnum | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 18 | fstockunitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | fchannellocationid | 渠道仓位 | int8 | 64 |  | √ | 0 | 渠道仓位 ococic_location |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 23 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 25 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 26 | flotid | 批号Id | int8 | 64 |  | √ | 0 | 商品批号 ococic_lot |
| 27 | fchannelstocktypeid | 渠道库存类型 | int8 | 64 |  | √ | 0 | 渠道库存类型 ococic_stocktype |
| 28 | fbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 29 | fbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 30 | fbillentityid | 来源单据名称 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 31 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 32 | fassistqty | 主辅助单位数量 | numeric | 23 | 10 | √ | 0 | 主辅助单位数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_chlinvacclog |  | fid |
| 2 | idx_ococic_chlinvacclog_beid |  | fbillid,fbillentryid |
| 3 | idx_ococic_chlinvacclog_ci |  | fchannelid,fitemid |

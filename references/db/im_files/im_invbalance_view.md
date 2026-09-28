# 库存余额表（数据查看）-im_invbalance_view

## 库存余额表（数据查看）-主表 t_im_invbalance

- **表名称：** 库存余额表（数据查看）-主表
- **表名：** t_im_invbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finqty3rd | finqty3rd | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | finqty | 本期收入(计量单位) | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入(计量单位) |
| 4 | foutqty | 本期发出(计量单位) | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出(计量单位) |
| 5 | foutqty2nd | 本期发出(辅助单位) | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出(辅助单位) |
| 6 | flotnumber | 批号编码 | varchar | 100 |  | √ | ' ' | 批号编码 |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fendqty3rd | fendqty3rd | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | funit2ndid | 主辅单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | finqty2nd | 本期收入(辅助单位) | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入(辅助单位) |
| 12 | fendqty2nd | 结存数量(辅助单位) | numeric | 23 | 10 | √ | 0.0000000000 | 结存数量(辅助单位) |
| 13 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fbalancetype | 余额类型 | bpchar | 1 |  | √ | '1' | 余额类型,枚举: 1 :库存余额 2 :核算余额 |
| 16 | foutqty3rd | foutqty3rd | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fisinit | 是否初始化数据 | bpchar | 1 |  | √ | ' ' | 是否初始化数据 |
| 18 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 19 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 20 | fendbaseqty | 结存数量(基本单位) | numeric | 23 | 10 | √ | 0.0000000000 | 结存数量(基本单位) |
| 21 | fdimstr | fdimstr | varchar | 1200 |  | √ | ' ' |  |
| 22 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 23 | finbaseqty | 本期收入(基本单位) | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入(基本单位) |
| 24 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fendperiod | 结束期间 | int8 | 64 |  | √ | 0 | 结束期间 |
| 26 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 28 | fbgnqty | 期初数量(计量单位) | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量(计量单位) |
| 29 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | fdimmd5str | fdimmd5str | varchar | 64 |  | √ | ' ' |  |
| 31 | fkeepertype | 保管者类型 | varchar | 30 |  | √ | ' ' | 保管者类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 32 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 33 | foutbaseqty | 本期发出(基本单位) | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出(基本单位) |
| 34 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fbgnbaseqty | 期初数量(基本单位) | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量(基本单位) |
| 36 | flotid | 批号 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 37 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 38 | fendqty | 结存数量(计量单位) | numeric | 23 | 10 | √ | 0.0000000000 | 结存数量(计量单位) |
| 39 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 40 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 41 | fbgnqty3rd | fbgnqty3rd | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fperiod | 开始期间 | int8 | 64 |  | √ | 0 | 开始期间 |
| 43 | funit3rdid | funit3rdid | int8 | 64 |  | √ | 0 |  |
| 44 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 45 | fbgnqty2nd | 期初数量(辅助单位) | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量(辅助单位) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invbalance_fkey |  | fdimmd5str,fstartdate,fbalancetype |
| 2 | idx_im_invbc_fmlid |  | fmaterialid |
| 3 | t_im_invbalance_pkey |  | fid |
| 4 | idx_im_invbc_fwid |  | fwarehouseid |
| 5 | idx_im_invbc_forgfb |  | forgid,fbalancetype |

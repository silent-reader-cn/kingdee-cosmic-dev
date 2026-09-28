# 领料差异分摊F7-im_mdc_backdiffshare_f7

## 领料差异分摊F7-主表 t_im_mdc_invbackdifshare

- **表名称：** 领料差异分摊F7-主表
- **表名：** t_im_mdc_invbackdifshare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fassignstauts | 生成状态 | varchar | 50 |  | √ | ' ' | 生成状态,枚举: A :未分配 B :部分分配 C :完全分配 |
| 5 | foutownerid | foutownerid | int8 | 64 |  | √ | 0 |  |
| 6 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 7 | flocation2 | flocation2 | int8 | 64 |  | √ | 0 |  |
| 8 | finvdatenum | finvdatenum | numeric | 23 | 10 | √ | 0 |  |
| 9 | finvtype | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 10 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 11 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fisadd | fisadd | bpchar | 1 |  | √ | '0' |  |
| 13 | fmaterial | fmaterial | int8 | 64 |  | √ | 0 |  |
| 14 | fdifnum | 差异数量 | numeric | 23 | 10 | √ | 0 | 差异数量 |
| 15 | foutkeeperid | foutkeeperid | int8 | 64 |  | √ | 0 |  |
| 16 | fwaitsharenum | 待分摊数量 | numeric | 23 | 10 | √ | 0 | 待分摊数量 |
| 17 | fbusinvassignnum | fbusinvassignnum | numeric | 23 | 10 | √ | 0 |  |
| 18 | fischange | fischange | bpchar | 1 |  | √ | '0' |  |
| 19 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 20 | funitfield | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 22 | finvaccnum | 即时库存 | numeric | 23 | 10 | √ | 0 | 即时库存 |
| 23 | foutinvstatusid | foutinvstatusid | int8 | 64 |  | √ | 0 |  |
| 24 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 25 | fbusinvaccnum | fbusinvaccnum | numeric | 23 | 10 | √ | 0 |  |
| 26 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fexpirydate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 28 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | flicenseno | flicenseno | int8 | 64 |  | √ | 0 |  |
| 31 | fassignnum | 已生成数量 | numeric | 23 | 10 | √ | 0 | 已生成数量 |
| 32 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 33 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 34 | fbuswaitsharenum | fbuswaitsharenum | numeric | 23 | 10 | √ | 0 |  |
| 35 | fbusinventorynum | fbusinventorynum | numeric | 23 | 10 | √ | 0 |  |
| 36 | fbusunitid | fbusunitid | int8 | 64 |  | √ | 0 |  |
| 37 | foutkeepertype | foutkeepertype | varchar | 50 |  | √ | ' ' |  |
| 38 | fmaterielmasterid | 物料（主数据） | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 39 | factissueqty | factissueqty | numeric | 23 | 10 | √ | 0 |  |
| 40 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 41 | fbusdifnum | fbusdifnum | numeric | 23 | 10 | √ | 0 |  |
| 42 | fsharestatus | 分摊状态 | varchar | 50 |  | √ | ' ' | 分摊状态,枚举: A :未分摊 B :部分分摊 C :完全分摊 |
| 43 | fqtyfield5 | fqtyfield5 | numeric | 23 | 10 | √ | 0 |  |
| 44 | fdifshare | fdifshare | bpchar | 1 |  | √ | '0' |  |
| 45 | foutownertype | foutownertype | varchar | 50 |  | √ | ' ' |  |
| 46 | finventory | 盘点数量 | numeric | 23 | 10 | √ | 0 | 盘点数量 |
| 47 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 48 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 49 | fcansendqty | fcansendqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | finvstatus | finvstatus | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_invbackdifshare |  | fentryid |
| 2 | idx_t_im_mdc_invback_a |  | fid |

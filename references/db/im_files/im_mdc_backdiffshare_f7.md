# 领料差异分摊F7-im_mdc_backdiffshare_f7

## 领料差异分摊F7-主表 t_im_mdc_invbackdifshare

- **表名称：** 领料差异分摊F7-主表
- **表名：** t_im_mdc_invbackdifshare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassignnum | 已生成数量 | numeric | 23 | 10 | √ | 0 | 已生成数量 |
| 3 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | foutkeepertype | foutkeepertype | varchar | 50 |  | √ | ' ' |  |
| 8 | fmaterielmasterid | 物料（主数据） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 9 | fassignstauts | 生成状态 | varchar | 50 |  | √ | ' ' | 生成状态,枚举: A :未分配 B :部分分配 C :完全分配 |
| 10 | foutownerid | foutownerid | int8 | 64 |  | √ | 0 |  |
| 11 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 12 | flocation2 | flocation2 | int8 | 64 |  | √ | 0 |  |
| 13 | finvdatenum | finvdatenum | numeric | 23 | 10 | √ | 0 |  |
| 14 | finvtype | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 15 | factissueqty | factissueqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 17 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 18 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fisadd | fisadd | bpchar | 1 |  | √ | '0' |  |
| 20 | fsharestatus | 分摊状态 | varchar | 50 |  | √ | ' ' | 分摊状态,枚举: A :未分摊 B :部分分摊 C :完全分摊 |
| 21 | fmaterial | fmaterial | int8 | 64 |  | √ | 0 |  |
| 22 | fqtyfield5 | fqtyfield5 | numeric | 23 | 10 | √ | 0 |  |
| 23 | fdifnum | 差异数量 | numeric | 23 | 10 | √ | 0 | 差异数量 |
| 24 | foutkeeperid | foutkeeperid | int8 | 64 |  | √ | 0 |  |
| 25 | fwaitsharenum | 待分摊数量 | numeric | 23 | 10 | √ | 0 | 待分摊数量 |
| 26 | fdifshare | fdifshare | bpchar | 1 |  | √ | '0' |  |
| 27 | foutownertype | foutownertype | varchar | 50 |  | √ | ' ' |  |
| 28 | fischange | fischange | bpchar | 1 |  | √ | '0' |  |
| 29 | finventory | 盘点数量 | numeric | 23 | 10 | √ | 0 | 盘点数量 |
| 30 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 31 | funitfield | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 32 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 33 | finvaccnum | 即时库存 | numeric | 23 | 10 | √ | 0 | 即时库存 |
| 34 | foutinvstatusid | foutinvstatusid | int8 | 64 |  | √ | 0 |  |
| 35 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 36 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 38 | fexpirydate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 39 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 40 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 41 | fcansendqty | fcansendqty | numeric | 23 | 10 | √ | 0 |  |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | finvstatus | finvstatus | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_invbackdifshare |  | fentryid |
| 2 | idx_t_im_mdc_invback_a |  | fid |

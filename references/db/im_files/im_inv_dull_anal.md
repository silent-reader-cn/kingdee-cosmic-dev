# 库存呆滞数据集-im_inv_dull_anal

## 库存呆滞数据集-主表 t_im_inv_dull_anal

- **表名称：** 库存呆滞数据集-主表
- **表名：** t_im_inv_dull_anal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 9 | fisdull | 是否呆滞 | bpchar | 1 |  | √ | '0' | 是否呆滞 |
| 10 | fdullqty | 呆滞数量 | numeric | 23 | 10 | √ | 0 | 呆滞数量 |
| 11 | fstarttime | 业务起始日期 | timestamp | 0 |  |  | null | 业务起始日期 |
| 12 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 13 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fversiontime | 版本同步日期 | timestamp | 0 |  |  | null | 版本同步日期 |
| 15 | fdulltype | 呆滞类型 | varchar | 50 |  | √ | ' ' | 呆滞类型,枚举: 1 :未入未出 2 :只入未出 |
| 16 | fdullbaseqty | 呆滞基本数量 | numeric | 23 | 10 | √ | 0 | 呆滞基本数量 |
| 17 | fdullday | 呆滞天数 | int8 | 64 |  | √ | 0 | 呆滞天数 |
| 18 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 19 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fendtime | 业务截止日期 | timestamp | 0 |  |  | null | 业务截止日期 |
| 23 | fkeycol | Keycol | varchar | 50 |  | √ | ' ' | Keycol |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_inv_dull_anal |  | fid |
| 2 | idx_im_inv_dull_anal_fkey |  | fkeycol,fdullday |

# 库存物料数据集-im_inv_inm_anal

## 库存物料数据集-主表 t_im_inv_inm_anal

- **表名称：** 库存物料数据集-主表
- **表名：** t_im_inv_inm_anal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 9 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 10 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fversiontime | 版本同步日期 | timestamp | 0 |  |  | null | 版本同步日期 |
| 12 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 13 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 16 | fkeycol | Keycol | varchar | 50 |  | √ | ' ' | Keycol |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_inv_inm_anal |  | fid |
| 2 | idx_im_inv_inm_anal_fkey |  | fkeycol |

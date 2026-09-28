# 库存预警数据集-im_inv_warn_anal

## 库存预警数据集-主表 t_im_inv_warn_anal

- **表名称：** 库存预警数据集-主表
- **表名：** t_im_inv_warn_anal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 4 | fcalcflag | 计算标识 | int4 | 32 |  | √ | 1 | 计算标识 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fwarninvqty | 预警数量 | numeric | 23 | 10 | √ | 0 | 预警数量 |
| 9 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 10 | fdiffqty | 差异数量 | numeric | 23 | 10 | √ | 0 | 差异数量 |
| 11 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 12 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 13 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fiswarndiff | 是否预警差异 | bpchar | 1 |  | √ | '0' | 是否预警差异 |
| 15 | fversiontime | 版本同步日期 | timestamp | 0 |  |  | null | 版本同步日期 |
| 16 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 17 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fwarntypename | 预警类型 | varchar | 30 |  | √ | ' ' | 预警类型 |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 21 | fiswarndiffcalcflag | 是否差异预警计算标识 | int4 | 32 |  | √ | 1 | 是否差异预警计算标识 |
| 22 | fkeycol | Keycol | varchar | 50 |  | √ | ' ' | Keycol |
| 23 | fwarntype | 预警类型标识 | varchar | 50 |  | √ | ' ' | 预警类型标识,枚举: 0 :最小库存预警 1 :最大库存预警 2 :安全库存预警 3 :再订货点预警 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_inv_warn_anal |  | fid |
| 2 | idx_im_inv_warn_anal_fkey |  | fkeycol |

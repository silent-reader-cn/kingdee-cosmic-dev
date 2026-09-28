# 库存对数结果-cal_checkinvbgnqtyrpt

## 库存对数结果-主表 t_cal_checkqtyresult

- **表名称：** 库存对数结果-主表
- **表名：** t_cal_checkqtyresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | festorageorgunitid | 库存组织（库存） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmaterialid | 物料（存货） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fconfiguredcodeid | 配置号（存货） | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 6 | fematerialid | 物料（库存） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | finvstatusid | 库存状态（存货） | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 8 | feownerid | 货主（库存） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | feinvstatusid | 库存状态（库存） | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 10 | feprojectid | 项目号（库存） | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 11 | fassistid | 辅助属性（存货） | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 13 | feconfiguredcodeid | 配置号（库存） | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 14 | fownertype | 货主类型（存货） | varchar | 30 |  | √ | ' ' | 货主类型（存货）,枚举: bos_org :核算组织 |
| 15 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | flot | 批号（存货） | varchar | 255 |  | √ | ' ' | 批号（存货） |
| 17 | fbaseunitid | 基本单位（存货） | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | febaseunitid | 基本单位（库存） | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | febaseqty | 数量（库存） | numeric | 23 | 10 | √ | 0 | 数量（库存） |
| 20 | fstorageorgunitid | 库存组织（存货） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fprojectid | 项目号（存货） | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | finvtypeid | 库存类型（存货） | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 23 | felocationid | 仓位（库存） | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 24 | fewarehouseid | 仓库（库存） | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 25 | fwarehouseid | 仓库（存货） | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 26 | fownerid | 货主（存货） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | flocationid | 仓位（存货） | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 28 | feownertype | 货主类型（库存） | varchar | 30 |  | √ | ' ' | 货主类型（库存）,枚举: bos_org :核算组织 |
| 29 | fbaseqty | 数量（存货） | numeric | 23 | 10 | √ | 0 | 数量（存货） |
| 30 | feinvtypeid | 库存类型（库存） | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 31 | felot | 批号（库存） | varchar | 255 |  | √ | ' ' | 批号（库存） |
| 32 | feassistid | 辅助属性（库存） | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_checkqtyresult_fid |  | fid |
| 2 | pk_cal_checkqtyresult |  | fid |

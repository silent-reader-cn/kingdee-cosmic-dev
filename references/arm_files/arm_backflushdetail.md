# 交互式倒冲-arm_backflushdetail

## 日程冲销-子表 t_arm_schedulewriteoff

- **表名称：** 日程冲销-子表
- **表名：** t_arm_schedulewriteoff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 工单数量 | numeric | 23 | 10 | √ | 0 | 工单数量 |
| 3 | forderunitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | forderid | 查看详情 | int8 | 64 |  | √ | 0 | 查看详情 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | funreportqty | 未汇报数量 | numeric | 23 | 10 | √ | 0 | 未汇报数量 |
| 7 | foperate | 查看详情 | varchar | 50 |  | √ | ' ' | 查看详情 |
| 8 | fwriteoffqty | 冲销数量 | numeric | 23 | 10 | √ | 0 | 冲销数量 |
| 9 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 10 | forderstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: P :计划 F :计划确认 E :锁定 R :下达 C :关闭 |
| 11 | fstartdatetime | 计划开工日期 | timestamp | 0 |  |  | null | 计划开工日期 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fduedatetime | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_schedulewriteoff |  | fid |
| 2 | pk_t_arm_schedulewriteoff |  | fentryid |

---

## 倒冲-子表 t_arm_backflush

- **表名称：** 倒冲-子表
- **表名：** t_arm_backflush

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnewline | 是否新增行 | bpchar | 1 |  | √ | ' ' | 是否新增行,枚举: 0 :0 1 :1 |
| 3 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 : 1 :不足 2 :超发 |
| 4 | fcomponentid | 子项编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 5 | fbackflushedqty | 应倒冲数量 | numeric | 23 | 10 | √ | 0 | 应倒冲数量 |
| 6 | flock | 是否锁定 | bpchar | 1 |  | √ | ' ' | 是否锁定,枚举: 0 :不锁定 1 :锁定 |
| 7 | fcompunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fbackflushqty | 倒冲数量 | numeric | 23 | 10 | √ | 0 | 倒冲数量 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcompauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fcompmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_backflush |  | fcomponentid,fcompmaterialversionid,fcompauxpty |
| 2 | pk_t_arm_backflush |  | fentryid |

---

## 交互式倒冲-主表 t_arm_interbackflush

- **表名称：** 交互式倒冲-主表
- **表名：** t_arm_interbackflush

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproductionlineid | 生产线 | int8 | 64 |  | √ | 0 | 生产线 arm_linecapacity |
| 3 | fworkshopid | 车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmaterialno | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fnotmatchqty | 多余数量 | numeric | 23 | 10 | √ | 0 | 多余数量 |
| 8 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 10 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | freportqty | 汇报数量 | numeric | 23 | 10 | √ | 0 | 汇报数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_interbackflush |  | fmaterialno,fmaterialversionid,fauxpty |
| 2 | pk_t_arm_interbackflush |  | fid |

---

## 倒冲明细-子表 t_arm_backflushdetail

- **表名称：** 倒冲明细-子表
- **表名：** t_arm_backflushdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmastermaterialid | 子项编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 2 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 3 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 4 | fdetailmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 5 | fdetailbackflushbaseqty | 倒冲基本数量 | numeric | 23 | 10 | √ | 0 | 倒冲基本数量 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 8 | fcompdetailauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 10 | fisallowneginv | fisallowneginv | bpchar | 1 |  | √ | ' ' |  |
| 11 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 12 | fcompbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fcompdetailunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 15 | fcomponentdetailid | 子项编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 19 | fdetailbackflushqty | 倒冲数量 | numeric | 23 | 10 | √ | 0 | 倒冲数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_backflushdetail |  | fdetailid |
| 2 | idx_t_arm_backflushdetail |  | fentryid |

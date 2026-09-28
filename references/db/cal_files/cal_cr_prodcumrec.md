# 生产消耗记录-cal_cr_prodcumrec

## 生产消耗记录-主表 t_cal_cr_prodcumrec

- **表名称：** 生产消耗记录-主表
- **表名：** t_cal_cr_prodcumrec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | frtpplanid | 还原方案 | int8 | 64 |  | √ | 0 | [还原方案 cal_cr_retrospectplan](../cal_files/cal_cr_retrospectplan.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 12 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_cr_prodcumrec_m0 |  | fbillno |
| 2 | pk_cal_cr_prodcumrec |  | fid |

---

## 单据体-子表 t_cal_cr_prodcumrecentry

- **表名称：** 单据体-子表
- **表名：** t_cal_cr_prodcumrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flbillno | l_编码 | varchar | 50 |  | √ | ' ' | l_编码 |
| 3 | flqty | l_数量 | numeric | 23 | 10 | √ | 0 | l_数量 |
| 4 | frmaterialid | r_物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | frbookdate | r_记账日期 | timestamp | 0 |  |  | null | r_记账日期 |
| 6 | frbillentryid | r_业务单据分录id | int8 | 64 |  | √ | 0 | r_业务单据分录id |
| 7 | frbizbillid | r_业务单据id | int8 | 64 |  | √ | 0 | r_业务单据id |
| 8 | frbillno | r_编码 | varchar | 50 |  | √ | ' ' | r_编码 |
| 9 | frbizentityobjectid | r_业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | flamount | l_金额 | numeric | 23 | 10 | √ | 0 | l_金额 |
| 13 | flbillentryid | l_业务单据分录id | int8 | 64 |  | √ | 0 | l_业务单据分录id |
| 14 | flbizentityobjectid | l_业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | flbookdate | l_记账日期 | timestamp | 0 |  |  | null | l_记账日期 |
| 17 | frqty | r_数量 | numeric | 23 | 10 | √ | 0 | r_数量 |
| 18 | flbizbillid | l_业务单据id | int8 | 64 |  | √ | 0 | l_业务单据id |
| 19 | framount | r_金额 | numeric | 23 | 10 | √ | 0 | r_金额 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_cr_prodcumrecentry_fk |  | fid |
| 2 | pk_cal_cr_prodcumrecentry |  | fentryid |

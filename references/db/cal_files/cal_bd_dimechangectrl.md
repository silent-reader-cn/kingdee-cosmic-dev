# 核算变更处理控制-cal_bd_dimechangectrl

## 核算变更处理控制-多语言表 t_cal_dimechangectrl_l

- **表名称：** 核算变更处理控制-多语言表
- **表名：** t_cal_dimechangectrl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_dimechangectrl_l_id |  | fid,flocaleid |
| 2 | pk_cal_dimechangectrl_l |  | fpkid |

---

## 核算变更处理控制-主表 t_cal_dimechangectrl

- **表名称：** 核算变更处理控制-主表
- **表名：** t_cal_dimechangectrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fapprovetime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftype | 变更类型 | varchar | 10 |  | √ | 'A' | 变更类型,枚举: A :物料计价方法变更 B :核算维度变更 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fyearperiod | 年期编号 | int4 | 32 |  | √ | 0 | 年期编号 |
| 15 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 16 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 17 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fiscaled | 是否核算 | bpchar | 1 |  | √ | '0' | 是否核算 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_dimechangectrl_ac |  | fcostaccountid |
| 2 | idx_cal_dimechangectrl_range |  | fcalrangeid |
| 3 | pk_cal_dimechangectrl |  | fid |

---

## 单据体-子表 t_cal_dimechangectrlentry

- **表名称：** 单据体-子表
- **表名：** t_cal_dimechangectrlentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhisyear | 核算年 | int4 | 32 |  | √ | 0 | 核算年 |
| 3 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fhisperiod | 核算期间 | int4 | 32 |  | √ | 0 | 核算期间 |
| 5 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fhisiscaled | 是否核算 | bpchar | 1 |  | √ | '0' | 是否核算 |
| 9 | fhisyearperiod | 核算年期编号 | int4 | 32 |  | √ | 0 | 核算年期编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_dimechangectrlentry |  | fentryid |
| 2 | idx_cal_dimechangectrlentry_id |  | fid |

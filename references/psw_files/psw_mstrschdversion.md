# 计划编制版本-psw_mstrschdversion

## 单据体-子表 t_psw_mstrschdvermtl

- **表名称：** 单据体-子表
- **表名：** t_psw_mstrschdvermtl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 4 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fmaterialmaster | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_mstrschdvermtl |  | fentryid |
| 2 | idx_t_psw_mstrschdvermtl |  | fid,fentryid |

---

## 计划编制版本-主表 t_psw_mstrschdversion

- **表名称：** 计划编制版本-主表
- **表名：** t_psw_mstrschdversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fproductionline | 生产线 | int8 | 64 |  | √ | 0 | 生产线 arm_linecapacity |
| 5 | fcreatetime | 版本日期 | timestamp | 0 |  |  | null | 版本日期 |
| 6 | fproorg | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fplanmonth | 计划月数 | int4 | 32 |  | √ | 0 | 计划月数 |
| 8 | fplanday | 计划日数 | int4 | 32 |  | √ | 0 | 计划日数 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fhorizonend | 计划日期范围.结束 | timestamp | 0 |  |  | null | 计划日期范围.结束 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fpredate | 前置时段(天) | int4 | 32 |  | √ | 0 | 前置时段(天) |
| 14 | fstartdate | 计划起始日 | timestamp | 0 |  |  | null | 计划起始日 |
| 15 | fplanweek | 计划周数 | int4 | 32 |  | √ | 0 | 计划周数 |
| 16 | fversionname | 版本名称 | varchar | 50 |  |  | ' ' | 版本名称 |
| 17 | fbillno | 版本号 | varchar | 30 |  | √ | ' ' | 版本号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fhorizonstart | 计划日期范围.开始 | timestamp | 0 |  |  | null | 计划日期范围.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_msvname |  | fversionname |
| 2 | idx_t_psw_msvproinfo |  | fproorg,fproductionline |
| 3 | pk_t_psw_mstrschdversion |  | fid |
| 4 | idx_t_psw_mstrschdversion |  | fbillno |

---

## 单据体-子表 t_psw_mstrschdvercap

- **表名称：** 单据体-子表
- **表名：** t_psw_mstrschdvercap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | favailcapacity | 剩余产能 | numeric | 23 | 10 | √ | 0 | 剩余产能 |
| 3 | fcumavailcapacity | 累计剩余产能 | numeric | 23 | 10 | √ | 0 | 累计剩余产能 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdateindex | 日期序号 | int4 | 32 |  | √ | 0 | 日期序号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_msvcapdate |  | fdateindex |
| 2 | idx_t_psw_mstrschdvercap |  | fid |
| 3 | pk_t_psw_mstrschdvercap |  | fentryid |

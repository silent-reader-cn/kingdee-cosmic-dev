# 核准平台筛选字段-psw_approval_filter

## 核准平台筛选字段-主表 t_psw_approvalfilter

- **表名称：** 核准平台筛选字段-主表
- **表名：** t_psw_approvalfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fnumofmonths | 计划月数 | int8 | 64 |  |  | null | 计划月数 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fpredays | 前置时段(天) | int8 | 64 |  |  | null | 前置时段(天) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 11 | fstartdate | 计划起始日 | timestamp | 0 |  |  | null | 计划起始日 |
| 12 | fplangroup | 计划分组 | varchar | 500 |  |  | null | 计划分组,枚举: |
| 13 | ftimefield | ftimefield | int4 | 32 |  |  | null |  |
| 14 | fbasedatafield | fbasedatafield | int8 | 64 |  |  | null |  |
| 15 | fsrcbillentity | 来源单据实体 | varchar | 50 |  |  | null | 来源单据实体 |
| 16 | fnumofweeks | 计划周数 | int8 | 64 |  |  | null | 计划周数 |
| 17 | fbillno | 单据编号 | varchar | 30 |  |  | null | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
| 19 | fbilltypefield | fbilltypefield | int8 | 64 |  |  | null |  |
| 20 | fnumofdays | 计划日数 | int8 | 64 |  |  | null | 计划日数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_ap_union |  | forgid |
| 2 | pk_t_psw_approvalfilter |  | fid |

---

## 生产线明细-子表 t_psw_filterprodline

- **表名称：** 生产线明细-子表
- **表名：** t_psw_filterprodline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductionlineid | 生产线 | int8 | 64 |  |  | null | 生产线 arm_linecapacity |
| 3 | fmodifierfield2 | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 5 | fmodifydatefield2 | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_fl_union |  | fentryid |
| 2 | pk_t_psw_filterprodline |  | fentryid |

---

## 需求组织明细-子表 t_psw_filterreqorg

- **表名称：** 需求组织明细-子表
- **表名：** t_psw_filterreqorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | freqorgid | 需求组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 4 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_fre_union |  | freqorgid |
| 2 | pk_t_psw_filterreqorg |  | fentryid |

---

## 物料明细-子表 t_psw_filtermateriel

- **表名称：** 物料明细-子表
- **表名：** t_psw_filtermateriel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierfield21 | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fmodifydatefield21 | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 5 | fmaterielid | 物料 | int8 | 64 |  |  | null | 物料生产信息 bd_materialmftinfo |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_filtermateriel |  | fentryid |
| 2 | idx_t_psw_fma_union |  | fmaterielid |

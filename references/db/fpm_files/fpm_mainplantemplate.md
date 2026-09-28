# 资金计划模板-fpm_mainplantemplate

## 资金计划模板-主表 t_fpm_mainplantemplate

- **表名称：** 资金计划模板-主表
- **表名：** t_fpm_mainplantemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fenabledate | fenabledate | timestamp | 0 |  |  | null |  |
| 6 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 7 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 8 | fcreatorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fbmreportid | 预算模板 | varchar | 36 |  | √ | ' ' | [预算模板 xkbm_reportsample](../xkbm_files/xkbm_reportsample.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | freportperiod | 编报周期 | varchar | 50 |  | √ | ' ' | 编报周期,枚举: 3 :月 5 :周 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fbmrptschemeid | 预算模板样式方案 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 16 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fenablerid | fenablerid | int8 | 64 |  | √ | 0 |  |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fplanningcalendar | 计划日历 | int8 | 64 |  | √ | 0 | [计划日历 fpm_planningcalendar](../fpm_files/fpm_planningcalendar.md) |
| 21 | feffectiveyear | 起始年度 | varchar | 50 |  | √ | ' ' | 起始年度,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_mainplantemplate |  | fid |
| 2 | idx_t_fpm_mainplantemplate |  | fnumber |

---

## 维度管理-子表 t_fpm_mainplantemplatedim

- **表名称：** 维度管理-子表
- **表名：** t_fpm_mainplantemplatedim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvisible | 是否可见 | bpchar | 1 |  | √ | '0' | 是否可见 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fdimension | 维度 | varchar | 50 |  | √ | ' ' | 维度,枚举: dept :部门 project :项目 settletype :结算方式 fundflowitem :资金用途 bizunit :业务单元 customer :客户 supplier :供应商 expense :费用项目 material :物料 materialgroup :物料分类 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpt_dim_fid |  | fid |
| 2 | pk_t_fpm_mainplantemplatedim |  | fentryid |

---

## 资金用途分录-子表 t_fpm_mainplantemplateffi

- **表名称：** 资金用途分录-子表
- **表名：** t_fpm_mainplantemplateffi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffundflowitem | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 3 | fcustomer | 客户必录 | bpchar | 1 |  | √ | '0' | 客户必录 |
| 4 | fmaterialgroup | 物料分类必录 | bpchar | 1 |  | √ | '0' | 物料分类必录 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fsettlement | 结算方式必录 | bpchar | 1 |  | √ | '0' | 结算方式必录 |
| 7 | finputtype | 录入方式 | varchar | 50 |  | √ | ' ' | 录入方式,枚举: manualinput :直接录入金额 detailinput :明细汇总 |
| 8 | fsupplier | 供应商必录 | bpchar | 1 |  | √ | '0' | 供应商必录 |
| 9 | fdepartment | 部门必录 | bpchar | 1 |  | √ | '0' | 部门必录 |
| 10 | frelateddetail | 明细信息类型 | varchar | 50 |  | √ | ' ' | 明细信息类型,枚举: procurement :采购明细信息 sale :销售明细信息 investment :投融资明细信息 other :补充明细信息 |
| 11 | fmaterial | 物料必录 | bpchar | 1 |  | √ | '0' | 物料必录 |
| 12 | fproject | 项目必录 | bpchar | 1 |  | √ | '0' | 项目必录 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fexpense | 费用项目必录 | bpchar | 1 |  | √ | '0' | 费用项目必录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpt_ffi_fid |  | fid |
| 2 | pk_t_fpm_mainplantemplateffi |  | fentryid |

---

## 资金计划模板-多语言表 t_fpm_mainplantemplate_l

- **表名称：** 资金计划模板-多语言表
- **表名：** t_fpm_mainplantemplate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_mainplantemplate_l |  | fpkid |
| 2 | idx_fpm_mpt_l_fid |  | fid |

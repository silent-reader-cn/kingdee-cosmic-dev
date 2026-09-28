# （废弃）信用档案申请单-ccm_archive_apply

## 信用额度分录-子表 t_ccm_archive_apply_sch_e

- **表名称：** 信用额度分录-子表
- **表名：** t_ccm_archive_apply_sch_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 信用数量 | numeric | 23 | 10 | √ | 0.0000000000 | 信用数量 |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fcustomer | fcustomer | int8 | 64 |  | √ | 0 |  |
| 5 | fsaleman | fsaleman | int8 | 64 |  | √ | 0 |  |
| 6 | farchiveid | 档案ID | int8 | 64 |  | √ | 0 | 档案ID |
| 7 | fmaterialgroup | fmaterialgroup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fprivilegeamt | 特批总额 | numeric | 23 | 10 | √ | 0.0000000000 | 特批总额 |
| 9 | fsalesgroup | fsalesgroup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fsalesorg | fsalesorg | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | foverdueamt | 逾期额度 | numeric | 23 | 10 | √ | 0.0000000000 | 逾期额度 |
| 13 | fquota | 信用额度 | numeric | 23 | 10 | √ | 0.0000000000 | 信用额度 |
| 14 | froleid0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 15 | froleid2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 16 | froleid1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | froleid3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 18 | fday | 信用天数 | numeric | 23 | 10 | √ | 0.0000000000 | 信用天数 |
| 19 | fmaterial | fmaterial | int8 | 64 |  | √ | 0 |  |
| 20 | fsalesdept | fsalesdept | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 21 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fgrade | 信用等级 | int8 | 64 |  | √ | 0 | 信用等级 ccm_grade |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_archive_apply_sch_e_fk |  | fid |
| 2 | t_ccm_archive_apply_sch_e_pkey |  | fentryid |

---

## （废弃）信用档案申请单-主表 t_ccm_archive_apply

- **表名称：** （废弃）信用档案申请单-主表
- **表名：** t_ccm_archive_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 120 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbegindate | 生效日期范围.开始 | timestamp | 0 |  |  | null | 生效日期范围.开始 |
| 7 | forgid | 授信组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | froletype2 | 维度成员类型2 | varchar | 80 |  | √ | ' ' | 维度成员类型2,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 10 | froletype3 | 维度成员类型3 | varchar | 80 |  | √ | ' ' | 维度成员类型3,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | forgfunc | forgfunc | varchar | 30 |  | √ | ' ' |  |
| 13 | froletype0 | 维度成员类型0 | varchar | 80 |  | √ | ' ' | 维度成员类型0,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | froletype1 | 维度成员类型1 | varchar | 80 |  | √ | ' ' | 维度成员类型1,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 16 | fenddate | 生效日期范围.结束 | timestamp | 0 |  |  | null | 生效日期范围.结束 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fscheme | 信控方案 | int8 | 64 |  | √ | 0 | （废弃）信控方案 ccm_scheme |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fdimension | fdimension | int8 | 64 |  | √ | 0 |  |
| 22 | fapplyyear | 年度 | varchar | 30 |  | √ | ' ' | 年度,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_archive_apply_pkey |  | fid |
| 2 | idx_ccm_archivea_fbillno |  | fbillno |

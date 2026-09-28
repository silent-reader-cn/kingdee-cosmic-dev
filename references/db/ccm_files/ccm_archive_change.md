# （废弃）信用档案变更申请单-ccm_archive_change

## （废弃）信用档案变更申请单-主表 t_ccm_archive_change

- **表名称：** （废弃）信用档案变更申请单-主表
- **表名：** t_ccm_archive_change

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 授信组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | froletype2 | 维度成员类型2 | varchar | 80 |  | √ | ' ' | 维度成员类型2,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 9 | froletype3 | 维度成员类型3 | varchar | 80 |  | √ | ' ' | 维度成员类型3,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | forgfunc | forgfunc | varchar | 30 |  | √ | ' ' |  |
| 12 | froletype0 | 维度成员类型0 | varchar | 80 |  | √ | ' ' | 维度成员类型0,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | froletype1 | 维度成员类型1 | varchar | 80 |  | √ | ' ' | 维度成员类型1,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 15 | fchangepersonid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fscheme | 信控方案 | int8 | 64 |  | √ | 0 | [（废弃）信控方案 ccm_scheme](../ccm_files/ccm_scheme.md) |
| 18 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fdimension | fdimension | int8 | 64 |  | √ | 0 |  |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_archive_change_pkey |  | fid |
| 2 | idx_ccm_ac_fbillno |  | fbillno |

---

## 信用额度分录-子表 t_ccm_archive_change_e

- **表名称：** 信用额度分录-子表
- **表名：** t_ccm_archive_change_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsaleman | fsaleman | int8 | 64 |  | √ | 0 |  |
| 3 | farchiveid | 档案ID | int8 | 64 |  | √ | 0 | 档案ID |
| 4 | fprivilegeamt | 特批总额 | numeric | 23 | 10 | √ | 0.0000000000 | 特批总额 |
| 5 | fgradebefore | 信用等级(原始) | int8 | 64 |  | √ | 0 | [（废弃）信用等级 ccm_grade](../ccm_files/ccm_grade.md) |
| 6 | fqtybefore | 信用数量(原始) | numeric | 23 | 10 | √ | 0.0000000000 | 信用数量(原始) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | froleid0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 9 | fenddate | 生效日期范围.结束 | timestamp | 0 |  |  | null | 生效日期范围.结束 |
| 10 | fenddatebefore | 生效日期范围(原始).结束 | timestamp | 0 |  |  | null | 生效日期范围(原始).结束 |
| 11 | froleid2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 12 | fbeforeoverdueamt | 逾期额度(原始) | numeric | 23 | 10 | √ | 0.0000000000 | 逾期额度(原始) |
| 13 | froleid1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 14 | froleid3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 15 | fday | 信用天数 | numeric | 23 | 10 | √ | 0.0000000000 | 信用天数 |
| 16 | fmainarchiveid | 主档案ID | int8 | 64 |  | √ | 0 | 主档案ID |
| 17 | fmaterial | fmaterial | int8 | 64 |  | √ | 0 |  |
| 18 | fbegindatebefore | 生效日期范围(原始).开始 | timestamp | 0 |  |  | null | 生效日期范围(原始).开始 |
| 19 | fgrade | 信用等级 | int8 | 64 |  | √ | 0 | [（废弃）信用等级 ccm_grade](../ccm_files/ccm_grade.md) |
| 20 | fqty | 信用数量 | numeric | 23 | 10 | √ | 0.0000000000 | 信用数量 |
| 21 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fcustomer | fcustomer | int8 | 64 |  | √ | 0 |  |
| 23 | fbegindate | 生效日期范围.开始 | timestamp | 0 |  |  | null | 生效日期范围.开始 |
| 24 | fquotabefore | 信用额度(原始) | numeric | 23 | 10 | √ | 0.0000000000 | 信用额度(原始) |
| 25 | fdaybefore | 信用天数(原始) | numeric | 23 | 10 | √ | 0.0000000000 | 信用天数(原始) |
| 26 | foverdueamt | 逾期额度 | numeric | 23 | 10 | √ | 0.0000000000 | 逾期额度 |
| 27 | fquota | 信用额度 | numeric | 23 | 10 | √ | 0.0000000000 | 信用额度 |
| 28 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fbeforeprivilegeamt | 特批总额(原始) | numeric | 23 | 10 | √ | 0.0000000000 | 特批总额(原始) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_archive_change_e_fk |  | fid |
| 2 | t_ccm_archive_change_e_pkey |  | fentryid |

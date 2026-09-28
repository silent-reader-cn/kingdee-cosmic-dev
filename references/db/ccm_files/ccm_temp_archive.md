# （废弃）临时信用档案申请单-ccm_temp_archive

## 临时档案设置分录-子表 t_ccm_temp_archive_entry

- **表名称：** 临时档案设置分录-子表
- **表名：** t_ccm_temp_archive_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | farchiveid | 档案ID | int8 | 64 |  | √ | 0 | 档案ID |
| 4 | famountfield | 临时额度 | numeric | 23 | 10 | √ | 0.0000000000 | 临时额度 |
| 5 | ftempqty | 临时数量 | numeric | 23 | 10 | √ | 0.0000000000 | 临时数量 |
| 6 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 7 | ftempdayfield | 临时天数 | int8 | 64 |  | √ | 0 | 临时天数 |
| 8 | fbegindate | 生效日期范围.开始 | timestamp | 0 |  |  | null | 生效日期范围.开始 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | froleid0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 11 | fenddate | 生效日期范围.结束 | timestamp | 0 |  |  | null | 生效日期范围.结束 |
| 12 | ftempoverdueamt | 临时逾期额度 | numeric | 23 | 10 | √ | 0.0000000000 | 临时逾期额度 |
| 13 | froleid2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 14 | fsalemanid | fsalemanid | int8 | 64 |  | √ | 0 |  |
| 15 | froleid1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 16 | froleid3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | ftempprivilegeamt | 临时特批总额 | numeric | 23 | 10 | √ | 0.0000000000 | 临时特批总额 |
| 18 | fmainarchiveid | 主档案ID | int8 | 64 |  | √ | 0 | 主档案ID |
| 19 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_temp_archive_entry_pkey |  | fentryid |
| 2 | idx_t_ccm_ta_fid |  | fid |

---

## （废弃）临时信用档案申请单-主表 t_ccm_temp_archive

- **表名称：** （废弃）临时信用档案申请单-主表
- **表名：** t_ccm_temp_archive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 授信组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fschemeid | 信控方案 | int8 | 64 |  | √ | 0 | [（废弃）信控方案 ccm_scheme](../ccm_files/ccm_scheme.md) |
| 8 | froletype2 | 维度成员类型2 | varchar | 80 |  | √ | ' ' | 维度成员类型2,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 9 | froletype3 | 维度成员类型3 | varchar | 80 |  | √ | ' ' | 维度成员类型3,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | froletype0 | 维度成员类型0 | varchar | 80 |  | √ | ' ' | 维度成员类型0,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 12 | ftextfield | 备注 | varchar | 120 |  |  | ' ' | 备注 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | froletype1 | 维度成员类型1 | varchar | 80 |  | √ | ' ' | 维度成员类型1,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fdimension | fdimension | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_temparchivea_fbillno |  | fbillno |
| 2 | t_ccm_temp_archive_pkey |  | fid |

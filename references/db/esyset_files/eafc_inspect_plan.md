# 业务检测配置-eafc_inspect_plan

## 业务检测配置-主表 tk_eafc_inspect_plan

- **表名称：** 业务检测配置-主表
- **表名：** tk_eafc_inspect_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_contain_bill | 包含单据 | bpchar | 1 |  | √ | '0' | 包含单据 |
| 3 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fk_eafc_contain_bill_iv | 包含单据发票 | bpchar | 1 |  | √ | '0' | 包含单据发票 |
| 5 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 6 | fk_eafc_contain_bank | 包含回单 | bpchar | 1 |  | √ | '0' | 包含回单 |
| 7 | fk_fpy_planclass | 适用分类： | varchar | 50 |  | √ | ' ' | 适用分类：,枚举: voucher :凭证 bill :业务单据 |
| 8 | fk_eafc_bill_att | 根据附件名称进行判断 | varchar | 100 |  | √ | ' ' | 根据附件名称进行判断 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fk_fpy_contain_bank | 包含单据-回单 | bpchar | 1 |  | √ | '0' | 包含单据-回单 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fk_eafc_planname | 方案名称： | varchar | 50 |  | √ | ' ' | 方案名称： |
| 13 | fk_eafc_voucher_att | 根据附件名称进行判断 | varchar | 100 |  | √ | ' ' | 根据附件名称进行判断 |
| 14 | fk_eafc_contain_field_ol | 某字段必须包含值 | bpchar | 1 |  | √ | '0' | 某字段必须包含值 |
| 15 | fk_eafc_textfield1 |  | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fk_eafc_radiogroupfield | 单选按钮组 | varchar | 50 |  | √ | ' ' | 单选按钮组,枚举: 1 :包含所有类型 2 :包含任一类型 |
| 19 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 1 :启用 2 :禁用 |
| 20 | fk_fpy_eafc_contain_bill | 包含自定义单据 | bpchar | 1 |  | √ | '0' | 包含自定义单据 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fk_eafc_contain_bill_fj | 包含单据附件 | bpchar | 1 |  | √ | '0' | 包含单据附件 |
| 24 | fk_fpy_contain_bill_invoi | 包含单据-发票 | bpchar | 1 |  | √ | '0' | 包含单据-发票 |
| 25 | fk_eafc_contain_appendix | 包含附件 | bpchar | 1 |  | √ | '0' | 包含附件 |
| 26 | fk_fpy_eafc_contain_appendix | 包含单据-附件 | bpchar | 1 |  | √ | '0' | 包含单据-附件 |
| 27 | fk_eafc_plancontent | 内容描述： | varchar | 2000 |  | √ | ' ' | 内容描述： |
| 28 | fk_eafc_textfield | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |
| 29 | fk_eafc_contain_bill_cont |  | varchar | 50 |  | √ | ' ' |  |
| 30 | fk_eafc_contain_invoice | 包含发票 | bpchar | 1 |  | √ | '0' | 包含发票 |
| 31 | fk_fpy_contain_bill_image | 包含单据-影像 | bpchar | 1 |  | √ | '0' | 包含单据-影像 |
| 32 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_inspect_plan |  | fid |

---

## 业务单据-数据范围-子表 tk_eafc_data_range_f

- **表名称：** 业务单据-数据范围-子表
- **表名：** tk_eafc_data_range_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_fpy_eafc_filed | 字段 | varchar | 50 |  | √ | ' ' | 字段,枚举: eafc_billname :单据类型 |
| 3 | fk_fpy_eafc_condition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: in :包含 = :等于 != :不等于 contain :在...中 |
| 4 | fk_fpy_eafc_content | 内容 | varchar | 50 |  | √ | ' ' | 内容 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_fpy_eafc_obj | 对象 | varchar | 50 |  | √ | ' ' | 对象,枚举: bizbill :业务单据 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_data_range_f |  | fentryid |
| 2 | idx__eafc_data_range_f_fk |  | fid |

---

## 单据体-子表 tk_eafc_data_range

- **表名称：** 单据体-子表
- **表名：** tk_eafc_data_range

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_content | 内容 | varchar | 50 |  | √ | ' ' | 内容 |
| 3 | fk_eafc_obj | 对象 | varchar | 50 |  | √ | ' ' | 对象,枚举: voucher :凭证 |
| 4 | fk_eafc_condition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: = :等于 != :不等于 > :大于 < :小于 in :包含 contain :在...中 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_eafc_filed | 字段 | varchar | 50 |  | √ | ' ' | 字段,枚举: eafc_voucher_type :凭证类型 eafc_account_date :过账日期 eafc_entryentity.eafc_account_code :科目代码 eafc_entryentity.eafc_account_name :科目名称 eafc_entryentity.eafc_credit :贷方金额 eafc_entryentity.eafc_debit :借方金额 eafc_entryentity.eafc_abstract :摘要 eafc_org_name :核算单位名称 eafc_org_no :核算单位代码 eafc_entryentity.eafc_account_dimensions :核算维度 eafc_creater :制单人 eafc_source_system :系统来源 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_data_range |  | fentryid |
| 2 | idx__eafc_data_range_fk |  | fid |

---

## 自定义单据类型-多选基础资料表 tk_eafc_mul_businesss

- **表名称：** 自定义单据类型-多选基础资料表
- **表名：** tk_eafc_mul_businesss

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_mul_businesss |  | fpkid |

---

## 适用组织-多选基础资料表 tk_eafc_inspect_plan_orgs

- **表名称：** 适用组织-多选基础资料表
- **表名：** tk_eafc_inspect_plan_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_inspect_plan_orgs_fk |  | fid |
| 2 | pk_eafc_inspect_plan_orgs |  | fpkid |

---

## 适用归档组织-多选基础资料表 tk_eafc_arcorgs

- **表名称：** 适用归档组织-多选基础资料表
- **表名：** tk_eafc_arcorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__tk_eafc_arcorgs |  | fpkid |
| 2 | idx__eafc_arcorgs_fk |  | fid |

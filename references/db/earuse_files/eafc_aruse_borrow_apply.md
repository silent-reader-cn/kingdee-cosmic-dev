# 借阅申请-eafc_aruse_borrow_apply

## 月报单据体-子表 tk_eafc_borrow_yb

- **表名称：** 月报单据体-子表
- **表名：** tk_eafc_borrow_yb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fk_eafc_register_yb | 月报id | varchar | 50 |  | √ | ' ' | 月报id |
| 5 | fk_eafc_location_month | 存储位置 | varchar | 50 |  | √ | ' ' | 存储位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_yb |  | fentryid |

---

## 凭证单据体-子表 tk_eafc_borrow_pz

- **表名称：** 凭证单据体-子表
- **表名：** tk_eafc_borrow_pz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_location_voucher | 存储位置 | varchar | 50 |  | √ | ' ' | 存储位置 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fk_eafc_relation_fid_pz | 凭证id | varchar | 50 |  | √ | ' ' | 凭证id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_pz |  | fentryid |

---

## 发票单据体-子表 tk_eafc_borrow_fp

- **表名称：** 发票单据体-子表
- **表名：** tk_eafc_borrow_fp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fk_eafc_relation_fid_fp | 发票id | varchar | 50 |  | √ | ' ' | 发票id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_fp |  | fentryid |

---

## 单据单据体-子表 tk_eafc_borrow_dj

- **表名称：** 单据单据体-子表
- **表名：** tk_eafc_borrow_dj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_location_bill | 存储位置 | varchar | 50 |  | √ | ' ' | 存储位置 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fk_eafc_relation_fid_dj | 单据id | varchar | 50 |  | √ | ' ' | 单据id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_dj |  | fentryid |

---

## 案卷单据体-子表 tk_eafc_borrow_volume

- **表名称：** 案卷单据体-子表
- **表名：** tk_eafc_borrow_volume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_relation_fid | 卷id | varchar | 50 |  | √ | ' ' | 卷id |
| 3 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fk_eafc_archivenum2 | 档案号 | varchar | 200 |  | √ | ' ' | 档案号 |
| 5 | fk_eafc_encrypt_type2 | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 6 | fk_eafc_stock_status2 | 是否出库 | varchar | 50 |  | √ | ' ' | 是否出库 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fk_eafc_entity_status2 | 载体形态 | varchar | 50 |  | √ | ' ' | 载体形态,枚举: 1 :电子 2 :实物 3 :混合 |
| 9 | fk_eafc_open_log2 | 开放标识 | varchar | 50 |  | √ | ' ' | 开放标识,枚举: 1 :开放 2 :控制 3 :延期开放 |
| 10 | fk_eafc_storage_period2 | 保管期限 | varchar | 50 |  | √ | ' ' | 保管期限,枚举: 1 :十年 2 :三十年 3 :永久 |
| 11 | fk_eafc_file_sign2 | 案卷题名 | varchar | 200 |  | √ | ' ' | 案卷题名 |
| 12 | fk_eafc_volume | 案卷号 | varchar | 50 |  | √ | ' ' | 案卷号 |
| 13 | fk_eafc_textfield | 期间 | varchar | 50 |  | √ | ' ' | 期间 |
| 14 | fk_eafc_desc | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 16 | fk_eafc_location_volume | 存储位置 | varchar | 50 |  | √ | ' ' | 存储位置 |
| 17 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_volume |  | fentryid |
| 2 | idx__eafc_borrow_volume_fk |  | fid |

---

## 余额调节表单据体-子表 tk_eafc_borrow_ye

- **表名称：** 余额调节表单据体-子表
- **表名：** tk_eafc_borrow_ye

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_relation_fid_ye | 余额调节表id | varchar | 50 |  | √ | ' ' | 余额调节表id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_ye |  | fentryid |

---

## 现金日记账单据体-子表 tk_eafc_borrow_xjrj

- **表名称：** 现金日记账单据体-子表
- **表名：** tk_eafc_borrow_xjrj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_relation_fid_xjrj | 日记账id | varchar | 50 |  | √ | ' ' | 日记账id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_xjrj |  | fentryid |

---

## 季报单据体-子表 tk_eafc_borrow_jb

- **表名称：** 季报单据体-子表
- **表名：** tk_eafc_borrow_jb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fk_eafc_relation_fid_jb | 季报id | varchar | 50 |  | √ | ' ' | 季报id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_jb |  | fentryid |

---

## 年报单据体-子表 tk_eafc_borrow_nb

- **表名称：** 年报单据体-子表
- **表名：** tk_eafc_borrow_nb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fk_eafc_relation_fid_nb | 年报id | varchar | 50 |  | √ | ' ' | 年报id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_nb |  | fentryid |

---

## 明细账单据体-子表 tk_eafc_borrow_mxz

- **表名称：** 明细账单据体-子表
- **表名：** tk_eafc_borrow_mxz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_relation_fid_mxz | 明细账id | varchar | 50 |  | √ | ' ' | 明细账id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_mxz |  | fentryid |

---

## 总账单据体-子表 tk_eafc_borrow_zz

- **表名称：** 总账单据体-子表
- **表名：** tk_eafc_borrow_zz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_relation_fid_zz | 总账id | varchar | 50 |  | √ | ' ' | 总账id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_zz |  | fentryid |

---

## 固定资产卡片单据体-子表 tk_eafc_borrow_gdzc

- **表名称：** 固定资产卡片单据体-子表
- **表名：** tk_eafc_borrow_gdzc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fk_eafc_relation_fid_gdzc | 卡片id | varchar | 50 |  | √ | ' ' | 卡片id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_gdzc |  | fentryid |

---

## 税务资料单据体-子表 tk_eafc_borrow_sw

- **表名称：** 税务资料单据体-子表
- **表名：** tk_eafc_borrow_sw

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fk_eafc_relation_fid_sw | 税务资料id | varchar | 50 |  | √ | ' ' | 税务资料id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_sw |  | fentryid |

---

## 银行回单单据体-子表 tk_eafc_borrow_yhhd

- **表名称：** 银行回单单据体-子表
- **表名：** tk_eafc_borrow_yhhd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fk_eafc_relation_fid_yhhd | 回单id | varchar | 50 |  | √ | ' ' | 回单id |
| 4 | fk_eafc_location_bank | 存储位置 | varchar | 50 |  | √ | ' ' | 存储位置 |
| 5 | fk_eafc_total_tax_amount | 单据金额 | numeric | 23 | 10 |  | null | 单据金额 |
| 6 | fk_eafc_uuid_yhhd | 回单uuid | varchar | 50 |  | √ | ' ' | 回单uuid |
| 7 | fk_eafc_basedatafield1 | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_yhhd |  | fentryid |

---

## 自定义分类通用表单据体-子表 tk_eafc_aruapp_entry_cb

- **表名称：** 自定义分类通用表单据体-子表
- **表名：** tk_eafc_aruapp_entry_cb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_org_cb | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_cus_amt04_cb | 金额4 | numeric | 23 | 10 |  | null | 金额4 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fk_eafc_cus_date08_cb | 日期08 | timestamp | 0 |  |  | null | 日期08 |
| 6 | fk_eafc_arcorg_cb | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 7 | fk_eafc_cus_date05_cb | 日期05 | timestamp | 0 |  |  | null | 日期05 |
| 8 | fk_eafc_cus_text04_cb | 自定义文本4 | varchar | 200 |  | √ | ' ' | 自定义文本4 |
| 9 | fk_eafc_cus_time03_cb | 长日期03 | timestamp | 0 |  |  | null | 长日期03 |
| 10 | fk_eafc_cus_text10_cb | 自定义文本10 | varchar | 200 |  | √ | ' ' | 自定义文本10 |
| 11 | fk_eafc_cus_date01_cb | 日期01 | timestamp | 0 |  |  | null | 日期01 |
| 12 | fk_eafc_cus_int02_cb | 整数02 | int4 | 32 |  | √ | 0 | 整数02 |
| 13 | fk_eafc_book_type_cb | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 14 | fk_eafc_cus_text14_cb | 自定义文本14 | varchar | 200 |  | √ | ' ' | 自定义文本14 |
| 15 | fk_eafc_entity_status_cb | 载体形态 | varchar | 50 |  | √ | ' ' | 载体形态,枚举: 1 :电子 2 :电子+纸质 |
| 16 | fk_eafc_period_new_cb | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间 |
| 17 | fk_eafc_cus_text18_cb | 自定义文本18 | varchar | 200 |  | √ | ' ' | 自定义文本18 |
| 18 | fk_eafc_cus_text20_cb | 自定义文本20 | varchar | 200 |  | √ | ' ' | 自定义文本20 |
| 19 | fk_eafc_rel_fid_cb | 分类通用id | varchar | 50 |  | √ | ' ' | 分类通用id |
| 20 | fk_eafc_register_cb | 归档人 | varchar | 50 |  | √ | ' ' | 归档人 |
| 21 | fk_eafc_cus_text03_cb | 自定义文本3 | varchar | 200 |  | √ | ' ' | 自定义文本3 |
| 22 | fk_eafc_cus_date07_cb | 日期07 | timestamp | 0 |  |  | null | 日期07 |
| 23 | fk_eafc_cus_amt03_cb | 金额3 | numeric | 23 | 10 |  | null | 金额3 |
| 24 | fk_eafc_cus_date04_cb | 日期04 | timestamp | 0 |  |  | null | 日期04 |
| 25 | fk_eafc_cus_text07_cb | 自定义文本7 | varchar | 200 |  | √ | ' ' | 自定义文本7 |
| 26 | fk_eafc_cus_time02_cb | 长日期02 | timestamp | 0 |  |  | null | 长日期02 |
| 27 | fk_eafc_cus_text13_cb | 自定义文本13 | varchar | 200 |  | √ | ' ' | 自定义文本13 |
| 28 | fk_eafc_register_time_cb | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 29 | fk_eafc_cus_int01_cb | 整数01 | int4 | 32 |  | √ | 0 | 整数01 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fk_eafc_cus_text17_cb | 自定义文本17 | varchar | 200 |  | √ | ' ' | 自定义文本17 |
| 32 | fk_eafc_cus_text02_cb | 自定义文本2 | varchar | 200 |  | √ | ' ' | 自定义文本2 |
| 33 | fk_eafc_cus_text09_cb | 自定义文本9 | varchar | 200 |  | √ | ' ' | 自定义文本9 |
| 34 | fk_eafc_cus_amt02_cb | 金额2 | numeric | 23 | 10 |  | null | 金额2 |
| 35 | fk_eafc_cus_text06_cb | 自定义文本6 | varchar | 200 |  | √ | ' ' | 自定义文本6 |
| 36 | fk_eafc_cus_time01_cb | 长日期01 | timestamp | 0 |  |  | null | 长日期01 |
| 37 | fk_eafc_cus_date03_cb | 日期03 | timestamp | 0 |  |  | null | 日期03 |
| 38 | fk_eafc_archivenum_cb | 档案号 | varchar | 200 |  | √ | ' ' | 档案号 |
| 39 | fk_eafc_cus_text12_cb | 自定义文本12 | varchar | 200 |  | √ | ' ' | 自定义文本12 |
| 40 | fk_eafc_cus_text16_cb | 自定义文本16 | varchar | 200 |  | √ | ' ' | 自定义文本16 |
| 41 | fk_eafc_relation_fid_cb | fk_eafc_relation_fid_cb | int8 | 64 |  | √ | 0 |  |
| 42 | fk_eafc_cus_text01_cb | 自定义文本1 | varchar | 200 |  | √ | ' ' | 自定义文本1 |
| 43 | fk_eafc_file_code_cb | 文件编码 | varchar | 200 |  | √ | ' ' | 文件编码 |
| 44 | fk_eafc_cus_amt01_cb | 金额1 | numeric | 23 | 10 |  | null | 金额1 |
| 45 | fk_eafc_cus_text08_cb | 自定义文本8 | varchar | 200 |  | √ | ' ' | 自定义文本8 |
| 46 | fk_eafc_cus_amt05_cb | 金额5 | numeric | 23 | 10 |  | null | 金额5 |
| 47 | fk_eafc_cus_text05_cb | 自定义文本5 | varchar | 200 |  | √ | ' ' | 自定义文本5 |
| 48 | fk_eafc_cus_date06_cb | 日期06 | timestamp | 0 |  |  | null | 日期06 |
| 49 | fk_eafc_cus_date02_cb | 日期02 | timestamp | 0 |  |  | null | 日期02 |
| 50 | fk_eafc_cus_int03_cb | 整数03 | int4 | 32 |  | √ | 0 | 整数03 |
| 51 | fk_eafc_cus_text11_cb | 自定义文本11 | varchar | 200 |  | √ | ' ' | 自定义文本11 |
| 52 | fk_eafc_cus_text15_cb | 自定义文本15 | varchar | 200 |  | √ | ' ' | 自定义文本15 |
| 53 | fk_eafc_cus_text19_cb | 自定义文本19 | varchar | 200 |  | √ | ' ' | 自定义文本19 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_aruapp_entry_cb |  | fentryid |

---

## 借阅人信息-子表 tk_eafc_borrow_entry

- **表名称：** 借阅人信息-子表
- **表名：** tk_eafc_borrow_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_borrowphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 3 | fk_fpy_login_times | 访问次数 | int4 | 32 |  | √ | 0 | 访问次数 |
| 4 | fk_fpy_login_ip | 访问设备ip | varchar | 200 |  | √ | ' ' | 访问设备ip |
| 5 | fk_eafc_borrowuser | 借阅人 | varchar | 50 |  | √ | ' ' | 借阅人 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fk_eafc_borrowemail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 8 | fk_eafc_description | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 9 | fk_eafc_borrowdeptid | 系统借阅部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fk_eafc_borrowdept | 借阅部门 | varchar | 50 |  | √ | ' ' | 借阅部门 |
| 11 | fk_eafc_borrowuserid | 系统借阅人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fk_fpy_login_pass | 提取密钥 | varchar | 50 |  | √ | ' ' | 提取密钥 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_borrow_entry |  | fentryid |
| 2 | idx_eafc_borrow_entry_fid |  | fid |

---

## 借阅申请-主表 tk_eafc_borrow_apply

- **表名称：** 借阅申请-主表
- **表名：** tk_eafc_borrow_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_stop_reason | 终止原因 | varchar | 50 |  | √ | ' ' | 终止原因 |
| 3 | fk_eafc_borrow_way_type | 分类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 4 | fk_eafc_borrow_count | 借阅数量 | varchar | 50 |  | √ | ' ' | 借阅数量 |
| 5 | fk_eafc_borrow_status | 借阅状态_旧 | varchar | 50 |  | √ | ' ' | 借阅状态_旧,枚举: 1 :待提交 2 :待审批 3 :审批中 4 :借阅中 5 :已归还 6 :已逾期 7 :已驳回 |
| 6 | forgid | 申请人业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fk_eafc_borrow_way | 借阅形式 | varchar | 50 |  | √ | ' ' | 借阅形式,枚举: 1 :按件借阅 2 :按卷借阅 3 :分类借阅 |
| 8 | fk_eafc_auditor | 审批人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 申请人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fk_eafc_borrow_address | 借阅链接 | varchar | 200 |  | √ | ' ' | 借阅链接 |
| 12 | fk_eafc_bill_type | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: 1 :新增 2 :续借 |
| 13 | fk_eafc_slippage | 逾期天数 | int8 | 64 |  |  | null | 逾期天数 |
| 14 | fk_item_eafc_borrow_type | 列表是否包含实物[弃用] | varchar | 50 |  | √ | ' ' | 列表是否包含实物[弃用],枚举: 1 :否 2 :是 |
| 15 | fk_eafc_borrow_org | 借阅组织 | varchar | 50 |  | √ | ' ' | 借阅组织 |
| 16 | fk_eafc_borrow_type | 是否包含实物 | varchar | 50 |  | √ | ' ' | 是否包含实物,枚举: 1 :否 2 :是 |
| 17 | fbillno | 借阅单号 | varchar | 30 |  | √ | ' ' | 借阅单号 |
| 18 | fk_eafc_borrow_dept | 借阅部门 | varchar | 50 |  | √ | ' ' | 借阅部门 |
| 19 | fk_eafc_arcorg | 申请人组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 20 | fk_eafc_return_date | 最终归还/终止时间 | timestamp | 0 |  |  | null | 最终归还/终止时间 |
| 21 | fk_eafc_select_dept | 系统借阅部门 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fk_eafc_borrow_manus | 实物稿本 | varchar | 50 |  | √ | ' ' | 实物稿本,枚举: 1 :原件 2 :打印副本 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fk_eafc_audit_result | 审批意见 | varchar | 50 |  | √ | ' ' | 审批意见 |
| 25 | fbillstatus | 借阅状态 | varchar | 50 |  | √ | ' ' | 借阅状态,枚举: 1 :待提交 2 :审批中 3 :已审核/借阅中 4 :已归还 5 :已逾期 6 :已驳回 7 :即将到期 8 :已终止 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fk_eafc_borrow_reason | 借阅事由 | varchar | 50 |  | √ | ' ' | 借阅事由 |
| 28 | fk_eafc_fid_lists | 借阅清单id | varchar | 1505 |  | √ | ' ' | 借阅清单id |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fk_eafc_start_time | 借阅起始日期.开始 | timestamp | 0 |  |  | null | 借阅起始日期.开始 |
| 31 | fk_eafc_borrow_user | 借阅人 | varchar | 50 |  | √ | ' ' | 借阅人 |
| 32 | fk_eafc_borrow_email | 借阅人邮箱 | varchar | 50 |  | √ | ' ' | 借阅人邮箱 |
| 33 | fk_eafc_borrow_reasontype | 借阅事由类型 | varchar | 50 |  | √ | ' ' | 借阅事由类型,枚举: 1 :查账需要借阅 2 :历史账务清理 3 :政府项目审计 4 :年度审计 5 :诉讼 6 :客户发票遗失 7 :项目申报 8 :税局抽查 9 :企业上云 10 :其他 |
| 34 | fk_eafc_borrow_no | 借阅单号 | varchar | 50 |  | √ | ' ' | 借阅单号 |
| 35 | fk_eafc_borrow_phone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 36 | fk_originally_eafc_borrow | 原始借阅单号 | varchar | 50 |  | √ | ' ' | 原始借阅单号 |
| 37 | fk_eafc_textfield | 备注说明 | varchar | 50 |  | √ | ' ' | 备注说明 |
| 38 | fk_eafc_select_borrow_u | 系统借阅人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fk_eafc_end_time | 借阅起始日期.结束 | timestamp | 0 |  |  | null | 借阅起始日期.结束 |
| 40 | fk_eafc_must_return | 是否要归还 | varchar | 50 |  | √ | ' ' | 是否要归还,枚举: 1 :是 2 :否 |
| 41 | fk_fpy_isborrowlimit | 借阅访问控制 | bpchar | 1 |  | √ | '0' | 借阅访问控制 |
| 42 | fk_eafc_allow_download | 是否允许下载 | varchar | 50 |  | √ | ' ' | 是否允许下载,枚举: 1 :是 2 :否 |
| 43 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_apply |  | fid |

---

## 银行对账单单据体-子表 tk_eafc_borrow_dzd

- **表名称：** 银行对账单单据体-子表
- **表名：** tk_eafc_borrow_dzd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_relation_fid_dzd | 对账单id | varchar | 50 |  | √ | ' ' | 对账单id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_dzd |  | fentryid |

---

## 文件单据体-子表 tk_eafc_borrow_file

- **表名称：** 文件单据体-子表
- **表名：** tk_eafc_borrow_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_relation_fid | 文件id | varchar | 50 |  | √ | ' ' | 文件id |
| 3 | fk_eafc_file_code1 | 文件编码 | varchar | 200 |  | √ | ' ' | 文件编码 |
| 4 | fk_eafc_business1 | 分类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 5 | fk_eafc_encrypt_type1 | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 6 | fk_eafc_file_way1 | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: 1 :散文件 2 :组合文件 3 :复合文件 |
| 7 | fk_eafc_archivenum1 | 档案号 | varchar | 200 |  | √ | ' ' | 档案号 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fk_eafc_stock_status1 | 是否出库 | varchar | 50 |  | √ | ' ' | 是否出库 |
| 10 | fk_eafc_open_log1 | 开放标识 | varchar | 50 |  | √ | ' ' | 开放标识,枚举: 1 :开放 2 :控制 3 :延期开放 |
| 11 | fk_eafc_storage_period1 | 保管期限 | varchar | 50 |  | √ | ' ' | 保管期限,枚举: 1 :10年 2 :30年 3 :永久 |
| 12 | fk_eafc_file_sign1 | 文件题名 | varchar | 200 |  | √ | ' ' | 文件题名 |
| 13 | fk_eafc_entity_status1 | 载体形态 | varchar | 50 |  | √ | ' ' | 载体形态,枚举: 1 :电子 2 :电子+纸质 |
| 14 | fk_eafc_period1 | 期间 | varchar | 50 |  | √ | ' ' | 期间 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 16 | fk_eafc_location_file | 存储位置 | varchar | 200 |  | √ | ' ' | 存储位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_file |  | fentryid |
| 2 | idx__eafc_borrow_file_fk |  | fid |

---

## 银行存款日记账单据体-子表 tk_eafc_borrow_yhck

- **表名称：** 银行存款日记账单据体-子表
- **表名：** tk_eafc_borrow_yhck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_relation_fid_yhck | 存款日记账id | varchar | 50 |  | √ | ' ' | 存款日记账id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_yhck |  | fentryid |

---

## 半年报单据体-子表 tk_eafc_borrow_bnb

- **表名称：** 半年报单据体-子表
- **表名：** tk_eafc_borrow_bnb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fk_eafc_relation_fid_bnb | 半年报id | varchar | 50 |  | √ | ' ' | 半年报id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_borrow_bnb |  | fentryid |

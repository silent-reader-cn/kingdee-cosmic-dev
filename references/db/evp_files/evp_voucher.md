# 凭证-evp_voucher

## 凭证-主表 t_evp_voucher

- **表名称：** 凭证-主表
- **表名：** t_evp_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 入池操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisintopool | 电子凭证入池 | bpchar | 1 |  | √ | '0' | 电子凭证入池 |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdirectbillid | 关联单据ID | int8 | 64 |  | √ | 0 | 关联单据ID |
| 6 | fisdelete | 已删除 | bpchar | 1 |  | √ | '0' | 已删除 |
| 7 | fvoucherno | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | farchivebatchcode | 归档批次号 | varchar | 255 |  | √ | ' ' | 归档批次号 |
| 11 | fisarchive | 归档 | bpchar | 1 |  | √ | '0' | 归档 |
| 12 | foriginsysid | 集成系统 | int8 | 64 |  | √ | 0 | [集成系统配置 evp_originsys](../evp_files/evp_originsys.md) |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 14 | fdirectbillno | 关联单据号 | varchar | 50 |  | √ | ' ' | 关联单据号 |
| 15 | fvdescription | 摘要 | varchar | 200 |  | √ | ' ' | 摘要 |
| 16 | fvoucherid | fvoucherid | varchar | 50 |  | √ | ' ' |  |
| 17 | fxhvoucherid | 星空凭证id | int8 | 64 |  | √ | 0 | 星空凭证id |
| 18 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 19 | fseqno | 票据流水号（唯一标识） | varchar | 200 |  | √ | ' ' | 票据流水号（唯一标识） |
| 20 | fhaspullbill | 已抽取关联单据 | bpchar | 1 |  | √ | '0' | 已抽取关联单据 |
| 21 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 22 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 23 | fdirectbilltype | 关联单据类型 | varchar | 50 |  | √ | ' ' | 关联单据类型 |
| 24 | fperiodtypeid | 会计日历 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 25 | fbatchcode | 批次号 | varchar | 128 |  | √ | ' ' | 批次号 |
| 26 | fishandle | 数据来源 | bpchar | 1 |  | √ | '0' | 数据来源,枚举: 0 :API导入 1 :手工新增 2 :系统抽取 |
| 27 | fbillid | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 28 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 29 | fintopooldate | 入池时间 | timestamp | 0 |  |  | null | 入池时间 |
| 30 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evp_voucher |  | fid |
| 2 | idx_evp_voucher |  | fbillid,forgid |

---

## 单据体-子表 t_evp_voucherentry

- **表名称：** 单据体-子表
- **表名：** t_evp_voucherentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbookedamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 3 | famountdc | 借贷方向 | bpchar | 1 |  | √ | '0' | 借贷方向,枚举: 1 :借方 0 :贷方 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailaccountname | 明细科目名称 | varchar | 50 |  | √ | ' ' | 明细科目名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fglaccountname | 总账科目名称 | varchar | 50 |  | √ | ' ' | 总账科目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evp_voucherentry |  | fentryid |
| 2 | idx_evp_voucherentry |  | fid |

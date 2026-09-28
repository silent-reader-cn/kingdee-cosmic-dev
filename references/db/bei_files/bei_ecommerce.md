# 电商流水入账方案-bei_ecommerce

## 单据体-子表 t_bei_entry_ecommerce

- **表名称：** 单据体-子表
- **表名：** t_bei_entry_ecommerce

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgroupfiled | 分组字段 | varchar | 256 |  | √ | ' ' | 分组字段,枚举: |
| 3 | fotherpayer | 付款单位（其他） | varchar | 256 |  | √ | ' ' | 付款单位（其他） |
| 4 | fdatafilter | 数据过滤条件 | text | 0 |  |  | ' ' | 数据过滤条件 |
| 5 | fpayee | 收款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 6 | fpayertype | 付款单位类型 | varchar | 64 |  | √ | ' ' | 付款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fdatafilterdesc | 适用条件 | text | 0 |  |  | ' ' | 适用条件 |
| 9 | fpayer | 付款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 10 | fnote | 摘要 | varchar | 512 |  | √ | ' ' | 摘要 |
| 11 | forg | 收付组织（隐藏） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | ftargetbill | 目标单据 | varchar | 64 |  | √ | ' ' | 目标单据,枚举: cas_recbill :收款单 cas_paybill :付款单 |
| 13 | fsettletype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 14 | fcontactunittype | 往来单位类型 | varchar | 64 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 15 | frectype | 收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 16 | fpayeetype | 收款单位类型 | varchar | 64 |  | √ | ' ' | 收款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 17 | fpaytype | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 18 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fdatafilter_tag | 数据过滤条件_详情 | text | 0 |  |  | ' ' | 数据过滤条件_详情 |
| 21 | fpayismatch | 付款单位匹配客商 | bpchar | 1 |  | √ | '0' | 付款单位匹配客商 |
| 22 | frecismatch | 收款单位匹配客商 | bpchar | 1 |  | √ | '0' | 收款单位匹配客商 |
| 23 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 24 | fotherpayee | 收款单位（其他） | varchar | 256 |  | √ | ' ' | 收款单位（其他） |
| 25 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 26 | frulename | 规则项名称 | varchar | 512 |  | √ | ' ' | 规则项名称 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_entry_ecommerce |  | fid,forg |
| 2 | pk_t_bei_entry_ecommerce |  | fentryid |

---

## 电商流水入账方案-主表 t_bei_ecommerce

- **表名称：** 电商流水入账方案-主表
- **表名：** t_bei_ecommerce

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | frecentday | 匹配最近X天流水 | int8 | 64 |  | √ | 0 | 匹配最近X天流水 |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 收付组织（废弃） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillstate | 下游单据状态 | varchar | 64 |  | √ | '4' | 下游单据状态,枚举: 1 :暂存 2 :已提交 3 :已审核 4 :已收款/已付款 |
| 10 | faccountbank | 银行账号（废弃） | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态 |
| 15 | fschema | 方案名称 | varchar | 128 |  | √ | ' ' | 方案名称 |
| 16 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_ecommerce |  | fid |
| 2 | idx_bei_ecommerre |  | fbillno,fbillstatus |

---

## 银行账户（废弃）-多选基础资料表 t_bei_ecom_account

- **表名称：** 银行账户（废弃）-多选基础资料表
- **表名：** t_bei_ecom_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_ecom_account |  | fid |
| 2 | pk_bei_ecom_account |  | fpkid |

---

## 适用范围-子表 t_bei_ecommerce_uorg

- **表名称：** 适用范围-子表
- **表名：** t_bei_ecommerce_uorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuseorg | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | faccountbank | 银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_ecommerce_uorg |  | faccountbank |
| 2 | pk_t_bei_ecommerce_uorg |  | fentryid |

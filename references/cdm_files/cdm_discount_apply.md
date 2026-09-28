# 贴现申请-cdm_discount_apply

## 贴现申请-多语言表 t_cdm_discount_apply_l

- **表名称：** 贴现申请-多语言表
- **表名：** t_cdm_discount_apply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 用途 | varchar | 50 |  | √ | ' ' | 用途 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_discountapply_l_fid |  | fid |
| 2 | pk_t_cdm_discount_apply_l |  | fpkid |

---

## 询价信息单据体-子表 t_cdm_discount_apply_inqu

- **表名称：** 询价信息单据体-子表
- **表名：** t_cdm_discount_apply_inqu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquotedate | 报价日期 | timestamp | 0 |  |  | null | 报价日期 |
| 3 | fpreferentialpoints | 优惠点数（bp） | numeric | 23 | 10 | √ | 0 | 优惠点数（bp） |
| 4 | fquoteinterestday | 利率转换天数 | varchar | 50 |  | √ | ' ' | 利率转换天数,枚举: 360 :360 365 :365 |
| 5 | fdescribe | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 6 | fopenprice | 公开价格（%） | numeric | 23 | 10 | √ | 0 | 公开价格（%） |
| 7 | fquoteorganizationid | 报价机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fquotecurrencyid | 报价币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fservicecharge | 手续费 | varchar | 50 |  | √ | ' ' | 手续费 |
| 11 | factualprice | 实际价格（%） | numeric | 23 | 10 | √ | 0 | 实际价格（%） |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fadjustdays | 调整天数 | int8 | 64 |  | √ | 0 | 调整天数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_discountapply_inqu_fid |  | fid |
| 2 | pk_t_cdm_discount_apply_inqu |  | fentryid |

---

## 贴现申请-主表 t_cdm_discount_apply

- **表名称：** 贴现申请-主表
- **表名：** t_cdm_discount_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdiscountdays | 贴现调整天数 | int8 | 64 |  | √ | 0 | 贴现调整天数 |
| 3 | frecbodyid | 受理机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdrafttypeid | 票据类型 | int8 | 64 |  | √ | 0 | 票据类型 cdm_billtype |
| 6 | famount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatedate | fcreatedate | varchar | 50 |  |  | ' ' |  |
| 9 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | frate | 贴现利率（%） | numeric | 23 | 10 | √ | 0 | 贴现利率（%） |
| 11 | fdraftcount | 票据张数 | varchar | 50 |  | √ | ' ' | 票据张数 |
| 12 | froughlyinterest | 匡算贴现利息金额 | numeric | 23 | 10 | √ | 0 | 匡算贴现利息金额 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | finterestday | 利率转换天数 | varchar | 50 |  | √ | ' ' | 利率转换天数,枚举: 360 :360 365 :365 |
| 20 | fbankcharge | 手续费 | numeric | 23 | 10 | √ | 0 | 手续费 |
| 21 | fdescription | 用途 | varchar | 50 |  | √ | ' ' | 用途 |
| 22 | fapplicant | fapplicant | varchar | 50 |  | √ | ' ' |  |
| 23 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 24 | fdiscamt | 贴现收款金额 | numeric | 23 | 10 | √ | 0 | 贴现收款金额 |
| 25 | fispushtradebill | 业务处理 | bpchar | 1 |  | √ | '0' | 业务处理 |
| 26 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fcompanyid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_discount_apply |  | fid |
| 2 | idx_cdmdiscountapply_billno |  | fbillno |

---

## 已选票据单据体-子表 t_cdm_discount_appl_entry

- **表名称：** 已选票据单据体-子表
- **表名：** t_cdm_discount_appl_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillamt | fbillamt | numeric | 23 | 10 | √ | 0 |  |
| 3 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | foldstatus | 票据旧状态 | varchar | 50 |  | √ | ' ' | 票据旧状态,枚举: registered :已登记 pledged :已质押 collocated :已托管 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fdraftbillid | 票据号码 | int8 | 64 |  | √ | 0 | 票据登记 cdm_draftbillf7 |
| 9 | ftranstatus | 票据交易状态 | varchar | 50 |  | √ | ' ' | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 failing :交易失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_discount_appl_entry |  | fentryid |
| 2 | idx_discountapply_emtry_fid |  | fid |

# 质押申请-cdm_pledge_apply

## 质押申请-多语言表 t_cdm_pledge_apply_l

- **表名称：** 质押申请-多语言表
- **表名：** t_cdm_pledge_apply_l

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
| 1 | pk_t_cdm_pledge_apply_l |  | fpkid |
| 2 | idx_pledgeapply_l_fid |  | fid |

---

## 已选票据单据体-子表 t_cdm_pledge_appl_entry

- **表名称：** 已选票据单据体-子表
- **表名：** t_cdm_pledge_appl_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillamt | fbillamt | numeric | 23 | 10 | √ | 0 |  |
| 3 | foldstatus | 票据旧状态 | varchar | 30 |  | √ | ' ' | 票据旧状态,枚举: registered :已登记 pledged :已质押 collocated :已托管 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fisinvalid | 作废 | bpchar | 1 |  | √ | '0' | 作废 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fdraftbillid | 票据号码 | int8 | 64 |  | √ | 0 | [票据登记 cdm_draftbillf7](../cdm_files/cdm_draftbillf7.md) |
| 8 | flogid | 票据交易记录 | int8 | 64 |  | √ | 0 | 票据交易记录 |
| 9 | fbillamount | 票面金额(子票包金额) | numeric | 23 | 10 | √ | 0 | 票面金额(子票包金额) |
| 10 | ftranstatus | 票据交易状态 | varchar | 30 |  | √ | ' ' | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 failing :交易失败 |
| 11 | fdraftpoolamount | 票据质押金额 | numeric | 23 | 10 | √ | 0 | 票据质押金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_pledge_appl_entry |  | fentryid |
| 2 | idx_pledgeapply_entry_fid |  | fid |

---

## 质押申请-主表 t_cdm_pledge_apply

- **表名称：** 质押申请-主表
- **表名：** t_cdm_pledge_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpledgeetypebase | 质权人基础资料类型 | varchar | 50 |  | √ | ' ' | 质权人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :业务单元 bd_finorginfo :合作金融机构 cas_othercontactunit :其他往来单位 |
| 4 | fpledgeebase | 质权人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 5 | fdrafttypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 6 | famount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fpoolprotocolid | 票据池 | int8 | 64 |  | √ | 0 | [银行票据池协议 cdm_pool_protocol](../cdm_files/cdm_pool_protocol.md) |
| 9 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fpledgeetext | 质权人 | varchar | 512 |  | √ | ' ' | 质权人 |
| 11 | fpledgeeaccount | 质权人银行账号 | varchar | 50 |  | √ | ' ' | 质权人银行账号 |
| 12 | fdraftcount | 票据张数 | varchar | 50 |  | √ | ' ' | 票据张数 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fpledgeeopenbank | 质权人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 15 | fpledgeeaccounttext | 质权人银行账号 | varchar | 50 |  | √ | ' ' | 质权人银行账号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fpledgeetype | 质权人类型 | varchar | 50 |  | √ | ' ' | 质权人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 bd_finorginfo :合作金融机构 |
| 21 | fpledgeeopenbanknumber | 质权人开户行行号 | varchar | 50 |  | √ | ' ' | 质权人开户行行号 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fdescription | 用途 | varchar | 50 |  | √ | ' ' | 用途 |
| 24 | fpledgeenddate | 质押到期日 | timestamp | 0 |  |  | null | 质押到期日 |
| 25 | fpoolamount | 票据质押金额 | numeric | 23 | 10 | √ | 0 | 票据质押金额 |
| 26 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 27 | fispushtradebill | 业务处理 | bpchar | 1 |  | √ | '0' | 业务处理 |
| 28 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fcompanyid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_pledge_apply |  | fid |
| 2 | idx_cdmpledgeapply_billno |  | fbillno |

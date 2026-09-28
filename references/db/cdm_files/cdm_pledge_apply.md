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
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdraftbillid | 票据号码 | int8 | 64 |  | √ | 0 | 票据登记 cdm_draftbillf7 |
| 7 | ftranstatus | 票据交易状态 | varchar | 30 |  | √ | ' ' | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 failing :交易失败 |

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
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpledgeetypebase | 质权人基础资料类型 | varchar | 50 |  | √ | ' ' | 质权人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :业务单元 bd_finorginfo :合作金融机构 |
| 4 | fpledgeebase | 质权人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 5 | fdrafttypeid | 票据类型 | int8 | 64 |  | √ | 0 | 票据类型 cdm_billtype |
| 6 | famount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fpledgeetext | 质权人 | varchar | 512 |  | √ | ' ' | 质权人 |
| 10 | fpledgeeaccount | 质权人银行账号 | varchar | 50 |  | √ | ' ' | 质权人银行账号 |
| 11 | fdraftcount | 票据张数 | varchar | 50 |  | √ | ' ' | 票据张数 |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fpledgeeopenbank | 质权人开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 14 | fpledgeeaccounttext | 质权人银行账号 | varchar | 50 |  | √ | ' ' | 质权人银行账号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fpledgeetype | 质权人类型 | varchar | 50 |  | √ | ' ' | 质权人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 bd_finorginfo :合作金融机构 |
| 20 | fpledgeeopenbanknumber | 质权人开户行行号 | varchar | 50 |  | √ | ' ' | 质权人开户行行号 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdescription | 用途 | varchar | 50 |  | √ | ' ' | 用途 |
| 23 | fpledgeenddate | 质押到期日 | timestamp | 0 |  |  | null | 质押到期日 |
| 24 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
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
| 1 | pk_t_cdm_pledge_apply |  | fid |
| 2 | idx_cdmpledgeapply_billno |  | fbillno |

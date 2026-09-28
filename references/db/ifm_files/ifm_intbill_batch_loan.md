# 贷款利息结息批量处理-ifm_intbill_batch_loan

## 结息记录-子表 t_ifm_intbill_batch_int

- **表名称：** 结息记录-子表
- **表名：** t_ifm_intbill_batch_int

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floanbillid | 放款单id | int8 | 64 |  | √ | 0 | 放款单id |
| 3 | fintsettleid | fintsettleid | int8 | 64 |  | √ | 0 |  |
| 4 | fisinterest | fisinterest | bpchar | 1 |  | √ | ' ' |  |
| 5 | fintsetnum | fintsetnum | varchar | 80 |  | √ | ' ' |  |
| 6 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fintdetail | 利息明细 | varchar | 255 |  | √ | ' ' | 利息明细 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | freversenum | freversenum | varchar | 80 |  | √ | ' ' |  |
| 10 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 11 | fintdays | 计息天数 | int8 | 64 |  | √ | 0 | 计息天数 |
| 12 | factualinstamt | 实收利息金额 | numeric | 19 | 6 | √ | 0 | 实收利息金额 |
| 13 | finneracctid | finneracctid | int8 | 64 |  | √ | 0 |  |
| 14 | fenddate | 计息结束日期 | timestamp | 0 |  |  | null | 计息结束日期 |
| 15 | fstatus | 生成状态 | varchar | 50 |  | √ | ' ' | 生成状态,枚举: success :成功 fail :失败 |
| 16 | frate | 计息利率 | numeric | 23 | 10 | √ | 0 | 计息利率 |
| 17 | fpayeeaccttext | 收款账号 | varchar | 80 |  | √ | ' ' | 收款账号 |
| 18 | fprinciple | 计息积数 | numeric | 23 | 10 | √ | 0 | 计息积数 |
| 19 | fsumpreint | fsumpreint | numeric | 23 | 10 | √ | 0 |  |
| 20 | fisreverse | fisreverse | bpchar | 1 |  | √ | ' ' |  |
| 21 | floancontractbillno | 合同单据编号 | varchar | 50 |  | √ | ' ' | 合同单据编号 |
| 22 | finterestamt | 利息金额 | numeric | 23 | 10 | √ | 0 | 利息金额 |
| 23 | fintcomment | 结息摘要 | varchar | 255 |  | √ | ' ' | 结息摘要 |
| 24 | fintinneracctid | fintinneracctid | int8 | 64 |  | √ | 0 |  |
| 25 | floanbillno | 放款单编号 | varchar | 50 |  | √ | ' ' | 放款单编号 |
| 26 | fintdetail_tag | 利息明细_详情 | text | 0 |  |  | null | 利息明细_详情 |
| 27 | fintobjectid | fintobjectid | int8 | 64 |  | √ | 0 |  |
| 28 | fpayeetype | 收款人类型 | varchar | 80 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 fbd_other :其他 |
| 29 | ftextcreditor | 债权人 | varchar | 255 |  | √ | ' ' | 债权人 |
| 30 | fnotpreint | fnotpreint | numeric | 23 | 10 | √ | 0 |  |
| 31 | freverseintamt | freverseintamt | numeric | 23 | 10 | √ | 0 |  |
| 32 | fpayeeid | 收款人ID | int8 | 64 |  | √ | 0 | 收款人ID |
| 33 | fintdetailnum | 结息记录编号 | varchar | 50 |  | √ | ' ' | 结息记录编号 |
| 34 | fstartdate | 计息开始日期 | timestamp | 0 |  |  | null | 计息开始日期 |
| 35 | fintbillid | 结息记录id | int8 | 64 |  | √ | 0 | 结息记录id |
| 36 | finttype | 结息类别 | varchar | 50 |  | √ | ' ' | 结息类别,枚举: lsbq :利随本清 jx :结息 |
| 37 | fcontractnum | 合同号 | varchar | 50 |  | √ | ' ' | 合同号 |
| 38 | fpayeetext | 收款人 | varchar | 80 |  | √ | ' ' | 收款人 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | floannum | floannum | varchar | 50 |  | √ | ' ' |  |
| 42 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | ffinorginfoid | ffinorginfoid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_intbill_batch_int |  | fid |
| 2 | pk_t_ifm_intbill_batch_int |  | fentryid |

---

## 贷款利息结息批量处理-主表 t_ifm_intbill_batch

- **表名称：** 贷款利息结息批量处理-主表
- **表名：** t_ifm_intbill_batch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fcurintdate | fcurintdate | timestamp | 0 |  |  | null |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | finteresttype | 结息类别 | varchar | 30 |  | √ | ' ' | 结息类别,枚举: hbfx :还本付息 fx :付息 |
| 8 | fpreintdate | fpreintdate | timestamp | 0 |  |  | null |  |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fissettleadd | fissettleadd | bpchar | 1 |  | √ | '0' |  |
| 12 | fdescription | 结息摘要（共用） | varchar | 255 |  | √ | ' ' | 结息摘要（共用） |
| 13 | fsettlecenterid | 结算中心 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fbizdealno | 受理单号 | varchar | 50 |  | √ | ' ' | 受理单号 |
| 16 | floantype | 贷款类型 | varchar | 50 |  | √ | ' ' | 贷款类型,枚举: ec :企业贷款 entrust :企业借款 bond :债权发行 loan :银行借款 |
| 17 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: preint :预提利息 loan :贷款利息 currentint :存款结息 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | foperatetype | foperatetype | varchar | 30 |  | √ | ' ' |  |
| 20 | fbizdate | 结息日期 | timestamp | 0 |  |  | null | 结息日期 |
| 21 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: hand :手工新增 ifm :内部金融 cfm :贷款管理 bond :债权发行 |
| 22 | fintsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: inneracct :内部账户 accountview :科目 |
| 23 | fbillno | 批次号 | varchar | 30 |  | √ | ' ' | 批次号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_intbill_batch |  | fbillno |
| 2 | pk_t_ifm_intbill_batch |  | fid |

---

## 贷款利息结息批量处理-多语言表 t_ifm_intbill_batch_l

- **表名称：** 贷款利息结息批量处理-多语言表
- **表名：** t_ifm_intbill_batch_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | 结息摘要（共用） | varchar | 255 |  | √ | ' ' | 结息摘要（共用） |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_intbill_batch_l |  | fpkid |
| 2 | idx_ifm_intbill_batch_l |  | fid,flocaleid |

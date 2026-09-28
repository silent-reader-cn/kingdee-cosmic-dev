# 付息批量处理模板-cfm_intbill_batch_loan

## 结息记录-子表 t_ifm_intbill_batch_int

- **表名称：** 结息记录-子表
- **表名：** t_ifm_intbill_batch_int

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floanbillid | 提款单id | int8 | 64 |  | √ | 0 | 提款单id |
| 3 | fintsettleid | fintsettleid | int8 | 64 |  | √ | 0 |  |
| 4 | fisinterest | fisinterest | bpchar | 1 |  | √ | ' ' |  |
| 5 | fintsetnum | fintsetnum | varchar | 80 |  | √ | ' ' |  |
| 6 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fintdetail | 利息明细 | varchar | 255 |  | √ | ' ' | 利息明细 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | freversenum | freversenum | varchar | 80 |  | √ | ' ' |  |
| 10 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 11 | fintdays | 计息天数 | int8 | 64 |  | √ | 0 | 计息天数 |
| 12 | factualinstamt | 实付利息金额 | numeric | 19 | 6 | √ | 0 | 实付利息金额 |
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
| 25 | floanbillno | 提款单编号 | varchar | 50 |  | √ | ' ' | 提款单编号 |
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
| 36 | finttype | 利息类别 | varchar | 50 |  | √ | ' ' | 利息类别,枚举: lsbq :利随本清 jx :结息 |
| 37 | fcontractnum | 合同号 | varchar | 50 |  | √ | ' ' | 合同号 |
| 38 | fpayeetext | 收款人 | varchar | 80 |  | √ | ' ' | 收款人 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 41 | floannum | floannum | varchar | 50 |  | √ | ' ' |  |
| 42 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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

## 付息批量处理模板-主表 t_ifm_intbill_batch

- **表名称：** 付息批量处理模板-主表
- **表名：** t_ifm_intbill_batch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurintdate | fcurintdate | timestamp | 0 |  |  | null |  |
| 3 | finteresttype | 结息类别 | varchar | 30 |  | √ | ' ' | 结息类别,枚举: |
| 4 | fpreintdate | fpreintdate | timestamp | 0 |  |  | null |  |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: preint :预提利息 loan :贷款利息 currentint :存款结息 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | foperatetype | foperatetype | varchar | 30 |  | √ | ' ' |  |
| 10 | fintsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: inneracct :内部账户 accountview :科目 |
| 11 | fbillno | 批次号 | varchar | 30 |  | √ | ' ' | 批次号 |
| 12 | fpostdate | fpostdate | timestamp | 0 |  |  | null |  |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fissettleadd | fissettleadd | bpchar | 1 |  | √ | '0' |  |
| 19 | fdescription | 结息摘要（共用） | varchar | 255 |  | √ | ' ' | 结息摘要（共用） |
| 20 | fsettlecenterid | 结算中心 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 21 | fbizdealno | 受理单号 | varchar | 50 |  | √ | ' ' | 受理单号 |
| 22 | floantype | 贷款类型 | varchar | 50 |  | √ | ' ' | 贷款类型,枚举: ec :企业贷款 entrust :企业借款 bond :债权发行 loan :银行借款 |
| 23 | fbizdate | 结息日期 | timestamp | 0 |  |  | null | 结息日期 |
| 24 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: hand :手工新增 cim :投资管理 ifm :内部金融 cfm :贷款管理 bond :债权发行 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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

## 付息批量处理模板-多语言表 t_ifm_intbill_batch_l

- **表名称：** 付息批量处理模板-多语言表
- **表名：** t_ifm_intbill_batch_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | 结息摘要（共用） | varchar | 500 |  |  | ' ' | 结息摘要（共用） |
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

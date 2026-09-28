# 内部利息结息单-ifm_currentintbill

## 关联子实体-子表 t_ifm_currentintbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_currentintbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_currentintbill_lk |  | fpkid |
| 2 | idx_t_ifm_currentintbill_lk_fid |  | fid |

---

## 内部利息结息单-关联追踪表 t_ifm_currentintbill_tc

- **表名称：** 内部利息结息单-关联追踪表
- **表名：** t_ifm_currentintbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_currentintbill_tc_tbill |  | ftbillid |
| 2 | pk_t_ifm_currentintbill_tc |  | fid |
| 3 | idx_ifm_currentintbill_tc_fid |  | ftbillid |
| 4 | idx_ifm_currentintbill_tc_tid |  | ftid |

---

## 内部利息结息单-主表 t_ifm_currentintbill

- **表名称：** 内部利息结息单-主表
- **表名：** t_ifm_currentintbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fintamount | 本期存款利息 | numeric | 23 | 10 | √ | 0 | 本期存款利息 |
| 3 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fisinterest | 是否结息 | bpchar | 1 |  | √ | ' ' | 是否结息 |
| 5 | fprincipal | fprincipal | numeric | 23 | 10 | √ | 0 |  |
| 6 | famount | 结算利息 | numeric | 23 | 10 | √ | 0 | 结算利息 |
| 7 | factualinstamt | 实际结算利息 | numeric | 19 | 6 | √ | 0 | 实际结算利息 |
| 8 | finneracctid | 内部账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fenddate | 结息结束日 | timestamp | 0 |  |  | null | 结息结束日 |
| 11 | fbiztype | 业务类型 | varchar | 80 |  | √ | ' ' | 业务类型,枚举: currentint :存款结息 preint :预提结息 reversepreint :冲销预提结息 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | frate | frate | numeric | 23 | 10 | √ | 0 |  |
| 14 | fisreverse | 是否冲销 | bpchar | 1 |  | √ | ' ' | 是否冲销 |
| 15 | fintsource | 计息对象来源 | varchar | 30 |  | √ | ' ' | 计息对象来源,枚举: inneracct :内部账户 accountview :科目 |
| 16 | fbillno | 结息记录编号 | varchar | 50 |  | √ | ' ' | 结息记录编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | foverintamt | 本期透支利息 | numeric | 23 | 10 | √ | 0 | 本期透支利息 |
| 19 | fintinneracctid | 利息计入账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcomment | 结息摘要 | varchar | 255 |  | √ | ' ' | 结息摘要 |
| 22 | fbatchno | 结息批次号 | varchar | 50 |  | √ | ' ' | 结息批次号 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fbegindate | 结息开始日 | timestamp | 0 |  |  | null | 结息开始日 |
| 25 | fdeposit | 存款积数 | numeric | 23 | 10 | √ | 0 | 存款积数 |
| 26 | foverdraft | 透支积数 | numeric | 23 | 10 | √ | 0 | 透支积数 |
| 27 | fintobjectid | 计息对象 | int8 | 64 |  | √ | 0 | 计息对象 ifm_intobject |
| 28 | fsumwritoffamt | 本次冲销金额汇总 | numeric | 23 | 10 | √ | 0 | 本次冲销金额汇总 |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | finterestday | 结息日 | timestamp | 0 |  |  | null | 结息日 |
| 31 | faccptno | faccptno | varchar | 50 |  | √ | ' ' |  |
| 32 | fsettlecenterid | 结算中心 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 33 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand :手工新增 cim :投资管理 ifm :内部金融 |
| 34 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 35 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 36 | floannum | floannum | varchar | 50 |  | √ | ' ' |  |
| 37 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fcompanyid | 成员单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_currentintbill |  | fbillno |
| 2 | pk_t_ifm_currentintbill |  | fid |

---

## 内部利息结息单-反写记录表 t_ifm_currentintbill_wb

- **表名称：** 内部利息结息单-反写记录表
- **表名：** t_ifm_currentintbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ifm_currentintbill_wb_fid |  | fid |
| 2 | pk_t_ifm_currentintbill_wb |  | fentryid |

---

## 预提冲销明细-子表 t_ifm_currintbill_pre

- **表名称：** 预提冲销明细-子表
- **表名：** t_ifm_currintbill_pre

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 预提结束日 | timestamp | 0 |  |  | null | 预提结束日 |
| 3 | fwriteoffamount | 本次冲销金额 | numeric | 23 | 10 | √ | 0 | 本次冲销金额 |
| 4 | fpreinstdays | 计息天数 | int8 | 64 |  | √ | 0 | 计息天数 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fprebookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 7 | fprebegindate | 预提开始日 | timestamp | 0 |  |  | null | 预提开始日 |
| 8 | fcanwriteoffamt | 可冲销金额 | numeric | 23 | 10 | √ | 0 | 可冲销金额 |
| 9 | fpreamount | 预提金额 | numeric | 23 | 10 | √ | 0 | 预提金额 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fpreintbillid | 预提记录编号 | int8 | 64 |  | √ | 0 | 内部利息预提单 ifm_preintbill |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_currintbill_pre |  | fid |
| 2 | pk_t_ifm_currintbill_pre |  | fentryid |

---

## 计息明细-子表 t_ifm_currintbill_entry

- **表名称：** 计息明细-子表
- **表名：** t_ifm_currintbill_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finstprincipal | 计息积数 | numeric | 23 | 10 | √ | 0 | 计息积数 |
| 3 | finststartdate | 结息开始日期 | timestamp | 0 |  |  | null | 结息开始日期 |
| 4 | finttype | 利息类型 | varchar | 30 |  | √ | ' ' | 利息类型,枚举: normal :存款利息 overdue :透支利息 |
| 5 | finstdays | 计息天数 | int8 | 64 |  | √ | 0 | 计息天数 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | finstenddate | 结息结束日期 | timestamp | 0 |  |  | null | 结息结束日期 |
| 8 | fintrate | 利率 | numeric | 23 | 10 | √ | 0 | 利率 |
| 9 | finstctg | 结息单类别 | varchar | 50 |  | √ | ' ' | 结息单类别,枚举: lsbq :利随本清 jx :结息 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | finstamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_currintbill_entry |  | fentryid |
| 2 | idx_ifm_currintbill_entry |  | fid |

# 内部利息预提单-ifm_preintbill

## 关联子实体-子表 t_ifm_preintbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_preintbill_lk

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
| 1 | pk_t_ifm_preintbill_lk |  | fpkid |
| 2 | idx_t_ifm_preintbill_lk_fid |  | fid |

---

## 内部利息预提单-主表 t_ifm_preintbill

- **表名称：** 内部利息预提单-主表
- **表名：** t_ifm_preintbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fintamount | 本期存款利息 | numeric | 23 | 10 | √ | 0 | 本期存款利息 |
| 3 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fisinterest | 是否结息 | bpchar | 1 |  | √ | '0' | 是否结息 |
| 5 | funwriteoffamt | 未冲销金额 | numeric | 23 | 10 | √ | 0 | 未冲销金额 |
| 6 | famount | 预提利息 | numeric | 23 | 10 | √ | 0 | 预提利息 |
| 7 | factualinstamt | 实际结算利息 | numeric | 23 | 10 | √ | 0 | 实际结算利息 |
| 8 | finneracctid | 内部账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fenddate | 预提结束日 | timestamp | 0 |  |  | null | 预提结束日 |
| 11 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: currentint :存款结息 preint :预提结息 reversepreint :冲销预提结息 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fwriteoffedamt | 已冲销金额 | numeric | 23 | 10 | √ | 0 | 已冲销金额 |
| 14 | fisreverse | 是否冲销 | bpchar | 1 |  | √ | '0' | 是否冲销 |
| 15 | fintsource | 计息对象来源 | varchar | 50 |  | √ | ' ' | 计息对象来源,枚举: inneracct :内部账户 accountview :科目 |
| 16 | fbillno | 预提记录编号 | varchar | 50 |  | √ | ' ' | 预提记录编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | foverintamt | 本期透支利息 | numeric | 23 | 10 | √ | 0 | 本期透支利息 |
| 19 | fintinneracctid | 利息计入账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcomment | 结息摘要 | varchar | 255 |  | √ | ' ' | 结息摘要 |
| 22 | fbatchno | 预提批次号 | varchar | 50 |  | √ | ' ' | 预提批次号 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fbegindate | 预提开始日 | timestamp | 0 |  |  | null | 预提开始日 |
| 25 | fdeposit | 存款积数 | numeric | 23 | 10 | √ | 0 | 存款积数 |
| 26 | foverdraft | 透支积数 | numeric | 23 | 10 | √ | 0 | 透支积数 |
| 27 | fintobjectid | 计息对象 | int8 | 64 |  | √ | 0 | 计息对象 ifm_intobject |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | finterestday | 预提日 | timestamp | 0 |  |  | null | 预提日 |
| 30 | fsettlecenterid | 结算中心 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 31 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand :手工新增 cim :投资管理 ifm :内部金融 |
| 32 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 33 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 34 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fcompanyid | 成员单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_preintbill |  | fbillno |
| 2 | pk_t_ifm_preintbill |  | fid |

---

## 内部利息预提单-关联追踪表 t_ifm_preintbill_tc

- **表名称：** 内部利息预提单-关联追踪表
- **表名：** t_ifm_preintbill_tc

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
| 1 | idx_ifm_preintbill_tc_tbill |  | ftbillid |
| 2 | idx_ifm_preintbill_tc_tid |  | ftid |
| 3 | idx_ifm_preintbill_tc_fid |  | ftbillid |
| 4 | pk_t_ifm_preintbill_tc |  | fid |

---

## 冲销明细-子表 t_ifm_preintbill_cur

- **表名称：** 冲销明细-子表
- **表名：** t_ifm_preintbill_cur

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrentintbillid | 结息记录编号 | int8 | 64 |  | √ | 0 | 内部利息结息单 ifm_currentintbill |
| 3 | fcurwriteoffamt | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 4 | fcurbookdate | 冲销日期 | timestamp | 0 |  |  | null | 冲销日期 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_preintbill_cur |  | fid |
| 2 | pk_t_ifm_preintbill_cur |  | fentryid |

---

## 内部利息预提单-反写记录表 t_ifm_preintbill_wb

- **表名称：** 内部利息预提单-反写记录表
- **表名：** t_ifm_preintbill_wb

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
| 1 | idx_t_ifm_preintbill_wb_fid |  | fid |
| 2 | pk_t_ifm_preintbill_wb |  | fentryid |

---

## 计息明细-子表 t_ifm_preintbill_entry

- **表名称：** 计息明细-子表
- **表名：** t_ifm_preintbill_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finstprincipal | 计息积数 | numeric | 23 | 10 | √ | 0 | 计息积数 |
| 3 | finststartdate | 预提开始日期 | timestamp | 0 |  |  | null | 预提开始日期 |
| 4 | finttype | 利息类型 | varchar | 50 |  | √ | ' ' | 利息类型,枚举: normal :存款利息 overdue :透支利息 |
| 5 | finstdays | 计息天数 | int8 | 64 |  | √ | 0 | 计息天数 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | finstenddate | 预提结束日期 | timestamp | 0 |  |  | null | 预提结束日期 |
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
| 1 | pk_t_ifm_preintbill_entry |  | fentryid |
| 2 | idx_ifm_preintbill_entry |  | fid |

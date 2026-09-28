# 应付利息预提-cfm_preinterestbill

## 应付利息预提-反写记录表 t_cfm_preinterestbill_wb

- **表名称：** 应付利息预提-反写记录表
- **表名：** t_cfm_preinterestbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 80 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 19 | 6 | √ | 0.000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_preinterestbill_wb_pkey |  | fentryid |
| 2 | idx_cfm_preinterestbill_wb |  | fid |

---

## 应付利息预提-主表 t_cfm_preinterestbill

- **表名称：** 应付利息预提-主表
- **表名：** t_cfm_preinterestbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwriteoffamt | 冲销金额 | numeric | 19 | 6 | √ | 0 | 冲销金额 |
| 3 | finsttype | 利率类型 | varchar | 80 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 4 | forgid | 借款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fchargeinstid | 冲销付息id | int8 | 64 |  | √ | 0 | 冲销付息id |
| 6 | flender | 贷款人 | varchar | 80 |  | √ | ' ' | 贷款人 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fprestenddate | 预提结束日期 | timestamp | 0 |  |  | null | 预提结束日期 |
| 9 | fcreditorid | 债权人id | int8 | 64 |  | √ | 0 | 债权人id |
| 10 | fbillno | 预提单编号 | varchar | 80 |  | √ | ' ' | 预提单编号 |
| 11 | fclientorgid | 受托机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 12 | ftextdebtor | 借款人(文本) | varchar | 80 |  | √ | ' ' | 借款人(文本) |
| 13 | flendernature | 贷款人性质 | varchar | 80 |  | √ | ' ' | 贷款人性质,枚举: outgroup :集团外 ingroup :集团内 |
| 14 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 15 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fbatchno | fbatchno | varchar | 30 |  | √ | ' ' |  |
| 17 | fproductfactoryid | fproductfactoryid | int8 | 64 |  | √ | 0 |  |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 20 | ftextcreditor | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 21 | fafterexpiredate | 展期后到期日期 | timestamp | 0 |  |  | null | 展期后到期日期 |
| 22 | fcreditortype | 债权人类型 | varchar | 50 |  | √ | ' ' | 债权人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 settlecenter :结算中心 custom :客商 other :其它 |
| 23 | fcontractbillno | 合同单据编号 | varchar | 80 |  | √ | ' ' | 合同单据编号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 26 | ffinorginfoid | 贷款人 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 27 | frecordstatus | 记账状态 | varchar | 80 |  | √ | ' ' | 记账状态,枚举: norecord :未记账 alrecord :已记账 |
| 28 | fwriteoffstatus | 冲销状态 | varchar | 80 |  | √ | ' ' | 冲销状态,枚举: part_writeoff :部分冲销 writeoff :已冲销 no_writeoff :未冲销 red_writeoff :红字冲销 |
| 29 | fnowriteoffamt | 剩余未冲销金额 | numeric | 19 | 6 | √ | 0 | 剩余未冲销金额 |
| 30 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | foperatetype | 操作类别 | varchar | 30 |  | √ | ' ' | 操作类别,枚举: preint :预提利息 reverseint :冲销预提利息 |
| 32 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 33 | fdrawamount | 提款金额 | numeric | 19 | 6 | √ | 0.000000 | 提款金额 |
| 34 | factpreinstamt | 实际预提利息 | numeric | 19 | 6 | √ | 0.000000 | 实际预提利息 |
| 35 | floandate | 放款日期 | timestamp | 0 |  |  | null | 放款日期 |
| 36 | fpostdate | fpostdate | timestamp | 0 |  |  | null |  |
| 37 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fcreatetime | 预提单创建时间 | timestamp | 0 |  |  | null | 预提单创建时间 |
| 39 | floanbillno | 提款单编号 | varchar | 80 |  | √ | ' ' | 提款单编号 |
| 40 | fwriteoffpreintbillid | 被冲销预提单id | int8 | 64 |  | √ | 0 | 被冲销预提单id |
| 41 | fprestartdate | 预提开始日期 | timestamp | 0 |  |  | null | 预提开始日期 |
| 42 | finstschemeid | 结息方案 | int8 | 64 |  | √ | 0 | [结息计划方案 cfm_inscheme](../cfm_files/cfm_inscheme.md) |
| 43 | fcontractno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 44 | fsettlecenterid | fsettlecenterid | int8 | 64 |  | √ | 0 |  |
| 45 | floanorgid | 贷款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fnotrepayamt | 未还本金 | numeric | 19 | 6 | √ | 0.000000 | 未还本金 |
| 47 | floantype | 贷款类型 | varchar | 80 |  | √ | ' ' | 贷款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券发行 |
| 48 | fbizdate | 预提日期 | timestamp | 0 |  |  | null | 预提日期 |
| 49 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 50 | fpredictpreinstamt | 测算预提利息 | numeric | 19 | 6 | √ | 0.000000 | 测算预提利息 |
| 51 | fcurrencyid | 借款币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_preinstbill |  | fbillno,fbillstatus |
| 2 | t_cfm_preinterestbill_pkey |  | fid |

---

## 应付利息预提-分表 t_cfm_preinterestbill_e

- **表名称：** 应付利息预提-分表
- **表名：** t_cfm_preinterestbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreditorgid | 债权人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdebtorid | 借款人id | int8 | 64 |  | √ | 0 | 借款人id |
| 4 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 ifm :内部金融管理 bond :债券 |
| 5 | fdebtortype | 借款人类型 | varchar | 30 |  | √ | ' ' | 借款人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 custom :客商 other :其它 |
| 6 | fauto | 自动预提 | bpchar | 1 |  | √ | '0' | 自动预提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_preinterestbill_e |  | fid |
| 2 | idx_cfm_preinterestbill_e |  | fdebtorid |

---

## 利息预算明细-子表 t_cfm_preinstbill_entrys

- **表名称：** 利息预算明细-子表
- **表名：** t_cfm_preinstbill_entrys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frate | 利率(%) | numeric | 23 | 10 | √ | 0 | 利率(%) |
| 3 | finststartdate | 计息开始日 | timestamp | 0 |  |  | null | 计息开始日 |
| 4 | finstdays | 计息天数 | int8 | 64 |  | √ | 0 | 计息天数 |
| 5 | fratetrandays | 利率转换天数 | int8 | 64 |  | √ | 0 | 利率转换天数 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | finstenddate | 计息结束日 | timestamp | 0 |  |  | null | 计息结束日 |
| 8 | finstprincipalamt | 计息本金 | numeric | 19 | 6 | √ | 0.000000 | 计息本金 |
| 9 | finstamt | 利息金额 | numeric | 19 | 6 | √ | 0.000000 | 利息金额 |
| 10 | finstctg | 利息类别 | varchar | 80 |  | √ | ' ' | 利息类别,枚举: normal :正常利息 extend :展期利息 overdue :逾期利息 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_preinstbill_entrys_pkey |  | fentryid |
| 2 | idx_cfm_preinstbill_entrys |  | fid |

---

## 关联子实体-子表 t_cfm_preinterestbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cfm_preinterestbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_preinterestbill_lk_pkey |  | fpkid |
| 2 | idx_cfm_preinterestbill_lk |  | fid |

---

## 应付利息预提-关联追踪表 t_cfm_preinterestbill_tc

- **表名称：** 应付利息预提-关联追踪表
- **表名：** t_cfm_preinterestbill_tc

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
| 1 | idx_cfm_preinterestbill_tc_tbill |  | ftbillid |
| 2 | t_cfm_preinterestbill_tc_pkey |  | fid |
| 3 | idx_cfm_preinterestbill_tc |  | ftbillid |
| 4 | idx_cfm_preinterestbill_tc_tid |  | ftid |

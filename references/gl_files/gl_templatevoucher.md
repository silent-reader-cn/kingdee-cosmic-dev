# 模式凭证-gl_templatevoucher

## 模式凭证-主表 t_gl_templatevoucher

- **表名称：** 模式凭证-主表
- **表名：** t_gl_templatevoucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fgroupid | 模式凭证类别 | int8 | 64 |  | √ | 0 | 模式凭证类别 gl_templatevouchergroup |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 8 | fdescription | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 9 | fbookstypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 10 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 11 | fexratedataid | fexratedataid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | ftypeid | 凭证字 | int8 | 64 |  | √ | 0 | 凭证字 gl_vouchertype |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fattachments | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 16 | fcreatorid | 制单 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | floccurrency | 组织本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fapplytype | 适用范围 | bpchar | 1 |  | √ | '1' | 适用范围,枚举: 0 :手工凭证 |
| 23 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_templatevoucher |  | forgid |
| 2 | t_gl_templatevoucher_pkey |  | fid |

---

## 模式凭证-多语言表 t_gl_templatevoucher_l

- **表名称：** 模式凭证-多语言表
- **表名：** t_gl_templatevoucher_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_templatevoucher_l |  | fid,flocaleid |
| 2 | t_gl_templatevoucher_l_pkey |  | fpkid |

---

## 单据体-子表 t_gl_templatevoucherentry

- **表名称：** 单据体-子表
- **表名：** t_gl_templatevoucherentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foriginalcredit | 原币贷方 | numeric | 19 | 6 | √ | 0.000000 | 原币贷方 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | foriginalamount | 原币金额 | numeric | 19 | 6 | √ | 0.000000 | 原币金额 |
| 5 | fmaincfamount | 主表项目金额 | numeric | 19 | 6 | √ | 0.000000 | 主表项目金额 |
| 6 | fmaincfassgrpid | 主表核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 7 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 8 | fentrydc | 分录方向 | varchar | 2 |  | √ | '0' | 分录方向,枚举: 1 :借 -1 :贷 |
| 9 | freportingdebit | 报告币借方 | numeric | 19 | 6 | √ | 0.000000 | 报告币借方 |
| 10 | flocaldebit | 借方 | numeric | 19 | 6 | √ | 0.000000 | 借方 |
| 11 | flocalcredit | 贷方 | numeric | 19 | 6 | √ | 0.000000 | 贷方 |
| 12 | freportingamount | 报告币金额 | numeric | 19 | 6 | √ | 0.000000 | 报告币金额 |
| 13 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 14 | fsuppcfamount | 附表项目金额 | numeric | 19 | 6 | √ | 0.000000 | 附表项目金额 |
| 15 | fdebitlocalcomb | 借方 | bpchar | 1 |  | √ | '1' | 借方,枚举: 0 :金额 1 :税额 2 :价税合计 |
| 16 | flocalamount | 本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 本位币金额 |
| 17 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 18 | fmaincfitemid | 主表项目 | int8 | 64 |  | √ | 0 | 现金流量项目 gl_cashflowitem |
| 19 | freportexchangerate | 报告币汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 报告币汇率 |
| 20 | freportingcredit | 报告币贷方 | numeric | 19 | 6 | √ | 0.000000 | 报告币贷方 |
| 21 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 22 | flocalexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 23 | fsuppcfitemid | 附表项目 | int8 | 64 |  | √ | 0 | 现金流量项目 gl_cashflowitem |
| 24 | fcreditlocalcomb | 贷方 | bpchar | 1 |  | √ | '1' | 贷方,枚举: 0 :金额 1 :税额 2 :价税合计 |
| 25 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | foriginaldebit | 原币借方 | numeric | 19 | 6 | √ | 0.000000 | 原币借方 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_templatevoucherentry |  | fid |
| 2 | t_gl_templatevoucherentry_pkey |  | fentryid |

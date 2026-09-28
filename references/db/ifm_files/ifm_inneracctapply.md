# 内部账户开户申请单-ifm_inneracctapply

## 内部账户开户申请单-反写记录表 t_ifm_inneracctapply_wb

- **表名称：** 内部账户开户申请单-反写记录表
- **表名：** t_ifm_inneracctapply_wb

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
| 1 | t_ifm_inneracctapply_wb_pkey |  | fentryid |
| 2 | idx_ifm_inneracctap_wb_fid |  | fid |

---

## 内部账户开户申请单-主表 t_ifm_inneracctapply

- **表名称：** 内部账户开户申请单-主表
- **表名：** t_ifm_inneracctapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcenteracctdlftid | 默认中心账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 4 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmgrfee | 账户管理费 | numeric | 19 | 6 | √ | 0.000000 | 账户管理费 |
| 6 | ffinorgid | 开户行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | faccttype | 账户类型 | varchar | 30 |  | √ | ' ' | 账户类型,枚举: basic :基本存款账户 normal :一般存款账户 temp :临时存款账户 spcl :专用存款账户 fgn_curr :经常项目外汇账户 fng_fin :资本项目外汇账户 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fname | 账户名称 | varchar | 80 |  | √ | ' ' | 账户名称 |
| 13 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 H :已受理 C :已审核 E :已生成 |
| 14 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fopendate | 开户日期 | timestamp | 0 |  |  | null | 开户日期 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | freason | 开户原因和其他开户要求 | varchar | 255 |  | √ | ' ' | 开户原因和其他开户要求 |
| 20 | fcurrencymgrfeeid | 账户管理费币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fmgrstratgid | 账户管理策略 | int8 | 64 |  | √ | 0 | 账户管理策略 am_strategy |
| 22 | facctusageid | 账户用途 | int8 | 64 |  | √ | 0 | 账户用途 bd_acctpurpose |
| 23 | feasycode | 助记码 | varchar | 30 |  | √ | ' ' | 助记码 |
| 24 | facctprop | 账户性质 | varchar | 30 |  | √ | ' ' | 账户性质,枚举: in_out :收支户 in :收入户 out :支出户 |
| 25 | fnumber | 账号 | varchar | 80 |  | √ | ' ' | 账号 |
| 26 | fcurrencydlftid | 默认币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fcompanyid | 申请公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ifm_inneracctapply_pkey |  | fid |
| 2 | idx_t_ifm_inneracctapply_num |  | fnumber |

---

## 内部账户开户申请单-关联追踪表 t_ifm_inneracctapply_tc

- **表名称：** 内部账户开户申请单-关联追踪表
- **表名：** t_ifm_inneracctapply_tc

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
| 1 | idx_ifm_inneracctapply_tc_tbill |  | ftbillid |
| 2 | idx_ifm_inneracctap_tc_fid |  | ftbillid |
| 3 | t_ifm_inneracctapply_tc_pkey |  | fid |
| 4 | idx_ifm_inneracctapply_tc_tid |  | ftid |

---

## 币别-多选基础资料表 t_ifm_inneracctapply_cr

- **表名称：** 币别-多选基础资料表
- **表名：** t_ifm_inneracctapply_cr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ifm_inneracctapply_cr_pkey |  | fpkid |
| 2 | idx_ifm_inneracctap_cr_fid |  | fid |

---

## 关联子实体-子表 t_ifm_inneracctapply_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_inneracctapply_lk

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
| 1 | idx_ifm_inneracctap_lk_fid |  | fid |
| 2 | t_ifm_inneracctapply_lk_pkey |  | fpkid |

---

## 内部账户开户申请单-多语言表 t_ifm_inneracctapply_l

- **表名称：** 内部账户开户申请单-多语言表
- **表名：** t_ifm_inneracctapply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 账户名称 | varchar | 80 |  | √ | ' ' | 账户名称 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ifm_inneracctapply_l_fid |  | fid,flocaleid |
| 2 | t_ifm_inneracctapply_l_pkey |  | fpkid |

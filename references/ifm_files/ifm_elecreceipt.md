# 内部电子回单查询-ifm_elecreceipt

## 内部电子回单查询-关联追踪表 t_bei_elecreceipt_tc

- **表名称：** 内部电子回单查询-关联追踪表
- **表名：** t_bei_elecreceipt_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bei_elecreceipt_tc |  | fid |
| 2 | idx_bei_elecreceipt_tc_tid |  | ftid |
| 3 | idx_bei_elecreceipt_tc_tbill |  | ftbillid |

---

## 内部电子回单查询-反写记录表 t_bei_elecreceipt_wb

- **表名称：** 内部电子回单查询-反写记录表
- **表名：** t_bei_elecreceipt_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bei_elecreceipt_wb |  | fentryid |
| 2 | idx_bei_elecreceipt_wb_fk |  | fid |

---

## 内部电子回单查询-多语言表 t_bei_elecreceipt_l

- **表名称：** 内部电子回单查询-多语言表
- **表名：** t_bei_elecreceipt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 100 |  | √ | ' ' | localeid |
| 3 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_elecreceipt_l_pkey |  | fpkid |
| 2 | idx_bei_elecreceipt_l |  | fid,flocaleid,fdescription |

---

## 内部电子回单查询-分表 t_bei_elecreceipt_e

- **表名称：** 内部电子回单查询-分表
- **表名：** t_bei_elecreceipt_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecname | 收款人名称 | varchar | 100 |  | √ | ' ' | 收款人名称 |
| 3 | fscorgid | 结算中心组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | frecbankname | 收方开户银行名称 | varchar | 100 |  | √ | ' ' | 收方开户银行名称 |
| 5 | frecno | 收方账号 | varchar | 80 |  | √ | ' ' | 收方账号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_bei_elecreceipt_e |  | frecno |
| 2 | t_bei_elecreceipt_e_pkey |  | fid |
| 3 | index_bei_elecrec_e_org |  | fscorgid |

---

## 内部电子回单查询-主表 t_bei_elecreceipt

- **表名称：** 内部电子回单查询-主表
- **表名：** t_bei_elecreceipt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftcpurl | ftcpurl | varchar | 100 |  | √ | ' ' |  |
| 3 | fcreditdebitflag | 借贷标记 | varchar | 100 |  | √ | ' ' | 借贷标记,枚举: 1 :出账 2 :入账 |
| 4 | fbankcheckflag | 对账标识码 | varchar | 255 |  | √ | ' ' | 对账标识码 |
| 5 | foppunit | 对方单位 | varchar | 255 |  | √ | ' ' | 对方单位 |
| 6 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | ffileserverurl | ffileserverurl | varchar | 100 |  | √ | ' ' |  |
| 8 | ftransnetcode | ftransnetcode | varchar | 100 |  | √ | ' ' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsortno | 排序号 | varchar | 100 |  | √ | ' ' | 排序号 |
| 11 | fuploadfilename | fuploadfilename | varchar | 500 |  | √ | ' ' |  |
| 12 | foppbanknumber | 对方银行账号 | varchar | 255 |  | √ | ' ' | 对方银行账号 |
| 13 | fdetailid | 交易流水号 | varchar | 100 |  | √ | ' ' | 交易流水号 |
| 14 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 15 | freceiptno | 电子回单号 | varchar | 100 |  | √ | ' ' | 电子回单号 |
| 16 | fismatch | 匹配交易明细 | bpchar | 1 |  | √ | '0' | 匹配交易明细 |
| 17 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fproxy | fproxy | varchar | 100 |  | √ | ' ' |  |
| 19 | fcreditamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 20 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 21 | fdebitamount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 22 | fbankname | 付方开户银行名称 | varchar | 100 |  | √ | ' ' | 付方开户银行名称 |
| 23 | fport | fport | int8 | 64 |  | √ | 0 |  |
| 24 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: frombank :银企接口 import :模板引入 modify :系统修复 image :图片引入 fromifm :结算中心 |
| 25 | ffileflag | 是否文件 | bpchar | 1 |  | √ | '0' | 是否文件 |
| 26 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 27 | ftransdetailid | 内部交易明细id | int8 | 64 |  | √ | 0 | 内部交易明细id |
| 28 | faccountbankid | 内部账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 29 | fcompanyid | 成员单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fhost | fhost | varchar | 100 |  | √ | ' ' |  |
| 31 | fcompleteflag | fcompleteflag | bpchar | 1 |  | √ | '0' |  |
| 32 | foppbank | 对方开户银行 | varchar | 255 |  | √ | ' ' | 对方开户银行 |
| 33 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 34 | fpassword | fpassword | varchar | 100 |  | √ | ' ' |  |
| 35 | fbizrefno | 业务参考号 | varchar | 100 |  | √ | ' ' | 业务参考号 |
| 36 | faccno | 付方账号 | varchar | 80 |  | √ | ' ' | 付方账号 |
| 37 | fuse | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 38 | fusername | fusername | varchar | 100 |  | √ | ' ' |  |
| 39 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 1 :普通 2 :上划 3 :下拨 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | ftranstellno | ftranstellno | varchar | 100 |  | √ | ' ' |  |
| 42 | fvalidcode | fvalidcode | varchar | 100 |  | √ | ' ' |  |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | ffinancialtypeid | ffinancialtypeid | int8 | 64 |  | √ | 0 |  |
| 46 | faccname | 付款人名称 | varchar | 100 |  | √ | ' ' | 付款人名称 |
| 47 | foppbankname | 对方银行账号名称 | varchar | 100 |  | √ | ' ' | 对方银行账号名称 |
| 48 | fprintcount | 打印次数 | int8 | 64 |  | √ | 0 | 打印次数 |
| 49 | fbizdate | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 50 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 51 | fdetaildatetime | 明细交易时间 | timestamp | 0 |  |  | null | 明细交易时间 |
| 52 | ffilepath | ffilepath | varchar | 500 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_elecreceipt_pkey |  | fid |
| 2 | idx_bei_elecreceipt |  | fcompanyid,faccountbankid,fcurrencyid,fbizdate |

---

## 关联子实体-子表 t_bei_elecreceipt_lk

- **表名称：** 关联子实体-子表
- **表名：** t_bei_elecreceipt_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_elecreceipt_lk_fk |  | fid |
| 2 | pk_bei_elecreceipt_lk |  | fpkid |

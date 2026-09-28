# 电票交易查询-cdm_banklog

## 电票交易查询-多语言表 t_bei_banklog_l

- **表名称：** 电票交易查询-多语言表
- **表名：** t_bei_banklog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | fcomment | fcomment | varchar | 255 |  |  | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_banklog_l |  | fid,flocaleid,fcomment |
| 2 | t_bei_banklog_l_pkey |  | fpkid |

---

## 电票交易查询-使用范围位图表 t_bei_banklog_m

- **表名称：** 电票交易查询-使用范围位图表
- **表名：** t_bei_banklog_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_banklog_m |  | forgid |

---

## 电票交易查询-使用范围表 t_bei_banklog_u

- **表名称：** 电票交易查询-使用范围表
- **表名：** t_bei_banklog_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_banklog_u_uo |  | fuseorgid |
| 2 | pk_t_bei_banklog_u |  | fdataid,fuseorgid |

---

## 电票交易查询-主表 t_bei_banklog

- **表名称：** 电票交易查询-主表
- **表名：** t_bei_banklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | fexceptionmsg | text | 0 |  |  | null |  |
| 3 | fopenorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbanklogtype | 执行任务 | varchar | 30 |  | √ | ' ' | 执行任务,枚举: queryNotePayable :应付票据查询 queryNoteReceivable :应收票据查询 notePayable_remit_register :开票登记 notePayable_remit_revocation :撤销出票 notePayable_remit_accept :提示承兑 notePayable_remit_receive :提示收票 noteReceivable_note_endorse :票据背书 noteReceivable_note_discount :票据贴现 noteReceivable_note_signin :票据通用签收 noteReceivable_pledge_note :票据质押 noteReceivable_remove_pledge :票据解除质押 noteReceivable_note_cancle :票据通用撤销 |
| 5 | fsourceid | 主键ID | varchar | 100 |  | √ | ' ' | 主键ID |
| 6 | fbizexceptioninfo_tag | fbizexceptioninfo_tag | text | 0 |  |  | null |  |
| 7 | fsrcbizid | fsrcbizid | int8 | 64 |  | √ | 0 |  |
| 8 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fbankinterface | fbankinterface | varchar | 100 |  | √ | ' ' |  |
| 12 | fsendexceptioninfo | fsendexceptioninfo | text | 0 |  |  | null |  |
| 13 | fbizexceptioninfo | fbizexceptioninfo | text | 0 |  |  | null |  |
| 14 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 15 | fenablerid | fenablerid | int8 | 64 |  | √ | 0 |  |
| 16 | freceiveinfo | 返回时电票状态 | text | 0 |  |  | null | 返回时电票状态 |
| 17 | freceiveinfo_tag | freceiveinfo_tag | text | 0 |  |  | null |  |
| 18 | fsourcebillno | 票据号码 | varchar | 100 |  | √ | ' ' | 票据号码 |
| 19 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 20 | fsourcebilltype | 业务单据 | varchar | 30 |  | √ | ' ' | 业务单据,枚举: |
| 21 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 22 | faccountbank | 银行账户 | varchar | 30 |  | √ | ' ' | 银行账户 |
| 23 | fbankinterfaceid | fbankinterfaceid | varchar | 100 |  | √ | ' ' |  |
| 24 | fsendinfo | 请求时电票状态 | text | 0 |  |  | null | 请求时电票状态 |
| 25 | ftranstype | ftranstype | varchar | 30 |  | √ | ' ' |  |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
| 28 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 29 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fbankpaystate | fbankpaystate | varchar | 30 |  | √ | 'OP' |  |
| 31 | fpaycurrencyid | fpaycurrencyid | int8 | 64 |  | √ | 0 |  |
| 32 | fstatus | fstatus | bpchar | 5 |  | √ | '0' |  |
| 33 | fsendinfo_tag | fsendinfo_tag | text | 0 |  |  | null |  |
| 34 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 35 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 36 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 37 | fpaytotalamt | fpaytotalamt | numeric | 19 | 6 | √ | 0 |  |
| 38 | fisexception | 执行结果 | varchar | 30 |  | √ | ' ' | 执行结果,枚举: 0 :成功 1 :失败 |
| 39 | fexecutorid | fexecutorid | int8 | 64 |  | √ | 0 |  |
| 40 | ftime | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 41 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 42 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 43 | fsendexceptioninfo_tag | fsendexceptioninfo_tag | text | 0 |  |  | null |  |
| 44 | fcomment | fcomment | varchar | 255 |  |  | ' ' |  |
| 45 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 46 | fpayeeacnt | fpayeeacnt | varchar | 100 |  | √ | ' ' |  |
| 47 | fenabledate | fenabledate | timestamp | 0 |  |  | null |  |
| 48 | freceiveexceptioninfo_tag | freceiveexceptioninfo_tag | text | 0 |  |  | null |  |
| 49 | freceiveexceptioninfo | freceiveexceptioninfo | text | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_banklog_pkey |  | fid |
| 2 | idx_bei_banklog_no |  | fsourcebillno |
| 3 | idx_bei_banklog |  | fcompanyid,ftime,fisexception |
| 4 | idx_t_bei_banklog_master |  | fmasterid |
| 5 | idx_bei_banklog_sidb |  | fsrcbizid,fbanklogtype |
| 6 | idx_bei_banklog_time |  | ftime |
| 7 | idx_t_bei_banklog_createorg |  | fcreateorgid |

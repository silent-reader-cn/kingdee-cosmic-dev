# 母子账户组（F7以母子账户组及母账户信息维度）-fca_acctgroup_inh

## 母子账户组（F7以母子账户组及母账户信息维度）-多语言表 t_fca_acctgroup_l

- **表名称：** 母子账户组（F7以母子账户组及母账户信息维度）-多语言表
- **表名：** t_fca_acctgroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 256 |  | √ | ' ' | 备注 |
| 4 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fca_acctgroup_l |  | fid,flocaleid |
| 2 | t_fca_acctgroup_l_pkey |  | fpkid |

---

## 子账户信息-子表 t_fca_acctgroup_entrys

- **表名称：** 子账户信息-子表
- **表名：** t_fca_acctgroup_entrys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftranstrategyid | 账户划拨策略 | int8 | 64 |  | √ | 0 | [账户划拨策略 fca_transtrategy](../fca_files/fca_transtrategy.md) |
| 3 | ftwolinetype | 两条线类别 | varchar | 50 |  | √ | '0' | 两条线类别,枚举: 0 :默认值 1 :收入户页签 2 :支出户页签 |
| 4 | fentrybankacctid | 银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fautotransupid | 自动上划设置 | int8 | 64 |  | √ | 0 | [自动划拨设置 fca_autotrans](../fca_files/fca_autotrans.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | finneracctid | 对应内部账号 | int8 | 64 |  | √ | 0 | [内部账户管理 ifm_inneracct](../ifm_files/ifm_inneracct.md) |
| 9 | fautotransdownid | 自动下拨设置 | int8 | 64 |  | √ | 0 | [自动划拨设置 fca_autotrans](../fca_files/fca_autotrans.md) |
| 10 | fcompanyid | 成员单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fca_acctgroup_entrys |  | fentrybankacctid |
| 2 | t_fca_acctgroup_entrys_pkey |  | fentryid |

---

## 母子账户组（F7以母子账户组及母账户信息维度）-主表 t_fca_acctgroup

- **表名称：** 母子账户组（F7以母子账户组及母账户信息维度）-主表
- **表名：** t_fca_acctgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 4 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [母子账户组（F7以母子账户组及母账户信息维度） fca_acctgroup_inh](../fca_files/fca_acctgroup_inh.md) |
| 7 | fcomment | 备注 | varchar | 256 |  | √ | ' ' | 备注 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 10 | flongnumber | 长编码 | varchar | 80 |  | √ | ' ' | 长编码 |
| 11 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 12 | facctctlmode | 账户管理模式 | varchar | 80 |  | √ | ' ' | 账户管理模式 |
| 13 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 14 | fstatus | 数据状态 | varchar | 80 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fentrybankcount | 母账户下属子账户数 | int8 | 64 |  | √ | 0 | 母账户下属子账户数 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fenable | 使用状态 | varchar | 80 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fmanagemode | 账户管理模式单选 | varchar | 80 |  | √ | ' ' | 账户管理模式单选,枚举: portal_acct :收支一条线 income_twoline :收支两条线 |
| 21 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | faccountbankid | 银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 23 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_acctgroup_pkey |  | fid |
| 2 | idx_fca_acctgroup |  | fcompanyid,faccountbankid |

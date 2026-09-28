# 收入规则-tcvat_rule_income

## 增值税专用发票不含税收入-子表 t_tcvat_income_entry

- **表名称：** 增值税专用发票不含税收入-子表
- **表名：** t_tcvat_income_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 3 | ftable12 | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 4 | ftaxrate | 税率/征收率 | varchar | 30 |  | √ | ' ' | 税率/征收率 |
| 5 | famountfield12 | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 8 | fabsolute12 | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 9 | fdatadirection12 | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 10 | fdifferenceinvoice | 差额发票标识 | bpchar | 1 |  | √ | '0' | 差额发票标识 |
| 11 | fdatatype12 | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 sehshsj :税额换算含税价 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_income_entry |  | fid |
| 2 | t_tcvat_income_entry_pkey |  | fentryid |

---

## 税收业务分类-多选基础资料表 t_tcvat_rule_taxrate

- **表名称：** 税收业务分类-多选基础资料表
- **表名：** t_tcvat_rule_taxrate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 18 |  | √ | ' ' | 税收分类编码表 tpo_tcvat_taxrateentry |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_rule_taxrate_pkey |  | fpkid |
| 2 | idx_tcvat_rule_taxrate_fk |  | fid |

---

## 其他发票税额取数规则-子表 t_tcvat_rule_inc_qtse

- **表名称：** 其他发票税额取数规则-子表
- **表名：** t_tcvat_rule_inc_qtse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratejson | 汇率转换 | varchar | 255 |  | √ | ' ' | 汇率转换 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 6 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 7 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 8 | fvatrate | 增值税税率/征收率 | numeric | 23 | 10 | √ | 0 | 增值税税率/征收率 |
| 9 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 10 | fdifferenceinvoice | 差额发票标识 | bpchar | 1 |  | √ | '0' | 差额发票标识 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 13 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 14 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 hsjhsse :含税价换算税额 bhsjhsse :不含税价换算税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_rule_inc_qtse_fk |  | fid |
| 2 | pk_tcvat_rule_inc_qtse |  | fentryid |

---

## 未开票税额取数配置-子表 t_tcvat_rule_inc_wkpse

- **表名称：** 未开票税额取数配置-子表
- **表名：** t_tcvat_rule_inc_wkpse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratejson | 汇率转换 | varchar | 255 |  | √ | ' ' | 汇率转换 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 6 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 7 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 8 | fvatrate | 增值税税率/征收率 | numeric | 23 | 10 | √ | 0 | 增值税税率/征收率 |
| 9 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 10 | fdifferenceinvoice | 差额发票标识 | bpchar | 1 |  | √ | '0' | 差额发票标识 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 13 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 14 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 hsjhsse :含税价换算税额 bhsjhsse :不含税价换算税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_rule_inc_wkpse_fk |  | fid |
| 2 | pk_tcvat_rule_inc_wkpse |  | fentryid |

---

## 未开票不含税收入取数配置-子表 t_tcvat_rule_entry

- **表名称：** 未开票不含税收入取数配置-子表
- **表名：** t_tcvat_rule_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | fentryentityconf | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 4 | fexratejson | 汇率转换 | varchar | 255 |  | √ | ' ' | 汇率转换 |
| 5 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 8 | fentryentityconfjson | 增值税税率/征收率 | varchar | 2000 |  | √ | ' ' | 增值税税率/征收率 |
| 9 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 10 | fvatrate | fvatrate | numeric | 23 | 10 | √ | 0 |  |
| 11 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 12 | fiscustomtable | fiscustomtable | bpchar | 1 |  | √ | ' ' |  |
| 13 | fdifferenceinvoice | 差额发票标识 | bpchar | 1 |  | √ | '0' | 差额发票标识 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 16 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 17 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 sehshsj :税额换算含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_rule_entry_pkey |  | fentryid |
| 2 | idx_tcvat_rule_entry |  | fid |

---

## 其他发票不含税收入取数规则-子表 t_tcvat_rule_inc_qtbhs

- **表名称：** 其他发票不含税收入取数规则-子表
- **表名：** t_tcvat_rule_inc_qtbhs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratejson | 汇率转换 | varchar | 255 |  | √ | ' ' | 汇率转换 |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 6 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 7 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 8 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 9 | fdifferenceinvoice | 差额发票标识 | bpchar | 1 |  | √ | '0' | 差额发票标识 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 12 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 13 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 sehshsj :税额换算含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_rule_inc_qtbhs_fk |  | fid |
| 2 | pk_tcvat_rule_inc_qtbhs |  | fentryid |

---

## 增值税专用发票税额取数-子表 t_tcvat_income_tax_entry

- **表名称：** 增值税专用发票税额取数-子表
- **表名：** t_tcvat_income_tax_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratejson2 | 汇率转换 | varchar | 256 |  | √ | ' ' | 汇率转换 |
| 3 | fconditionjson2 | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizname2 | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 6 | famountfield2 | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 7 | fdifferenceinvoice2 | 差额发票标识 | bpchar | 1 |  | √ | '0' | 差额发票标识 |
| 8 | fdatatype2 | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 hsjhsse :含税价换算税额 bhsjhsse :不含税价换算税额 |
| 9 | fabsolute2 | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 10 | ftable2 | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 11 | ffiltercondition2 | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fvatrate2 | 增值税税率/征收率 | numeric | 23 | 10 | √ | 0 | 增值税税率/征收率 |
| 14 | fdatadirection2 | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_income_tax_entry |  | fentryid |
| 2 | idx_tcvat_income_tax_entry_fk |  | fid |

---

## 收入规则-多语言表 t_tcvat_rule_income_l

- **表名称：** 收入规则-多语言表
- **表名：** t_tcvat_rule_income_l

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
| 1 | idx_tcvat_rule_income_l_0 |  | fid,flocaleid |
| 2 | t_tcvat_rule_income_l_pkey |  | fpkid |

---

## 收入规则-主表 t_tcvat_rule_income

- **表名称：** 收入规则-主表
- **表名：** t_tcvat_rule_income

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxrate | ftaxrate | varchar | 30 |  | √ | ' ' |  |
| 3 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fruletype | 规则类型 | varchar | 30 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 5 | ftaxation | ftaxation | varchar | 30 |  | √ | ' ' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fjzjt | 即征即退业务 | varchar | 30 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 |
| 8 | finvoiceseqs | 配置税额取数 | bpchar | 1 |  | √ | '0' | 配置税额取数 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftaxationstr | 征收方式文本 | varchar | 400 |  | √ | ' ' | 征收方式文本 |
| 13 | ftaxrateid | 税率/征收率 | int8 | 64 |  | √ | 0 | 税率模板 tpo_tcvat_taxrates |
| 14 | ftaxpayertype | 适用纳税人类型 | varchar | 30 |  | √ | ' ' | 适用纳税人类型,枚举: ybnsr :一般纳税人 xgmnsr :小规模纳税人 |
| 15 | fdeductiontype | 免税项目代码及名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 16 | fwkpseqs | 配置税额取数 | bpchar | 1 |  | √ | '0' | 配置税额取数 |
| 17 | ftaxationid | 征收方式 | int8 | 64 |  | √ | 0 | 征收方式模板 tpo_tcvat_taxperiod |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fiswkpwscl | 尾数处理 | bpchar | 1 |  | √ | '0' | 尾数处理 |
| 21 | ftaxratestr | 税率文本 | varchar | 400 |  | √ | ' ' | 税率文本 |
| 22 | fqtfpseqs | 配置税额取数 | bpchar | 1 |  | √ | '0' | 配置税额取数 |
| 23 | fexporting | 出口业务 | varchar | 50 |  | √ | ' ' | 出口业务,枚举: 1 :是 0 :否 |
| 24 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 26 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_rule_income |  | fnumber |
| 2 | t_tcvat_rule_income_pkey |  | fid |

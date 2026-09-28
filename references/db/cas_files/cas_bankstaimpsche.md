# 银行对账单导入方案-cas_bankstaimpsche

## 银行对账单导入方案-多语言表 t_cas_bankstaimpsche_l

- **表名称：** 银行对账单导入方案-多语言表
- **表名：** t_cas_bankstaimpsche_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocationinfile | 银行账号在文件所在位置 | varchar | 100 |  | √ | ' ' | 银行账号在文件所在位置 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_bsisl_fpid |  | fid,flocaleid |
| 2 | pk_t_cas_bankstaimpsche_l |  | fpkid |

---

## 银行对账单字段列表(实体)-子表 t_cas_bankstaimpsche_e

- **表名称：** 银行对账单字段列表(实体)-子表
- **表名：** t_cas_bankstaimpsche_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcategory | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 1 :主要 2 :次要 |
| 3 | fbillfield | 单据字段标识 | varchar | 100 |  | √ | ' ' | 单据字段标识 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ffieldrule | 取数规则 | int8 | 64 |  | √ | 0 | [银行对账单字段取数规则 cas_bankstafieldrule](../cas_files/cas_bankstafieldrule.md) |
| 6 | fmustrecord | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 7 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 8 | fcolumnname | 文件列名（预置） | varchar | 500 |  | √ | ' ' | 文件列名（预置） |
| 9 | fbillfieldname | 单据字段 | varchar | 200 |  | √ | ' ' | 单据字段 |
| 10 | fcondition | 适用情形 | varchar | 100 |  | √ | ' ' | 适用情形 |
| 11 | fcolumnname2 | 文件列名补充2 | varchar | 100 |  | √ | ' ' | 文件列名补充2 |
| 12 | fcolumnname1 | 文件列名补充1 | varchar | 100 |  | √ | ' ' | 文件列名补充1 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcolumnname3 | 文件列名补充3 | varchar | 100 |  | √ | ' ' | 文件列名补充3 |
| 15 | fisshow | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_bsise_fid |  | fid |
| 2 | pk_cas_bankstaimpsche_e |  | fentryid |

---

## 银行对账单字段列表(实体)-多语言表 t_cas_bankstaimpsche_e_l

- **表名称：** 银行对账单字段列表(实体)-多语言表
- **表名：** t_cas_bankstaimpsche_e_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbillfieldname | 单据字段 | varchar | 255 |  | √ | ' ' | 单据字段 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_bsisee_l_fid |  | fentryid,flocaleid |
| 2 | pk_cas_bankstaimpsche_e_l |  | fpkid |

---

## 银行对账单导入方案-主表 t_cas_bankstaimpsche

- **表名称：** 银行对账单导入方案-主表
- **表名：** t_cas_bankstaimpsche

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 4 | funiquefiled | 数据替换规则的唯一值 | varchar | 500 |  | √ | ' ' | 数据替换规则的唯一值,枚举: accountbank :银行账户 currency :币别 bizdate :日期 description :摘要 debitamount :借方金额 creditamount :贷方金额 balanceamt :余额 settlementtype :结算方式 settlementnumber :结算号 oppunitname :对方户名 oppaccountnumber :对方账号 oppbank :对方开户行 sequencenumber :排序号 tradenumber :业务参考号 bankcheckflag :对账标识码 bankvouvherno :明细流水号 transtime :交易时间 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | flocationinfile | 银行账号在文件所在位置 | varchar | 50 |  | √ | ' ' | 银行账号在文件所在位置 |
| 7 | fschemaid | 预置银行方案id | int8 | 64 |  | √ | 0 | 预置银行方案id |
| 8 | fispreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fdefaultschema | 默认方案 | bpchar | 1 |  | √ | '0' | 默认方案 |
| 14 | fprebankschema | 是否预制银行方案 | bpchar | 1 |  | √ | '0' | 是否预制银行方案 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 17 | fdesc | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 18 | fbankid | 银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 19 | fbanktype | 银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cas_scheme_fbankid |  | fbankid |
| 2 | pk_cas_bankstaimpsche |  | fid |
| 3 | idx_cas_scheme_fname |  | fname |
| 4 | idx_cas_scheme_fnumber |  | fnumber |

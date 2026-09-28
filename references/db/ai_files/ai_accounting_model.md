# AI记账模型-ai_accounting_model

## 适用账簿-多选基础资料表 t_ai_accounting_book

- **表名称：** 适用账簿-多选基础资料表
- **表名：** t_ai_accounting_book

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_accounting_book_fk |  | fid |
| 2 | pk_ai_accounting_book |  | fpkid |

---

## 凭证分录详细描述-子表 t_ai_model_vchinfo

- **表名称：** 凭证分录详细描述-子表
- **表名：** t_ai_model_vchinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fdcdesc | 借贷方向 | varchar | 50 |  | √ | ' ' | 借贷方向,枚举: 1 :借 2 :贷 |
| 4 | faccountsproxy | faccountsproxy | varchar | 255 |  | √ | ' ' |  |
| 5 | facctinfo | facctinfo | varchar | 2000 |  | √ | ' ' |  |
| 6 | faccountruleid | faccountruleid | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fautobal | fautobal | bpchar | 1 |  | √ | '0' |  |
| 9 | faccountruledescription | 科目核算规则描述 | varchar | 500 |  | √ | ' ' | 科目核算规则描述 |
| 10 | ffatherlinkid | ffatherlinkid | varchar | 50 |  | √ | ' ' |  |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fcurrencytype | 记账币别 | varchar | 50 |  | √ | ' ' | 记账币别,枚举: 1 :账簿本位币 2 :业务原币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_model_vchinfo_fk |  | fid |
| 2 | pk_ai_model_vchinfo |  | fentryid |

---

## AI记账模型-主表 t_ai_accounting_model

- **表名称：** AI记账模型-主表
- **表名：** t_ai_accounting_model

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxml | fxml | text | 0 |  |  | null |  |
| 3 | fgptguideinfo | fgptguideinfo | varchar | 1000 |  | √ | ' ' |  |
| 4 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fanalyzeacctrule | fanalyzeacctrule | bpchar | 1 |  | √ | '0' |  |
| 10 | fentrymerge | fentrymerge | varchar | 500 |  | √ | ' ' |  |
| 11 | fcertificate | fcertificate | int8 | 64 |  | √ | '1323036438454863872' |  |
| 12 | fruledescription | 记账规则描述 | varchar | 500 |  | √ | ' ' | 记账规则描述 |
| 13 | fbizinfoschemeid | fbizinfoschemeid | int8 | 64 |  | √ | 0 |  |
| 14 | fisdeepthink | fisdeepthink | bpchar | 1 |  | √ | '0' |  |
| 15 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 16 | fname | 名称 | varchar | 148 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | faccounttableid | faccounttableid | int8 | 64 |  | √ | 0 |  |
| 20 | fentrymergedesc | fentrymergedesc | varchar | 50 |  | √ | ' ' |  |
| 21 | fsourcebillid | fsourcebillid | varchar | 36 |  | √ | ' ' |  |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fgenvoucherstatus | fgenvoucherstatus | varchar | 5 |  |  | '2' |  |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fsrcmodel | fsrcmodel | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ai_accounting_model |  | fid |
| 2 | idx_ai_acc_model_sourcebill |  | fsourcebillid |

---

## AI记账模型-多语言表 t_ai_accounting_model_l

- **表名称：** AI记账模型-多语言表
- **表名：** t_ai_accounting_model_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 148 |  | √ | ' ' | 名称 |
| 3 | fruledescription | 记账规则描述 | varchar | 500 |  | √ | ' ' | 记账规则描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fgptguideinfo | fgptguideinfo | varchar | 1000 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_accounting_model_l |  | fpkid |
| 2 | idx_ai_accounting_model_l_lid |  | fid,flocaleid |

---

## 凭证分录详细描述-多语言表 t_ai_model_vchinfo_l

- **表名称：** 凭证分录详细描述-多语言表
- **表名：** t_ai_model_vchinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccountruledescription | 科目核算规则描述 | varchar | 500 |  | √ | ' ' | 科目核算规则描述 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_model_vchinfo_l_lid |  | fentryid,flocaleid |
| 2 | pk_t_ai_model_vchinfo_l |  | fpkid |

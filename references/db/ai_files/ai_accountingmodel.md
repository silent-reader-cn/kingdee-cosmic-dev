# AI记账模型-ai_accountingmodel

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
| 2 | fremark | 摘要描述 | varchar | 255 |  | √ | ' ' | 摘要描述 |
| 3 | fdcdesc | 借贷方向 | varchar | 50 |  | √ | ' ' | 借贷方向,枚举: 1 :借 2 :贷 |
| 4 | faccountsproxy | 科目范围 | varchar | 255 |  | √ | ' ' | 科目范围 |
| 5 | facctinfo | 科目信息 | varchar | 2000 |  | √ | ' ' | 科目信息 |
| 6 | faccountruleid | 科目核算规则 | int8 | 64 |  | √ | 0 | [科目核算规则 ai_account_rule](../ai_files/ai_account_rule.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fautobal | 自动平衡 | bpchar | 1 |  | √ | '0' | 自动平衡 |
| 9 | faccountruledescription | 记账要求 | varchar | 500 |  | √ | ' ' | 记账要求 |
| 10 | ffatherlinkid | 关联id | varchar | 50 |  | √ | ' ' | 关联id |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fcurrencytype | 记账币种 | varchar | 50 |  | √ | ' ' | 记账币种,枚举: 1 :账簿本位币 2 :业务原币 |

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
| 2 | fxml | 系统规则配置内容 | text | 0 |  |  | null | 系统规则配置内容 |
| 3 | fgptguideinfo | AI提示词 | varchar | 1000 |  | √ | ' ' | AI提示词 |
| 4 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fanalyzeacctrule | 解析记账规则 | bpchar | 1 |  | √ | '0' | 解析记账规则 |
| 10 | fentrymerge | 分录合并选项设置 | varchar | 500 |  | √ | ' ' | 分录合并选项设置 |
| 11 | fcertificate | 凭证字 | int8 | 64 |  | √ | '1323036438454863872' | [凭证字 gl_vouchertype](../gl_files/gl_vouchertype.md) |
| 12 | fruledescription | 记账场景描述 | varchar | 500 |  | √ | ' ' | 记账场景描述 |
| 13 | fbizinfoschemeid | 会计事项 | int8 | 64 |  | √ | 0 | [会计事项 ai_bizinfoscheme](../ai_files/ai_bizinfoscheme.md) |
| 14 | fisdeepthink | 深度思考 | bpchar | 1 |  | √ | '0' | 深度思考 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fname | 名称 | varchar | 148 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 20 | fentrymergedesc | 分录合并选项 | varchar | 50 |  | √ | ' ' | 分录合并选项 |
| 21 | fsourcebillid | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fgenvoucherstatus | 凭证生成状态 | varchar | 5 |  |  | '2' | 凭证生成状态,枚举: 1 :暂存 2 :提交 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fsrcmodel | 来源预置模型 | varchar | 50 |  | √ | ' ' | 来源预置模型 |

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

## 科目范围真实字段-多选基础资料表 t_ai_accounting_account

- **表名称：** 科目范围真实字段-多选基础资料表
- **表名：** t_ai_accounting_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ai_accounting_account |  | fpkid |
| 2 | idx_ai_accounting_account_fk |  | fentryid |

---

## AI记账模型-多语言表 t_ai_accounting_model_l

- **表名称：** AI记账模型-多语言表
- **表名：** t_ai_accounting_model_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 148 |  | √ | ' ' | 名称 |
| 3 | fruledescription | 记账场景描述 | varchar | 500 |  | √ | ' ' | 记账场景描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fgptguideinfo | AI提示词 | varchar | 1000 |  | √ | ' ' | AI提示词 |
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
| 1 | faccountruledescription | 记账要求 | varchar | 500 |  | √ | ' ' | 记账要求 |
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

# 多栏账方案-gl_multcol_scheme

## 多栏账方案-多语言表 t_gl_multcolumn_scheme_l

- **表名称：** 多栏账方案-多语言表
- **表名：** t_gl_multcolumn_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_multcol_l |  | fid,flocaleid |
| 2 | t_gl_multcolumn_scheme_l_pkey |  | fpkid |

---

## 单据体-子表 t_gl_multcolumn_entry

- **表名称：** 单据体-子表
- **表名：** t_gl_multcolumn_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | 编码 | int8 | 64 |  | √ | 0 | [科目影响因素 ai_accountmaptype](../ai_files/ai_accountmaptype.md) |
| 3 | fdc | 方向 | bpchar | 1 |  | √ | '1' | 方向,枚举: 1 :借 0 :贷 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | faccountid | 编码 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_multcol_entry |  | fid |
| 2 | t_gl_multcolumn_entry_pkey |  | fentryid |

---

## 多栏账方案-主表 t_gl_multcolumn_scheme

- **表名称：** 多栏账方案-主表
- **表名：** t_gl_multcolumn_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ffieldname | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 7 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftypeid | 多栏账类别 | bpchar | 1 |  | √ | '0' | 多栏账类别,枚举: 0 :科目多栏账 1 :核算维度多栏账 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 12 | flevel | 多栏账明细级次 | varchar | 50 |  | √ | '0' | 多栏账明细级次,枚举: |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 17 | fleveltypeid | 多栏账级别 | bpchar | 1 |  | √ | '1' | 多栏账级别,枚举: 0 :最明细级 1 :非明细级 |
| 18 | fcurrencyid | 币种 | varchar | 50 |  | √ | '0' | 币种,枚举: |
| 19 | faccountid | 科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_multcol_org |  | forgid,fbooktypeid |
| 2 | t_gl_multcolumn_scheme_pkey |  | fid |

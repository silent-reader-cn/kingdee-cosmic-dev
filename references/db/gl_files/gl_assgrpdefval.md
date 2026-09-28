# 核算维度默认值设置-gl_assgrpdefval

## 指定人员-多选基础资料表 t_gl_assgrpdefvaluser

- **表名称：** 指定人员-多选基础资料表
- **表名：** t_gl_assgrpdefvaluser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_assgrpdefvaluser |  | fid |
| 2 | t_gl_assgrpdefvaluser_pkey |  | fpkid |

---

## 核算维度默认值设置-主表 t_gl_assgrpdefval

- **表名称：** 核算维度默认值设置-主表
- **表名：** t_gl_assgrpdefval

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fuserid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fusertype | 适用人员 | bpchar | 1 |  | √ | '0' | 适用人员,枚举: 0 :全部人员 1 :指定人员 |
| 6 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 7 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_assgrpdefval_pkey |  | fid |
| 2 | idx_gl_assgrpdefval |  | forgid,fuserid |

---

## 核算维度默认值设置-多语言表 t_gl_assgrpdefval_l

- **表名称：** 核算维度默认值设置-多语言表
- **表名：** t_gl_assgrpdefval_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_assgrpdefval_l_pkey |  | fpkid |
| 2 | idx_gl_assgrpdefval_l |  | fid,flocaleid |

---

## 单据体-子表 t_gl_assgrpdefvalentry

- **表名称：** 单据体-子表
- **表名：** t_gl_assgrpdefvalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasepk | 基础资料值主键 | varchar | 20 |  | √ | ' ' | 基础资料值主键 |
| 3 | fbasedataval | 默认维度值 | int8 | 64 |  | √ | 0 | [科目影响因素（旧） ai_vchentrytype](../ai_files/ai_vchentrytype.md) |
| 4 | fassgrpid | fassgrpid | int8 | 64 |  | √ | 0 |  |
| 5 | ftxtval | 默认手工维度值 | varchar | 50 |  | √ | ' ' | 默认手工维度值 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fassgrptypeid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_assgrpdefvalentry |  | fid |
| 2 | t_gl_assgrpdefvalentry_pkey |  | fentryid |

# 应收收款手工核销方案-ar_handsettlescheme

## 规则单据体-子表 t_ar_handsettleschemerule

- **表名称：** 规则单据体-子表
- **表名：** t_ar_handsettleschemerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettlerelation | 核销关系 | varchar | 50 |  | √ | ' ' | 核销关系,枚举: recsettle :应收收款核销 arapsettle :应收冲应付 recpaysettle :收款冲退款 arpaysettle :应收退款核销 arself :应收红蓝对冲 baddebtrecovery :坏账收回 |
| 3 | fmatchrulevalue | 匹配规则 | varchar | 255 |  | √ | ' ' | 匹配规则 |
| 4 | fmatchrulevalue_tag | 匹配规则_详情 | text | 0 |  |  | null | 匹配规则_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmatchruledesc | 匹配规则 | varchar | 1000 |  | √ | ' ' | 匹配规则 |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_handsettleschemerule |  | fentryid |
| 2 | idx_ar_handsettleschemer_fid |  | fid |

---

## 应收收款手工核销方案-主表 t_ar_handsettlescheme

- **表名称：** 应收收款手工核销方案-主表
- **表名：** t_ar_handsettlescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdefaultscheme | 默认方案 | bpchar | 1 |  | √ | ' ' | 默认方案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_handsettlescheme |  | fid |
| 2 | idx_ar_scheme_number |  | fnumber |

---

## 组织单据体-子表 t_ar_handsettleschemeorge

- **表名称：** 组织单据体-子表
- **表名：** t_ar_handsettleschemeorge

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | forg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_handsettleschemeorge |  | fentryid |
| 2 | idx_ar_handsettleschemeo_fid |  | fid |

---

## 应收收款手工核销方案-多语言表 t_ar_handsettlescheme_l

- **表名称：** 应收收款手工核销方案-多语言表
- **表名：** t_ar_handsettlescheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_handsettlescheme_l |  | fpkid |
| 2 | idx_ar_handsettlescheme_fid |  | fid,flocaleid |

# 成本BOM同步规则-cad_syncbom_rule

## 成本BOM同步规则-多语言表 t_cad_syncbom_rule_l

- **表名称：** 成本BOM同步规则-多语言表
- **表名：** t_cad_syncbom_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cad_syncbom_rule_l |  | fpkid |
| 2 | idx_cad_syncrulel_fid |  | fid,flocaleid |

---

## 成本BOM同步规则-主表 t_cad_syncbom_rule

- **表名称：** 成本BOM同步规则-主表
- **表名：** t_cad_syncbom_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fcalorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fsyncuser | 同步人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | ffilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | fisreplace | 包含替代件 | bpchar | 1 |  | √ | '0' | 包含替代件 |
| 13 | fisjumplevel | 包含跳层 | bpchar | 1 |  | √ | '0' | 包含跳层 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cad_syncbom_rule |  | fid |
| 2 | idx_cad_syncrule_no |  | fnumber |
| 3 | idx_cad_syncrule_org |  | fcalorg |

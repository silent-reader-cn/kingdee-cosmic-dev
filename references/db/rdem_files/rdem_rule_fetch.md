# 取数规则-rdem_rule_fetch

## 取数规则报表项关系-子表 t_rdem_rep_it_fetch_re

- **表名称：** 取数规则报表项关系-子表
- **表名：** t_rdem_rep_it_fetch_re

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freportitemid | 报表项 | int8 | 64 |  | √ | 0 | [报表项 rdem_report_item](../rdem_files/rdem_report_item.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_rep_it_fetch_re_fk |  | fid |
| 2 | pk_rdem_rep_it_fetch_re |  | fentryid |

---

## 取数规则-多语言表 t_rdem_rule_fetch_l

- **表名称：** 取数规则-多语言表
- **表名：** t_rdem_rule_fetch_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 公式名称 | varchar | 2000 |  | √ | ' ' | 公式名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_rule_fetch_l |  | fpkid |
| 2 | idx_rdem_rule_fetch_l_0 |  | fid,flocaleid |

---

## 取数规则-主表 t_rdem_rule_fetch

- **表名称：** 取数规则-主表
- **表名：** t_rdem_rule_fetch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 公式名称 | varchar | 2000 |  | √ | ' ' | 公式名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodelid | 体系 | int8 | 64 |  | √ | 0 | [体系管理 rdem_model](../rdem_files/rdem_model.md) |
| 6 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fformula | 公式 | varchar | 2000 |  | √ | ' ' | 公式 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | ffittype | 适用类型 | varchar | 50 |  | √ | ' ' | 适用类型,枚举: TYXGZ :通用项规则 BBXGZ :报表项规则 |
| 15 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: text :文本 number :数值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_rule_fetch |  | fid |
| 2 | idx_rdem_rule_fetch_m0 |  | fmasterid |

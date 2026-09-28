# 样式规则-rdem_rule_style

## 样式规则-多语言表 t_rdem_rule_style_l

- **表名称：** 样式规则-多语言表
- **表名：** t_rdem_rule_style_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 公式名称 | varchar | 300 |  | √ | ' ' | 公式名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_rule_style_l |  | fpkid |
| 2 | idx_rdem_rule_style_l_0 |  | fid,flocaleid |

---

## 样式规则报表项关系-子表 t_rdem_rep_it_style_re

- **表名称：** 样式规则报表项关系-子表
- **表名：** t_rdem_rep_it_style_re

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
| 1 | pk_rdem_rep_it_style_re |  | fentryid |
| 2 | idx_rdem_rep_it_style_re_fk |  | fid |

---

## 样式规则-主表 t_rdem_rule_style

- **表名称：** 样式规则-主表
- **表名：** t_rdem_rule_style

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 公式名称 | varchar | 200 |  | √ | ' ' | 公式名称 |
| 4 | fcelltype | 单元格类型 | varchar | 50 |  | √ | ' ' | 单元格类型,枚举: 1 :输入框 2 :下拉框 3 :复选框 4 :单选框 5 :基础资料 6 :URL 7 :加密文本 8 :格式化 9 :dataformat |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodelid | 体系 | int8 | 64 |  | √ | 0 | [体系管理 rdem_model](../rdem_files/rdem_model.md) |
| 7 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fformula | 样式表达式 | varchar | 2000 |  | √ | ' ' | 样式表达式 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | ffittype | 适用类型 | varchar | 50 |  | √ | ' ' | 适用类型,枚举: TYXGZ :通用项规则 BBXGZ :报表项规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_rule_style_m0 |  | fmasterid |
| 2 | pk_rdem_rule_style |  | fid |

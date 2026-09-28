# 报表指标定义-fsa_rptindicators

## 报表指标定义-多语言表 t_fsa_rptindicators_l

- **表名称：** 报表指标定义-多语言表
- **表名：** t_fsa_rptindicators_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 指标名称 | varchar | 100 |  | √ | ' ' | 指标名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_rptindicators_l |  | fpkid |
| 2 | idx_fsa_rptindicators_l |  | fid |

---

## 单据体-子表 t_fsa_rptidxrptent

- **表名称：** 单据体-子表
- **表名：** t_fsa_rptidxrptent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcstdrptid | 源标准报表 | int8 | 64 |  | √ | 0 | 标准报表项目 fsa_rptitems |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_rptidxrptent |  | fentryid |
| 2 | idx_fsa_rptidxrptent_1 |  | fid |

---

## 报表指标定义-主表 t_fsa_rptindicators

- **表名称：** 报表指标定义-主表
- **表名：** t_fsa_rptindicators

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fcalcformular_tag | 表达式_详情 | text | 0 |  |  | null | 表达式_详情 |
| 5 | fcalcformular | 表达式 | varchar | 510 |  | √ | ' ' | 表达式 |
| 6 | fdescription | 描述 | varchar | 510 |  |  | null | 描述 |
| 7 | frptitemsrctype | 数据来源类型 | bpchar | 1 |  | √ | ' ' | 数据来源类型,枚举: 0 :系统预置 1 :自定义 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fdisplayformular_tag | 表达译文_详情 | text | 0 |  |  | null | 表达译文_详情 |
| 13 | fdescription_tag | 描述_详情 | text | 0 |  |  | null | 描述_详情 |
| 14 | frefrptcnt | 依赖的报表数量 | int4 | 32 |  | √ | 0 | 依赖的报表数量 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fdisplayformular | 表达译文 | varchar | 510 |  | √ | ' ' | 表达译文 |
| 17 | fnumber | 指标编码 | varchar | 50 |  | √ | ' ' | 指标编码 |
| 18 | frpttype | 报表类型 | varchar | 10 |  | √ | ' ' | 报表类型,枚举: 0 :资产负债表 1 :利润表 2 :现金流量表 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_rptindicators |  | fstatus,frefrptcnt,fnumber |
| 2 | pk_t_fsa_rptindicators |  | fid |

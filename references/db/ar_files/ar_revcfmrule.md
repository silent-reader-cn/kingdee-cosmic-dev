# 收入分摊规则-ar_revcfmrule

## 收入分摊规则-多语言表 t_ar_revcfmrule_l

- **表名称：** 收入分摊规则-多语言表
- **表名：** t_ar_revcfmrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_revcfmrule_l_fid |  | fid,flocaleid |
| 2 | pk_t_ar_revcfmrule_l |  | fpkid |

---

## 收入分摊规则-主表 t_ar_revcfmrule

- **表名称：** 收入分摊规则-主表
- **表名：** t_ar_revcfmrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fname | 规则名称 | varchar | 80 |  | √ | ' ' | 规则名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fchangemethod | 变动调整方法 | varchar | 5 |  | √ | ' ' | 变动调整方法,枚举: 0 :适用未来法 1 :追溯调整法 |
| 7 | frevcfmmethod | 分摊方法 | varchar | 5 |  | √ | ' ' | 分摊方法,枚举: 0 :按天平均 1 :按期间平均 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | frevcfmdimension | 分摊维度 | varchar | 5 |  | √ | ' ' | 分摊维度,枚举: 0 :按期间分摊 |
| 13 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 规则编码 | varchar | 80 |  | √ | ' ' | 规则编码 |
| 15 | fisdefault | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_revcfmrule |  | fid |
| 2 | idx_ar_revcfmrule_num |  | fnumber |

---

## 收入计划映射-子表 t_ar_revcfmrule_mapping

- **表名称：** 收入计划映射-子表
- **表名：** t_ar_revcfmrule_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplankey | 计划行字段 | varchar | 255 |  | √ | ' ' | 计划行字段,枚举: |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentrykey | 明细行字段 | varchar | 255 |  | √ | ' ' | 明细行字段,枚举: |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_revcfmrule_mapping |  | fentryid |
| 2 | idx_ar_revcfm_m_fid |  | fid |

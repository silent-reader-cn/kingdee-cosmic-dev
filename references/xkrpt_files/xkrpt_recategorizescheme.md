# 净额重分类方案-xkrpt_recategorizescheme

## 净额重分类方案-主表 t_xkrpt_recategoryscheme

- **表名称：** 净额重分类方案-主表
- **表名：** t_xkrpt_recategoryscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpositiveitem | 净额正数记入 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fmaindime | 主核算维度 | varchar | 50 |  | √ | ' ' | 主核算维度,枚举: |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | facctformula | 科目表达式 | varchar | 2000 |  | √ | ' ' | 科目表达式 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fexprsrc | 表达式原始值 | varchar | 2000 |  | √ | ' ' | 表达式原始值 |
| 16 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 17 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fnegativeitem | 净额负数记入 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_xkrpt_recategory_number |  | fnumber |
| 2 | pk_xkrpt_recategoryscheme |  | fid |

---

## 净额重分类方案-多语言表 t_xkrpt_recategoryscheme_l

- **表名称：** 净额重分类方案-多语言表
- **表名：** t_xkrpt_recategoryscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_recategoryscheme_l |  | fpkid |
| 2 | idx_xkrpt_recategory_l |  | fid,flocaleid |

---

## 核算维度单据体-子表 t_xkrpt_dimensionmap

- **表名称：** 核算维度单据体-子表
- **表名：** t_xkrpt_dimensionmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimeto | 关联维度 | varchar | 50 |  | √ | ' ' | 关联维度,枚举: |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fdimetofieldname | 关联维度字段 | varchar | 100 |  | √ | ' ' | 关联维度字段 |
| 6 | fdimetofield | 关联维度字段 | varchar | 50 |  | √ | ' ' | 关联维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_dimensionmap |  | fentryid |
| 2 | idx_t_xkrpt_dimensionmap |  | fid |

---

## 项目数据类型-多选基础资料表 t_xkrpt_reschemedatatype

- **表名称：** 项目数据类型-多选基础资料表
- **表名：** t_xkrpt_reschemedatatype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_reschemedatatype |  | fpkid |
| 2 | idx_xkrpt_datatype_fid |  | fid |

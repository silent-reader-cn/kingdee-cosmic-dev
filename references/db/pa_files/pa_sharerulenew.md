# 分摊规则-pa_sharerulenew

## 接收方单据体-子表 t_pa_shareruleentry

- **表名称：** 接收方单据体-子表
- **表名：** t_pa_shareruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceivematename | 元数据标识 | varchar | 500 |  | √ | ' ' | 元数据标识 |
| 3 | freceivedimensiontext | 大文本4 | varchar | 255 |  | √ | ' ' | 大文本4 |
| 4 | fcomboreceive | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :在...中 |
| 5 | freceivedimtype | 维度类型 | varchar | 50 |  | √ | ' ' | 维度类型 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | freceivedimvalue | 维度值 | varchar | 1024 |  | √ | ' ' | 维度值 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | freceivedimid | 输入标识 | varchar | 1024 |  | √ | ' ' | 输入标识 |
| 10 | freceivedimensiontext_tag | 大文本4_详情 | text | 0 |  |  | null | 大文本4_详情 |
| 11 | freceivedimension | 维度 | int8 | 64 |  | √ | 0 | 维度 pa_dimension |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_shareruleentry |  | fentryid |
| 2 | idx_pa_shareruleentry_fk |  | fid |

---

## 详情单据体-子表 t_pa_sharesavesubdata

- **表名称：** 详情单据体-子表
- **表名：** t_pa_sharesavesubdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubdataid | id串 | varchar | 500 |  | √ | ' ' | id串 |
| 3 | fsubvalue_tag | 大文本_详情 | text | 0 |  |  | null | 大文本_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsubvalue | 大文本 | varchar | 255 |  | √ | ' ' | 大文本 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_sharesavesubdata |  | fentryid |
| 2 | idx_pa_share_savesubdata |  | fid |

---

## 分摊度量值-多选基础资料表 t_pa_sharebase

- **表名称：** 分摊度量值-多选基础资料表
- **表名：** t_pa_sharebase

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 度量 pa_measure |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_sharebase |  | fid |
| 2 | pk_t_pa_sharebase |  | fpkid |

---

## 限制组合单据体-子表 t_pa_sharesavelimit

- **表名称：** 限制组合单据体-子表
- **表名：** t_pa_sharesavelimit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubvaluelimit | 大文本 | varchar | 255 |  | √ | ' ' | 大文本 |
| 3 | fsubvaluelimit_tag | 大文本_详情 | text | 0 |  |  | null | 大文本_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsubdataidlimit | id串 | varchar | 500 |  | √ | ' ' | id串 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_sharesavelimit |  | fid |
| 2 | pk_t_pa_sharesavelimit |  | fentryid |

---

## 分摊规则-多语言表 t_pa_sharerulenew_l

- **表名称：** 分摊规则-多语言表
- **表名：** t_pa_sharerulenew_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_sharerulenew_l |  | fpkid |
| 2 | idx_pa_share_rulenew_l |  | flocaleid,fid |

---

## 发送方单据体-子表 t_pa_shareruleentrysend

- **表名称：** 发送方单据体-子表
- **表名：** t_pa_shareruleentrysend

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensiontext | 大文本3 | varchar | 255 |  | √ | ' ' | 大文本3 |
| 3 | fdimensionvalue | 维度值 | varchar | 1024 |  | √ | ' ' | 维度值 |
| 4 | fdimensionid | 输入标识 | varchar | 1024 |  | √ | ' ' | 输入标识 |
| 5 | fsenddimension | 维度 | int8 | 64 |  | √ | 0 | 维度 pa_dimension |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsenddimtype | 维度类型 | varchar | 50 |  | √ | ' ' | 维度类型 |
| 8 | fsendmatename | 元数据标识 | varchar | 500 |  | √ | ' ' | 元数据标识 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fdimensiontext_tag | 大文本3_详情 | text | 0 |  |  | null | 大文本3_详情 |
| 11 | fcombofield | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :在...中 B :不在...中 C :为空 D :不为空 E :全部 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_shareruleentrysend |  | fid |
| 2 | pk_t_pa_shareruleentrysend |  | fentryid |

---

## 分摊规则-主表 t_pa_sharerulenew

- **表名称：** 分摊规则-主表
- **表名：** t_pa_sharerulenew

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | flimittype | 限定方式 | varchar | 50 |  | √ | ' ' | 限定方式,枚举: 0 :排除 1 :仅包含 |
| 6 | finputratiobox | 输入比例 | bpchar | 1 |  | √ | ' ' | 输入比例 |
| 7 | fanalysissystemid | 分析体系 | int8 | 64 |  | √ | 0 | 分析体系 pa_anasystemsetting |
| 8 | freceiverule | 分摊方式 | varchar | 50 |  | √ | ' ' | 分摊方式,枚举: A :按分摊因子 B :按科目金额 C :按固定比例 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | faccountfilter_tag | 科目过滤条件_详情 | text | 0 |  |  | null | 科目过滤条件_详情 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fanalysismodelid | 分析模型 | int8 | 64 |  | √ | 0 | 分析模型 pa_analysismodel |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | flimitbox | 是否限定组合 | bpchar | 1 |  | √ | ' ' | 是否限定组合 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | faccountfilter | 科目过滤条件 | varchar | 255 |  | √ | ' ' | 科目过滤条件 |
| 19 | fmeasure | 参考度量值 | int8 | 64 |  | √ | 0 | 度量 pa_measure |
| 20 | fsharefactor | 分摊因子 | int8 | 64 |  | √ | 0 | 分摊因子 pa_sharefactor |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_sharerulenew |  | fid |
| 2 | idx_pa_share_rulenew |  | fnumber |

# 数据方案设置-fsa_data_scheme

## 数据方案设置-主表 t_fsa_dstoryscheme

- **表名称：** 数据方案设置-主表
- **表名：** t_fsa_dstoryscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 9 | fdescription | 描述信息 | text | 0 |  |  | null | 描述信息 |
| 10 | fdatacollectionid | 数据集合 | int8 | 64 |  | √ | 0 | [数据集合 fsa_data_collection](../fsa_files/fsa_data_collection.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_dstoryscheme |  | fid |
| 2 | idx_fsa_dstoryscheme |  | fnumber |

---

## 数据集合子单据体-子表 t_fsa_outputfields

- **表名称：** 数据集合子单据体-子表
- **表名：** t_fsa_outputfields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldnumber | 维度编码 | varchar | 50 |  | √ | ' ' | 维度编码 |
| 2 | fsourcenumber | 源字段编码 | varchar | 50 |  | √ | ' ' | 源字段编码 |
| 3 | fdimtype | 维度类型 | bpchar | 1 |  | √ | '2' | 维度类型,枚举: 1 :数据维 2 :度量维 0 :日期维 |
| 4 | fdisplaynumber | 输出编码 | bpchar | 1 |  | √ | '0' | 输出编码 |
| 5 | ffieldname | 维度名称 | varchar | 50 |  | √ | ' ' | 维度名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | foutputhierarchy | 输出层级 | bpchar | 1 |  | √ | '0' | 输出层级,枚举: 1 :是 0 :否 |
| 9 | foutput | 是否输出 | bpchar | 1 |  | √ | '1' | 是否输出,枚举: 1 :是 0 :否 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_outputfields |  | fdetailid |
| 2 | idx_fsa_outputfields_1 |  | ffieldnumber |

---

## 可用数据单据体-子表 t_fsa_dstoryschemeent

- **表名称：** 可用数据单据体-子表
- **表名：** t_fsa_dstoryschemeent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdisableversions | 禁用的版本 | varchar | 255 |  |  | ' ' | 禁用的版本 |
| 3 | fdisableversions_tag | 禁用的版本_详情 | text | 0 |  |  | null | 禁用的版本_详情 |
| 4 | fdatasyncparamid | 同步参数名称 | int8 | 64 |  | √ | 0 | [同步参数设置 fsa_syncparam](../fsa_files/fsa_syncparam.md) |
| 5 | fuselatestversion | 使用最新版本 | bpchar | 1 |  | √ | '1' | 使用最新版本 |
| 6 | fexportalldata | 输出全部数据 | bpchar | 1 |  | √ | '0' | 输出全部数据 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_dstoryschemeent |  | fentryid |
| 2 | idx_fsa_dstoryschemeent |  | fid |

---

## 数据方案设置-多语言表 t_fsa_dstoryscheme_l

- **表名称：** 数据方案设置-多语言表
- **表名：** t_fsa_dstoryscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_dstoryscheme_l |  | fpkid |
| 2 | idx_fsa_dstoryscheme_l |  | fid,flocaleid |

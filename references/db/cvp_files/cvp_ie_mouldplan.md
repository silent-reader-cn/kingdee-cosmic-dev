# 文档信息提取-cvp_ie_mouldplan

## 大模型提取单据体-子表 t_cvp_ie_mould_llm

- **表名称：** 大模型提取单据体-子表
- **表名：** t_cvp_ie_mould_llm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fextractnum | 提取编码 | varchar | 50 |  | √ | ' ' | 提取编码 |
| 3 | ftabname | 表名称 | varchar | 60 |  |  | null | 表名称 |
| 4 | fextractfield | 字段名称 | varchar | 1000 |  | √ | ' ' | 字段名称 |
| 5 | ffieldtype | 字段类型 | int8 | 64 |  |  | null | [提取字段类型 cvp_field_types](../cvp_files/cvp_field_types.md) |
| 6 | ftabnum | 表编码 | varchar | 50 |  |  | null | 表编码 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fexdescription | 字段描述与提取要求 | varchar | 1000 |  | √ | ' ' | 字段描述与提取要求 |
| 9 | foutput | 输出结果与要求 | varchar | 1000 |  | √ | ' ' | 输出结果与要求 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_llm_extracfield |  | ftabnum |
| 2 | pk_t_cvp_ie_mould_llm |  | fentryid |

---

## 文档信息提取-多语言表 t_cvp_ie_mould_l

- **表名称：** 文档信息提取-多语言表
- **表名：** t_cvp_ie_mould_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_ie_mould_l |  | fpkid |
| 2 | idx_t_cvp_ie_mould_l |  | fname |

---

## 文档信息提取-主表 t_cvp_ie_mould

- **表名称：** 文档信息提取-主表
- **表名：** t_cvp_ie_mould

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusellmextract | 大模型自定义提取字段 | bpchar | 1 |  |  | null | 大模型自定义提取字段 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 5 | fmulti_model | 多模态大模型 | varchar | 50 |  | √ | ' ' | 多模态大模型,枚举: kingdee_multi_llm :金蝶自研多模态模型 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcommonextract | 通用提取字段 | bpchar | 1 |  |  | null | 通用提取字段 |
| 8 | fdoc_extract_model | 文档解析模型 | varchar | 50 |  | √ | ' ' | 文档解析模型,枚举: kingdee_fileextract_v1 :金蝶自研复杂文档解析模型V1 kingdee_fileextract_v2 :金蝶自研复杂文档解析模型V2（多模态版） |
| 9 | fdescription | 方案说明 | varchar | 255 |  |  | null | 方案说明 |
| 10 | fdocdescrip | 文档内容描述 | varchar | 1000 |  | √ | ' ' | 文档内容描述 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 15 | freserve_tokens | 预留模型输出字数 | int4 | 32 |  | √ | 4096 | 预留模型输出字数 |
| 16 | fissys | 是否预置 | bpchar | 1 |  |  | null | 是否预置 |
| 17 | fllm | 文本大模型 | varchar | 80 |  | √ | 'DOUBAO_PRO' | 文本大模型,枚举: DOUBAO_PRO :豆包pro系列模型组合 |
| 18 | fextract_way | 提取方式 | varchar | 50 |  | √ | ' ' | 提取方式,枚举: multi_model_extract :多模态大模型提取 llm_extract :文档解析+文本大模型提取 |
| 19 | fenable | 使用状态 | varchar | 50 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fbusinessconfig | 文档类型 | varchar | 50 |  |  | 'B' | 文档类型,枚举: B :通用表单文档 A :合同文档 |
| 21 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_ie_mould |  | fid |
| 2 | inx_t_cvp_ie_mould |  | fnumber,fname |

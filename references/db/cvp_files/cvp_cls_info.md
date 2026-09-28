# 文档分类-cvp_cls_info

## 单据体-子表 t_cvp_classifier_config

- **表名称：** 单据体-子表
- **表名：** t_cvp_classifier_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fincludedtemplate | 模版名称 | int8 | 64 |  | √ | 0 | [模板基础资料 cvp_template_base](../cvp_files/cvp_template_base.md) |
| 3 | fmodifydate | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |
| 4 | fkeyoword | 分类关键字 | varchar | 1000 |  |  | ' ' | 分类关键字 |
| 5 | ftempid | 模板主键 | int8 | 64 |  | √ | 0 | 模板主键 |
| 6 | fkeycode | 模板类型 | varchar | 50 |  |  | null | 模板类型,枚举: preset :预置模板 custom :自定义模板 ie :信息提取方案 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | ftempformid | 模板formid | varchar | 50 |  |  | null | 模板formid |
| 10 | fclsdesc | 分类依据描述 | varchar | 2000 |  |  | null | 分类依据描述 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fdoctypename | 文件类别 | varchar | 50 |  |  | null | 文件类别 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_classifier_config |  | fincludedtemplate |
| 2 | pk_t_cvp_classifier_config |  | fentryid |

---

## 文档分类-主表 t_cvp_classifier_info

- **表名称：** 文档分类-主表
- **表名：** t_cvp_classifier_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 组合识别器名称 | varchar | 50 |  | √ | ' ' | 组合识别器名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 6 | fstatus | 状态 | varchar | 50 |  |  | ' ' | 状态,枚举: A :未发布 B :已发布-有更新 C :可用 D :禁用 E :发布可用 |
| 7 | ftext_extract_model | 文档解析模型 | varchar | 80 |  | √ | 'kingdee_fileextract_v1' | 文档解析模型,枚举: kingdee_fileextract_v1 :金蝶自研复杂文档解析模型V1（小模型版） kingdee_fileextract_v2 :金蝶自研复杂文档解析模型V2（多模态版） kingdee_common_cr :金蝶自研通用文字识别 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fbillisperset | 是否预置 | varchar | 50 |  |  | ' ' | 是否预置,枚举: A :是 B :否 |
| 11 | fmulti_llm | 多模态大模型 | varchar | 80 |  | √ | 'kingdee_multi_llm' | 多模态大模型,枚举: kingdee_multi_llm :金蝶自研多模态模型 |
| 12 | fclassifiermethod | 分类方法 | varchar | 50 |  |  | ' ' | 分类方法,枚举: 1 :关键字 2 :图片 3 :大模型 |
| 13 | fllm | 文本大模型 | varchar | 80 |  | √ | 'DOUBAO_PRO' | 文本大模型,枚举: DOUBAO_PRO :豆包pro系列模型组合 |
| 14 | fenable | 使用状态 | varchar | 50 |  |  | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 组合识别器编码 | varchar | 30 |  |  | ' ' | 组合识别器编码 |
| 16 | fdesc | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 17 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 18 | fclassifierllmtype | 大模型分类方式 | varchar | 50 |  | √ | 'text_model' | 大模型分类方式,枚举: text_model :文档解析+文本大模型分类 multimodal_model :多模态大模型分类 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_classifier_info |  | fid |
| 2 | idx_cvp_classifier_info |  | fnumber,fname |

---

## 图片集-附件表 t_cvp_classifier_files

- **表名称：** 图片集-附件表
- **表名：** t_cvp_classifier_files

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__cvp_classifier_files |  | fbasedataid |
| 2 | pk_t_cvp_classifier_files |  | fpkid |

---

## 文档分类-多语言表 t_cvp_classifier_info_l

- **表名称：** 文档分类-多语言表
- **表名：** t_cvp_classifier_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 组合识别器名称 | varchar | 50 |  | √ | ' ' | 组合识别器名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_classifier_info_l |  | fid |
| 2 | pk_t_cvp_classifier_info_l |  | fpkid |

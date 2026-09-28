# 主题-gai_cbi_theme_singledata

## 主题-主表 t_gai_cbi_single_scheme

- **表名称：** 主题-主表
- **表名：** t_gai_cbi_single_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatasetid | 数据集 | int8 | 64 |  | √ | 0 | [数据集 gai_cbi_dataset](../chatbi_files/gai_cbi_dataset.md) |
| 3 | fname | 主题名称 | varchar | 50 |  | √ | ' ' | 主题名称 |
| 4 | finputprompt | 输入框提示语 | varchar | 255 |  | √ | ' ' | 输入框提示语 |
| 5 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fpicture | 主题图标 | varchar | 255 |  | √ | ' ' | 主题图标 |
| 8 | fstatus | 主题状态 | varchar | 50 |  | √ | ' ' | 主题状态,枚举: offLine :已下线 unannounced :待发布 announced :已发布 |
| 9 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改日期 |
| 11 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: singleDataSet :单数据集 multiDataSet :多数据集 |
| 12 | foriginpicture | 主题Logo | varchar | 255 |  | √ | ' ' | 主题Logo |
| 13 | fpredatapic | 预制数据 | varchar | 50 |  | √ | ' ' | 预制数据,枚举: true :预置数据 |
| 14 | fscheme | 主题类型 | varchar | 50 |  | √ | ' ' | 主题类型 |
| 15 | fdesc | 主题描述 | varchar | 50 |  | √ | ' ' | 主题描述 |
| 16 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 17 | ficoninfo | 图标详情 | varchar | 255 |  | √ | ' ' | 图标详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_cbi_single_scheme_id |  | fid |

---

## 单据体_数据集配置-子表 t_gai_cbi_theme_dataset

- **表名称：** 单据体_数据集配置-子表
- **表名：** t_gai_cbi_theme_dataset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatasetid | 数据集id | int8 | 64 |  | √ | 0 | 数据集id |
| 3 | fname | 数据集名称 | varchar | 255 |  | √ | ' ' | 数据集名称 |
| 4 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: enable :启用 disable :禁用 |
| 5 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改日期 |
| 7 | ftype | 数据源类型 | varchar | 50 |  | √ | ' ' | 数据源类型,枚举: 2 :本地文件 4 :业务对象 5 :数据库 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_theme_dataset_fid |  | fid |
| 2 | idx_theme_dataset_datasetid |  | fdatasetid |
| 3 | pk_gai_cbi_theme_dataset |  | fentryid |

---

## 展示配置单据体-子表 t_gai_cbi_show_config

- **表名称：** 展示配置单据体-子表
- **表名：** t_gai_cbi_show_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 推荐问法 | varchar | 255 |  | √ | ' ' | 推荐问法 |
| 3 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改日期 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 7 | fshortname | 推荐问法简称 | varchar | 255 |  | √ | ' ' | 推荐问法简称 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_cbi_show_config |  | fentryid |

---

## 单据体_业务提示词配置-子表 t_gai_cbi_prompt_config

- **表名称：** 单据体_业务提示词配置-子表
- **表名：** t_gai_cbi_prompt_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 1000 |  | √ | ' ' |  |
| 3 | fapplyscale | 适用范围 | varchar | 50 |  | √ | ' ' | 适用范围,枚举: all :全局适用 part :部分数据集适用 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改日期 |
| 9 | fname_tag | 业务提示词 | text | 0 |  |  | null | 业务提示词 |
| 10 | fsamplequestion | fsamplequestion | varchar | 1000 |  | √ | ' ' |  |
| 11 | fapplydataset | 适用数据集 | varchar | 1000 |  | √ | ' ' | 适用数据集,枚举: |
| 12 | fpromptstatus | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 13 | fsamplequestion_tag | 示例问题 | text | 0 |  |  | null | 示例问题 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_cbi_prompt_config_fid |  | fid |
| 2 | pk_t_gai_cbi_prompt_config_id |  | fentryid |

---

## 单据体_业务名词知识库-子表 t_gai_cbi_business_word

- **表名称：** 单据体_业务名词知识库-子表
- **表名：** t_gai_cbi_business_word

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 业务名词 | varchar | 50 |  | √ | ' ' | 业务名词 |
| 3 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbusinesstermstatus | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 7 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 8 | fdesc | 解释说明 | varchar | 2000 |  | √ | ' ' | 解释说明 |
| 9 | fsynonyms | 业务名词同义词 | varchar | 255 |  | √ | ' ' | 业务名词同义词 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_cbi_business_word_fid |  | fid |
| 2 | pk_t_gai_cbi_business_word_id |  | fentryid |

---

## 单据体_案例集-子表 t_gai_cbi_caseset

- **表名称：** 单据体_案例集-子表
- **表名：** t_gai_cbi_caseset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpectedsql | 期望执行的SQL | varchar | 3000 |  | √ | ' ' | 期望执行的SQL |
| 3 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fquestion | 用户问题 | varchar | 300 |  | √ | ' ' | 用户问题 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_cbi_caseset |  | fentryid |
| 2 | idx_t_gai_cbi_caseset_fid |  | fid |

---

## 单据体_字段语义配置-子表 t_gai_cbi_fieldconfig

- **表名称：** 单据体_字段语义配置-子表
- **表名：** t_gai_cbi_fieldconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatasetconfigid | 数据集配置id | int8 | 64 |  | √ | 0 | 数据集配置id |
| 3 | fdatasetid | 数据集id | int8 | 64 |  | √ | 0 | 数据集id |
| 4 | fname | 主题字段名称 | varchar | 50 |  | √ | ' ' | 主题字段名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 7 | foriginname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | ffieldid | 字段id | varchar | 50 |  | √ | ' ' | 字段id |
| 10 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fstatus | 字段有效性 | varchar | 50 |  | √ | ' ' | 字段有效性,枚举: enable :有效 disable :失效 |
| 12 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改日期 |
| 13 | fnumber | 字段编码 | varchar | 500 |  | √ | ' ' | 字段编码 |
| 14 | fdesc | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |
| 15 | findicator | 维度/指标 | varchar | 50 |  | √ | ' ' | 维度/指标,枚举: DIMENSION :维度 METRIC :指标 |
| 16 | fsynonyms | 字段同义词 | varchar | 255 |  | √ | ' ' | 字段同义词 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_cbi_fieldconfig_id |  | fentryid |
| 2 | idx_t_gai_cbi_fieldconfig_fid |  | fid |

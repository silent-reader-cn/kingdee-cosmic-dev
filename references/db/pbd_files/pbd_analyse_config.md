# 分析模板配置-pbd_analyse_config

## 指标维度过滤映射详细配置-多语言表 t_pbd_analysefillter_item_l

- **表名称：** 指标维度过滤映射详细配置-多语言表
- **表名：** t_pbd_analysefillter_item_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldname | 属性名称 | varchar | 255 |  | √ | ' ' | 属性名称 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_analysefillter_ite_fid |  | fdetailid |
| 2 | pk_pbd_analysefillter_item_l |  | fpkid |

---

## 指标维度过滤映射配置-子表 t_pbd_analysefillter

- **表名称：** 指标维度过滤映射配置-子表
- **表名：** t_pbd_analysefillter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffiltertype | 过滤类型 | varchar | 2 |  | √ | ' ' | 过滤类型,枚举: 1 :基础资料过滤 2 :开始时间过滤 3 :结束时间过滤 4 :自定义过滤器 |
| 3 | fpropertykey | 属性标识 | varchar | 50 |  | √ | ' ' | 属性标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ffilterclass | 自定义过滤器 | varchar | 512 |  | √ | ' ' | 自定义过滤器 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fpropertyname | 过滤字段名称 | varchar | 255 |  | √ | ' ' | 过滤字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_analysefillter |  | fentryid |
| 2 | idx_pbd_analysefillter_fid |  | fid |

---

## 分析模板配置-多语言表 t_pbd_analyse_config_l

- **表名称：** 分析模板配置-多语言表
- **表名：** t_pbd_analyse_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 255 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_analyse_config_l_fid |  | fid,flocaleid |
| 2 | pk_pbd_analyse_config_l |  | fpkid |

---

## 指标维度过滤映射配置-多语言表 t_pbd_analysefillter_l

- **表名称：** 指标维度过滤映射配置-多语言表
- **表名：** t_pbd_analysefillter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fpropertyname | 过滤字段名称 | varchar | 255 |  | √ | ' ' | 过滤字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_analysefillter_l |  | fpkid |
| 2 | idx_pbd_analysefillter_l_fid |  | fentryid,flocaleid |

---

## 分析模板配置-主表 t_pbd_analyse_config

- **表名称：** 分析模板配置-主表
- **表名：** t_pbd_analyse_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 模板名称 | varchar | 255 |  | √ | ' ' | 模板名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 模板编码 | varchar | 80 |  | √ | ' ' | 模板编码 |
| 10 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fanalysetpl | 分析模板页面 | varchar | 36 |  | √ | ' ' | [实体元数据 bos_entitymeta](../mdl_files/bos_entitymeta.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_analyse_config |  | fid |
| 2 | idx_pbd_analyse_config_num |  | fnumber |

---

## 指标维度过滤映射详细配置-子表 t_pbd_analysefillter_item

- **表名称：** 指标维度过滤映射详细配置-子表
- **表名：** t_pbd_analysefillter_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | findicatorid | 指标 | int8 | 64 |  | √ | 0 | [风险指标 pbd_indicator](../pbd_files/pbd_indicator.md) |
| 2 | ffieldname | 属性名称 | varchar | 255 |  | √ | ' ' | 属性名称 |
| 3 | ffield | 属性标识 | varchar | 50 |  | √ | ' ' | 属性标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_analysefillter_item_id |  | fentryid |
| 2 | pk_pbd_analysefillter_item |  | fdetailid |

---

## 卡片配置-子表 t_pbd_analyseconf_entry

- **表名称：** 卡片配置-子表
- **表名：** t_pbd_analyseconf_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcardid | 分析卡片ID | varchar | 50 |  | √ | ' ' | 分析卡片ID |
| 3 | fcardcompid | 卡片组件 | int8 | 64 |  | √ | 0 | [卡片组件 pbd_cardcomp](../pbd_files/pbd_cardcomp.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcardnumber | 卡片序号 | int4 | 32 |  | √ | 0 | 卡片序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_analyseconf_entry_fid |  | fid |
| 2 | pk_pbd_analyseconf_entry |  | fentryid |

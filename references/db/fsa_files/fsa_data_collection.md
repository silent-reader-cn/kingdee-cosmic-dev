# 数据集合-fsa_data_collection

## 数据集合-主表 t_fsa_datacollection

- **表名称：** 数据集合-主表
- **表名：** t_fsa_datacollection

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fdefaultfiltering | 启用默认过滤 | bpchar | 1 |  | √ | ' ' | 启用默认过滤 |
| 5 | fdatasrctype | 数据源类型 | varchar | 50 |  | √ | ' ' | 数据源类型,枚举: 0 :自定义 bcmParamSource :星瀚合并报表 2 :星瀚预算 3 :星瀚总账 fileParamSource :导入离线数据 |
| 6 | fdescription | 描述信息 | varchar | 255 |  | √ | ' ' | 描述信息 |
| 7 | fparamsrc | 来源参数 | varchar | 255 |  | √ | ' ' | 来源参数 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fallowdimnull | 允许默认度量值为空 | bpchar | 1 |  | √ | ' ' | 允许默认度量值为空 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fparamsrc_tag | 来源参数_详情 | text | 0 |  |  | null | 来源参数_详情 |
| 14 | fsuperlongdata | 支持超长数据值 | bpchar | 1 |  | √ | '0' | 支持超长数据值 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fparamsrcname | 来源参数 | varchar | 255 |  | √ | ' ' | 来源参数 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_datacollection |  | fid |
| 2 | idx_fsa_datacollection_1 |  | fenable,fdatasrctype |

---

## 数据集合-多语言表 t_fsa_datacollection_l

- **表名称：** 数据集合-多语言表
- **表名：** t_fsa_datacollection_l

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
| 1 | idx_fsa_datacollection_l |  | fid,flocaleid |
| 2 | pk_t_fsa_datacollection_l |  | fpkid |

---

## 组合字段的映射关系分录-子表 t_fsa_datacolcombmappings

- **表名称：** 组合字段的映射关系分录-子表
- **表名：** t_fsa_datacolcombmappings

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsrcfieldmemname | 组合来源字段成员名称 | varchar | 500 |  | √ | ' ' | 组合来源字段成员名称 |
| 2 | fsrcfieldname | 组合来源字段名称 | varchar | 50 |  | √ | ' ' | 组合来源字段名称 |
| 3 | fsrcfieldmemnumber | 组合来源字段成员编码 | varchar | 50 |  | √ | ' ' | 组合来源字段成员编码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsrcfieldnumber | 组合来源字段编码 | varchar | 50 |  | √ | ' ' | 组合来源字段编码 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fdatatype | 数据类型 | bpchar | 1 |  | √ | ' ' | 数据类型,枚举: 0 :日期 1 :基础资料 2 :浮点数 3 :整数 4 :字符 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_datacolcombmappings_1 |  | fseq,fsrcfieldnumber,fsrcfieldmemnumber |
| 2 | pk_t_fsa_datacolcombmappings |  | fdetailid |
| 3 | idx_fsa_datacolcombmappings_2 |  | fdatatype |

---

## 数据集合单据体-子表 t_fsa_datacolfields

- **表名称：** 数据集合单据体-子表
- **表名：** t_fsa_datacolfields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 维度名称 | varchar | 50 |  | √ | ' ' | 维度名称 |
| 3 | fdimtype | 维度类型 | bpchar | 1 |  | √ | ' ' | 维度类型,枚举: 1 :维度 2 :度量 0 :日期 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsrcname | 源字段名称 | varchar | 50 |  | √ | ' ' | 源字段名称 |
| 6 | fnumber | 维度编码 | varchar | 50 |  | √ | ' ' | 维度编码 |
| 7 | ffieldcreatetype | 创建方式 | bpchar | 1 |  | √ | ' ' | 创建方式,枚举: 0 :手动添加 1 :源字段 2 :组合字段 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fdimid | 源字段维度ID | int8 | 64 |  | √ | 0 | 源字段维度ID |
| 10 | fsrcnumber | 源字段编码 | varchar | 50 |  | √ | ' ' | 源字段编码 |
| 11 | fdatatype | 数据类型 | bpchar | 1 |  | √ | ' ' | 数据类型,枚举: 0 :日期 1 :基础资料 2 :浮点数 3 :整数 4 :字符 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_datacolfields |  | fentryid |
| 2 | idx_fsa_datacolfields_1 |  | fid,fsrcnumber |

---

## 字段参数设置子分录-子表 t_fsa_datacolfieldparam

- **表名称：** 字段参数设置子分录-子表
- **表名：** t_fsa_datacolfieldparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvalue | 参数值 | varchar | 50 |  | √ | ' ' | 参数值 |
| 2 | fparamnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_datacolfieldparam |  | fdetailid |
| 2 | idx_fsa_datacolfieldparam_1 |  | fentryid,fparamnumber |

---

## 数据集合-组合字段-子表 t_fsa_datacolcombfields

- **表名称：** 数据集合-组合字段-子表
- **表名：** t_fsa_datacolcombfields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcombofieldfname | 组合来源字段名称 | text | 0 |  |  | null | 组合来源字段名称 |
| 3 | fcombofieldnumber | 组合来源字段编码 | text | 0 |  |  | null | 组合来源字段编码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdatatype | 数据类型 | bpchar | 1 |  | √ | ' ' | 数据类型,枚举: 0 :日期 1 :基础资料 2 :浮点数 3 :整数 4 :字符 |
| 7 | fcombinationid | 组合字段ID | int8 | 64 |  | √ | 0 | 组合字段ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_datacolcombfields |  | fentryid |
| 2 | idx_fsa_datacolcombfields_1 |  | fid |

---

## 源字段集合-子表 t_fsa_datacolsrcfilter

- **表名称：** 源字段集合-子表
- **表名：** t_fsa_datacolsrcfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldnumber | 维度编码 | varchar | 50 |  | √ | ' ' | 维度编码 |
| 3 | fvalue | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 4 | ffielddimtype | 维度类型 | varchar | 50 |  | √ | ' ' | 维度类型,枚举: 1 :维度 2 :度量 0 :日期 |
| 5 | ffieldtype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: 0 :日期 1 :基础资料 2 :浮点数 3 :整数 4 :字符 |
| 6 | ffieldname | 维度名称 | varchar | 50 |  | √ | ' ' | 维度名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fvaluename | 默认值名称 | varchar | 500 |  | √ | ' ' | 默认值名称 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fsa_datacolsrcfilter_1 |  | fid,ffieldnumber |
| 2 | pk_t_fsa_datacolsrcfilter |  | fentryid |

# 全文检索映射属性-pbd_esmapping_property

## 嵌套属性-多选基础资料表 t_pbd_esmappingprop_nests

- **表名称：** 嵌套属性-多选基础资料表
- **表名：** t_pbd_esmappingprop_nests

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [全文检索映射属性 pbd_esmapping_property](../pbd_files/pbd_esmapping_property.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_esprop_nests_fid |  | fid |
| 2 | pk_t_pbd_esmappingprop_nests |  | fpkid |

---

## 全文检索映射属性-主表 t_pbd_esmappingprop

- **表名称：** 全文检索映射属性-主表
- **表名：** t_pbd_esmappingprop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdynamic | dynamic | varchar | 50 |  | √ | ' ' | dynamic,枚举: true :true false :false strict :strict |
| 3 | fformat | format | varchar | 50 |  | √ | ' ' | format,枚举: yyyy-MM-dd :yyyy-MM-dd |
| 4 | fnullvalue | null_value | varchar | 50 |  | √ | ' ' | null_value,枚举: |
| 5 | ffielddata | fielddata | varchar | 50 |  | √ | ' ' | fielddata,枚举: true :true false :false |
| 6 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcoerce | coerce | varchar | 50 |  | √ | ' ' | coerce,枚举: true :true false :false |
| 12 | fdefaultvalue | 默认值 | varchar | 255 |  | √ | ' ' | 默认值 |
| 13 | ftermvector | term_vector | varchar | 50 |  | √ | ' ' | term_vector,枚举: |
| 14 | fboost | 查询权重 | numeric | 23 | 10 | √ | 0 | 查询权重 |
| 15 | fenabled | enabled | varchar | 50 |  | √ | ' ' | enabled,枚举: true :true false :false |
| 16 | fsimilarity | similarity | varchar | 50 |  | √ | ' ' | similarity,枚举: BM25 :BM25 classic :classic boolean :boolean |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | es属性名称 | varchar | 255 |  | √ | ' ' | es属性名称 |
| 19 | fstore | store | varchar | 50 |  | √ | ' ' | store,枚举: true :true false :false |
| 20 | findexentityid | 索引实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | festokenizertype | 字段分词类型 | varchar | 50 |  | √ | ' ' | 字段分词类型,枚举: standard :标准分词 ik_smart :中文粗粒度分词 ik_max_word :中文细粒度分词 ngram_analyzer :n元分词 |
| 23 | findex | index | varchar | 50 |  | √ | ' ' | index,枚举: true :true false :false |
| 24 | fcopyto | copy_to | varchar | 50 |  | √ | ' ' | copy_to,枚举: full_name :full_name |
| 25 | fwithpinyin | 支持拼音检索 | bpchar | 1 |  | √ | '0' | 支持拼音检索 |
| 26 | findexoptions | index_options | varchar | 50 |  | √ | ' ' | index_options,枚举: docs :docs freqs :freqs positions :positions offsets :offsets |
| 27 | feagerglobalordinals | eager_global_ordinals | varchar | 50 |  | √ | ' ' | eager_global_ordinals,枚举: true :true false :false |
| 28 | fignoreabove | ignore_above | varchar | 50 |  | √ | ' ' | ignore_above,枚举: 256 :256 |
| 29 | fignoremalformed | ignore_malformed | varchar | 50 |  | √ | ' ' | ignore_malformed,枚举: true :true false :false |
| 30 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | es属性编码 | varchar | 80 |  | √ | ' ' | es属性编码 |
| 32 | fdocvalues | doc_values | varchar | 50 |  | √ | ' ' | doc_values,枚举: true :true false :false |
| 33 | fmeta | meta | varchar | 50 |  | √ | ' ' | meta,枚举: |
| 34 | fnormalizer | normalizer | varchar | 50 |  | √ | ' ' | normalizer,枚举: |
| 35 | fmappingfield | 映射字段 | varchar | 50 |  | √ | ' ' | 映射字段 |
| 36 | fsearchanalyzer | search_analyzer | varchar | 50 |  | √ | ' ' | search_analyzer,枚举: |
| 37 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: text :文本 keyword :关键词 nested :嵌套 date :日期 boolean :布尔值 long :长整数 integer :整数 short :短整数 byte :字节 float :浮点数 double :小数 range :范围 object :对象 array :数组 attachment :附件 combo :下拉 completion :自动补全 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_esmappingprop |  | fid |
| 2 | idx_pbd_esmappingprop_fnumber |  | fnumber |

---

## 全文检索映射属性-多语言表 t_pbd_esmappingprop_l

- **表名称：** 全文检索映射属性-多语言表
- **表名：** t_pbd_esmappingprop_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | es属性名称 | varchar | 255 |  | √ | ' ' | es属性名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_esmappingprop_l_fid |  | fid |
| 2 | pk_t_pbd_esmappingprop_l |  | fpkid |

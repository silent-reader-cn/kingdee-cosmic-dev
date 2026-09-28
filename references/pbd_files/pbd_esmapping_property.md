# 全文检索映射属性-pbd_esmapping_property

## 嵌套属性-多选基础资料表 t_pbd_esmappingprop_nests

- **表名称：** 嵌套属性-多选基础资料表
- **表名：** t_pbd_esmappingprop_nests

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 全文检索映射属性 pbd_esmapping_property |
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
| 2 | fname | es属性名称 | varchar | 100 |  | √ | ' ' | es属性名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | findexentityid | 索引实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | festokenizertype | 字段分词类型 | varchar | 50 |  | √ | ' ' | 字段分词类型,枚举: standard :标准分词 ik_smart :中文粗粒度分词 ik_max_word :中文细粒度分词 ngram_analyzer :n元分词 |
| 7 | fwithpinyin | 支持拼音检索 | bpchar | 1 |  | √ | '0' | 支持拼音检索 |
| 8 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fdefaultvalue | 默认值 | varchar | 255 |  | √ | ' ' | 默认值 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fboost | 查询权重 | numeric | 23 | 10 | √ | 0 | 查询权重 |
| 16 | fnumber | es属性编码 | varchar | 80 |  | √ | ' ' | es属性编码 |
| 17 | fmappingfield | 映射字段 | varchar | 50 |  | √ | ' ' | 映射字段 |
| 18 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: text :文本 keyword :关键词 nested :嵌套 date :日期 boolean :布尔值 long :长整数 integer :整数 short :短整数 byte :字节 float :浮点数 double :小数 range :范围 object :对象 array :数组 attachment :附件 combo :下拉 completion :自动补全 |

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
| 2 | fname | es属性名称 | varchar | 100 |  | √ | ' ' | es属性名称 |
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

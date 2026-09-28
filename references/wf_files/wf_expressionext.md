# 对象扩展属性-wf_expressionext

## 对象扩展属性-多语言表 t_wf_expressionext_l

- **表名称：** 对象扩展属性-多语言表
- **表名：** t_wf_expressionext_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_expressionext_fid |  | fid |
| 2 | t_wf_expressionext_l_pkey |  | fpkid |

---

## 对象扩展属性-主表 t_wf_expressionext

- **表名称：** 对象扩展属性-主表
- **表名：** t_wf_expressionext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 3 | fgroupid | 分组名 | varchar | 100 |  | √ | ' ' | 分组名 |
| 4 | fispreinsdata | 是否预置数据 | bpchar | 1 |  | √ | '0' | 是否预置数据 |
| 5 | fvaluecomboitems | 结果下拉列表 | varchar | 2000 |  | √ | ' ' | 结果下拉列表 |
| 6 | fcontroltype | 空间类型 | varchar | 100 |  | √ | ' ' | 空间类型 |
| 7 | fentitynumber | 实体编码 | varchar | 100 |  | √ | ' ' | 实体编码 |
| 8 | fparseclass | 解析类 | varchar | 255 |  | √ | ' ' | 解析类 |
| 9 | fvaluetype | 值类型 | varchar | 100 |  | √ | ' ' | 值类型 |
| 10 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 11 | fhasquotes | 值是否有引号 | bpchar | 1 |  | √ | '0' | 值是否有引号 |
| 12 | fvalueentitynumber | （结果）实体编码 | varchar | 100 |  | √ | ' ' | （结果）实体编码 |
| 13 | fexpressiontemplate | 表达式模板 | varchar | 100 |  | √ | ' ' | 表达式模板 |
| 14 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 16 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fusecount | 使用次数 | int8 | 64 |  | √ | 0 | 使用次数 |
| 18 | forder | 顺序 | int8 | 64 |  | √ | 0 | 顺序 |
| 19 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 20 | fcomparetype | 比较符类型 | varchar | 100 |  | √ | ' ' | 比较符类型 |
| 21 | fstructurenumber | 结构编码 | varchar | 100 |  | √ | ' ' | 结构编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_expressionext_pkey |  | fid |
| 2 | idx_wf_expressionext |  | fentitynumber |

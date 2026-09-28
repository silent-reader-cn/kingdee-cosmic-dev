# 辅助属性值范围-bd_auxptyvalue

## 属性值-子表 t_bd_auxptyvalueentry

- **表名称：** 属性值-子表
- **表名：** t_bd_auxptyvalueentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisenable | 启用 | bpchar | 1 |  | √ | ' ' | 启用 |
| 3 | fassistantid | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fapvaluenames | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 6 | fapvaluenum | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fauxptyvalueid | 辅助属性值ID | int8 | 64 |  | √ | 0 | 辅助属性值ID |
| 9 | fapvaluename | 文本名称 | varchar | 100 |  | √ | ' ' | 文本名称 |
| 10 | fisdefault | 默认值 | bpchar | 1 |  | √ | ' ' | 默认值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_auxptyvalueentry_fid |  | fid |
| 2 | t_bd_auxptyvalueentry_pkey |  | fentryid |

---

## 属性值-多语言表 t_bd_auxptyvalueentry_l

- **表名称：** 属性值-多语言表
- **表名：** t_bd_auxptyvalueentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fapvaluenames | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fapvaluename | fapvaluename | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_auxptyvalueentry_l_fid |  | fentryid,flocaleid |
| 2 | t_bd_auxptyvalueentry_l_pkey |  | fpkid |

---

## 辅助属性值范围-主表 t_bd_auxptyvalue

- **表名称：** 辅助属性值范围-主表
- **表名：** t_bd_auxptyvalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | [辅助属性定义 bd_auxproperty](../sbd_files/bd_auxproperty.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_auxptyvalue_pkey |  | fid |
| 2 | idx_bd_auxptyvalue_mataux |  | fmaterialid,fauxptyid |

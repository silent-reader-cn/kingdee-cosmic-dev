# 维度-xkrpt_dimension

## 维度-多语言表 t_xkrpt_dimension_l

- **表名称：** 维度-多语言表
- **表名：** t_xkrpt_dimension_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmuliconditionname | 过滤条件多语言 | varchar | 570 |  | √ | ' ' | 过滤条件多语言 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkrpt_dimension_l |  | fid |
| 2 | pk_t_xkrpt_dimension_l |  | fpkid |

---

## 维度-主表 t_xkrpt_dimension

- **表名称：** 维度-主表
- **表名：** t_xkrpt_dimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparentfield | 上级字段 | varchar | 50 |  | √ | ' ' | 上级字段,枚举: |
| 3 | fassistantdatatype | 对应辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料分类 bos_assistantdatagroup](../base_files/bos_assistantdatagroup.md) |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fbasedatatype | 对应基础资料 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 10 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcategory | 维度类型 | varchar | 30 |  | √ | ' ' | 维度类型,枚举: 1 :基础资料 2 :辅助资料 |
| 14 | fparentfieldname | 上级字段名称 | varchar | 50 |  | √ | ' ' | 上级字段名称 |
| 15 | fmultitiered | 多层级维度 | bpchar | 1 |  | √ | '0' | 多层级维度 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fconditionjson | 过滤条件json | varchar | 2000 |  | √ | ' ' | 过滤条件json |
| 18 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 19 | fbasedatavalue | 对应基础资料值 | varchar | 50 |  | √ | ' ' | 对应基础资料值 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fconditionname | 过滤条件 | varchar | 570 |  | √ | ' ' | 过滤条件 |
| 22 | fmuliconditionname | 过滤条件多语言 | varchar | 570 |  | √ | ' ' | 过滤条件多语言 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 25 | frefdimautocreate | 多层级维度自动生成 | bpchar | 1 |  | √ | '0' | 多层级维度自动生成 |
| 26 | fconditionsql | 过滤条件sql | varchar | 2000 |  | √ | ' ' | 过滤条件sql |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_dimension_fnumber |  | fnumber |
| 2 | pk_t_xkrpt_dimension |  | fid |

---

## 关联的多层级维度-子表 t_xkrpt_relationdim

- **表名称：** 关联的多层级维度-子表
- **表名：** t_xkrpt_relationdim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frefdimnumber | 维度编码 | varchar | 30 |  | √ | ' ' | 维度编码 |
| 3 | flevel | 级次 | varchar | 5 |  | √ | '2' | 级次,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 |
| 4 | frefdim | 多层级维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frefdimname | 维度名称 | varchar | 570 |  | √ | ' ' | 维度名称 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_relationdim_fid |  | fid |
| 2 | pk_xkrpt_relationdim |  | fentryid |

---

## 关联的多层级维度-多语言表 t_xkrpt_relationdim_l

- **表名称：** 关联的多层级维度-多语言表
- **表名：** t_xkrpt_relationdim_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | frefdimname | 维度名称 | varchar | 570 |  | √ | ' ' | 维度名称 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_relationdim_l |  | fpkid |
| 2 | idx_xkrpt_relationdim_l |  | fentryid,flocaleid |

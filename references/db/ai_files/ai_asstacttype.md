# 业务维度-ai_asstacttype

## 业务维度-主表 t_ai_asstacttype

- **表名称：** 业务维度-主表
- **表名：** t_ai_asstacttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fdisplayproperty | 显示属性 | bpchar | 1 |  | √ | ' ' | 显示属性,枚举: 1 :编码 2 :名称 3 :编码+名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | findex | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 7 | fflexfiled | 后台编码 | varchar | 50 |  | √ | ' ' | 后台编码 |
| 8 | fasstacttype | 维度分类 | bpchar | 1 |  | √ | ' ' | 维度分类,枚举: 1 :维度 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fassistanttype | 值来源 | int8 | 64 |  | √ | 0 | [辅助资料分类 bos_assistantdatagroup](../base_files/bos_assistantdatagroup.md) |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fvaluesource | 值来源 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fdatatype | 数据类型 | bpchar | 1 |  | √ | ' ' | 数据类型,枚举: 1 :基础资料 2 :辅助资料 3 :文本 4 :布尔 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_asstacttype |  | fnumber |
| 2 | idx_ai_asstacttype_index |  | findex |
| 3 | pk_t_ai_asstacttype |  | fid |

---

## 业务维度-多语言表 t_ai_asstacttype_l

- **表名称：** 业务维度-多语言表
- **表名：** t_ai_asstacttype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ai_asstacttype_l_lid |  | fid |
| 2 | pk_t_ai_asstacttype_l |  | fpkid |

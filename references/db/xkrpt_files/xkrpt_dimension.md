# 维度-xkrpt_dimension

## 维度-多语言表 t_xkrpt_dimension_l

- **表名称：** 维度-多语言表
- **表名：** t_xkrpt_dimension_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

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
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcategory | 维度类型 | varchar | 30 |  | √ | ' ' | 维度类型,枚举: 1 :基础资料 2 :辅助资料 |
| 5 | fparentfield | 上级字段 | varchar | 50 |  | √ | ' ' | 上级字段,枚举: |
| 6 | fparentfieldname | 上级字段名称 | varchar | 50 |  | √ | ' ' | 上级字段名称 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 9 | fassistantdatatype | 对应辅助资料 | int8 | 64 |  | √ | 0 | 辅助资料分类 bos_assistantdatagroup |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbasedatavalue | 对应基础资料值 | varchar | 50 |  | √ | ' ' | 对应基础资料值 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fbasedatatype | 对应基础资料 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 19 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 20 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_dimension_fnumber |  | fnumber |
| 2 | pk_t_xkrpt_dimension |  | fid |

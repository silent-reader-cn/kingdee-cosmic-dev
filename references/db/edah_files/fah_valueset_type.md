# 外部数据值集-fah_valueset_type

## 外部数据值集-主表 t_fah_valueset_type

- **表名称：** 外部数据值集-主表
- **表名：** t_fah_valueset_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fstrucid | 值集扩展字段 | int8 | 64 |  | √ | 0 | 值集扩展字段定义 fah_flex_struc_type |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 8 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fah_valueset_type_no |  | fnumber |
| 2 | pk_t_fah_valueset_type |  | fid |

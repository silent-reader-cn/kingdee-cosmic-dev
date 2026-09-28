# 数据类型-fea_datatype

## 数据类型-主表 t_fea_datatype

- **表名称：** 数据类型-主表
- **表名：** t_fea_datatype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftotallength | 总位数 | int8 | 64 |  | √ | 0 | 总位数 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fintegerlength | 位数 | int8 | 64 |  | √ | 0 | 位数 |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | flength | 长度 | int8 | 64 |  | √ | 0 | 长度 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fcomments | 注释 | varchar | 255 |  | √ | ' ' | 注释 |
| 9 | fdecimallength | 小数位数 | int8 | 64 |  | √ | 0 | 小数位数 |
| 10 | fdescription | 值范围 | varchar | 255 |  | √ | ' ' | 值范围 |
| 11 | flengthrange | 长度范围 | bpchar | 1 |  | √ | ' ' | 长度范围,枚举: 0 :固定值 1 :最大值 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstandardid | 文件标准 | int8 | 64 |  | √ | 0 | [文件标准 fea_standard](../fea_files/fea_standard.md) |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fformatter | 格式 | varchar | 30 |  | √ | ' ' | 格式,枚举: |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_datatype |  | fid |
| 2 | idx_fea_datatype |  | fstandardid |

---

## 数据类型-多语言表 t_fea_datatype_l

- **表名称：** 数据类型-多语言表
- **表名：** t_fea_datatype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 值范围 | varchar | 255 |  | √ | ' ' | 值范围 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fea_datatype_l |  | fid,flocaleid |
| 2 | pk_t_fea_datatype_l |  | fpkid |

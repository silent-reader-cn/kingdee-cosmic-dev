# 信息提取通用提取表-cvp_ie_extract_common

## 信息提取通用提取表-多语言表 t_cvp_ie_common_l

- **表名称：** 信息提取通用提取表-多语言表
- **表名：** t_cvp_ie_common_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_ie_common_l |  | fid |
| 2 | pk_t_cvp_ie_common_l |  | fpkid |

---

## 信息提取通用提取表-主表 t_cvp_ie_common

- **表名称：** 信息提取通用提取表-主表
- **表名：** t_cvp_ie_common

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fextractnum | 提取编码 | varchar | 50 |  | √ | ' ' | 提取编码 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fextractfield | 提取字段 | varchar | 50 |  |  | null | 提取字段 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftabnum | 表编码 | varchar | 50 |  |  | null | 表编码 |
| 8 | fexdescription | 字段描述 | varchar | 255 |  |  | null | 字段描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 13 | ftabname | 表名称 | varchar | 60 |  |  | null | 表名称 |
| 14 | ffieldtype | 字段类型 | int8 | 64 |  |  | null | [提取字段类型 cvp_field_types](../cvp_files/cvp_field_types.md) |
| 15 | fenable | 使用状态 | varchar | 50 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_ie_common |  | fextractnum,ftabnum |
| 2 | pk_t_cvp_ie_common |  | fid |

# 信息提取方案-cvp_ie_mouldplan

## 信息提取方案-多语言表 t_cvp_ie_mould_l

- **表名称：** 信息提取方案-多语言表
- **表名：** t_cvp_ie_mould_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 50 |  |  | null | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_ie_mould_l |  | fpkid |
| 2 | idx_t_cvp_ie_mould_l |  | fname |

---

## 信息提取方案-主表 t_cvp_ie_mould

- **表名称：** 信息提取方案-主表
- **表名：** t_cvp_ie_mould

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 50 |  |  | null | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 方案说明 | varchar | 255 |  |  | null | 方案说明 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 10 | fissys | 是否预置 | bpchar | 1 |  |  | null | 是否预置 |
| 11 | fenable | 使用状态 | varchar | 50 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fbusinessconfig | 所属领域 | varchar | 50 |  |  | null | 所属领域,枚举: A :通用合同 |
| 13 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_ie_mould |  | fid |
| 2 | inx_t_cvp_ie_mould |  | fnumber,fname |

---

## -子表 t_cvp_ie_extracfield

- **表名称：** -子表
- **表名：** t_cvp_ie_extracfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fextractnum | 提取编码 | varchar | 50 |  | √ | ' ' | 提取编码 |
| 3 | ftabname | 表名称 | varchar | 60 |  |  | null | 表名称 |
| 4 | fextractfield | 提取字段 | varchar | 50 |  |  | null | 提取字段 |
| 5 | ffieldtype | 字段类型 | int8 | 64 |  |  | null | 提取字段类型 cvp_field_types |
| 6 | ftabnum | 表编码 | varchar | 50 |  |  | null | 表编码 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fexdescription | 字段描述 | varchar | 255 |  |  | null | 字段描述 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cvp_ie_extracfield |  | fextractfield,ffieldtype |
| 2 | pk_t_cvp_ie_extracfield |  | fentryid |

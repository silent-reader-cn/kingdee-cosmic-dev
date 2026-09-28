# 文件类型-mpdm_doctype

## 文件类型-多语言表 t_mpdm_doctype_l

- **表名称：** 文件类型-多语言表
- **表名：** t_mpdm_doctype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_doctype_l_0 |  | fid,flocaleid |
| 2 | pk_mpdm_doctype_l |  | fpkid |

---

## 单据体-子表 t_mpdm_docrule

- **表名称：** 单据体-子表
- **表名：** t_mpdm_docrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightsymbol | 符号 | varchar | 50 |  | √ | ' ' | 符号,枚举: ) :) )) :)) ))) :))) |
| 3 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 4 | fcomparesymbol | 比较符 | varchar | 50 |  | √ | ' ' | 比较符,枚举: = :等于 != :不等于 |
| 5 | fmanufacturerid | 制造商 | int8 | 64 |  | √ | 0 | [制造商 mpdm_manufacturer](../mpdm_files/mpdm_manufacturer.md) |
| 6 | ffield | 字段 | varchar | 50 |  | √ | ' ' | 字段,枚举: modelone :型号L1 modelmpdone :型号L1-MPD modeltwo :型号L2 modeltrd :型号L3 manufacturer :制造商编码 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | flinksymbol | 连接符 | varchar | 50 |  | √ | ' ' | 连接符,枚举: and :且 or :或 |
| 9 | fleftsymbol | 符号 | varchar | 50 |  | √ | ' ' | 符号,枚举: ( :( (( :(( ((( :((( |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_docrule |  | fentryid |
| 2 | idx_mpdm_docrule |  | fid |

---

## 文件类型-主表 t_mpdm_doctype

- **表名称：** 文件类型-主表
- **表名：** t_mpdm_doctype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | ffilterruler | 过滤规则 | varchar | 255 |  | √ | ' ' | 过滤规则 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ffilterruler_tag | 过滤规则_详情 | text | 0 |  |  | null | 过滤规则_详情 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_doctype |  | fid |
| 2 | idx_mpdm_doctype_fnumber |  | fnumber |

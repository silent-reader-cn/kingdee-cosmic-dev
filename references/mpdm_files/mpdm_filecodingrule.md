# 文件编码规则-mpdm_filecodingrule

## 文件编码规则-主表 t_mpdm_filecodingrule

- **表名称：** 文件编码规则-主表
- **表名：** t_mpdm_filecodingrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcodingobj | 编码对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | ffilterruler | 过滤规则 | varchar | 255 |  | √ | ' ' | 过滤规则 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ffilterruler_tag | 过滤规则_详情 | text | 0 |  |  | null | 过滤规则_详情 |
| 13 | fdoctype | 文件类型 | int8 | 64 |  | √ | 0 | 文件类型 mpdm_doctype |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_filecodingrule_n |  | fnumber |
| 2 | idx_mpdm_filecodingrule_d |  | fdoctype |
| 3 | pk_mpdm_filecodingrule |  | fid |

---

## 适用规则-子表 t_mpdm_filecodfilter

- **表名称：** 适用规则-子表
- **表名：** t_mpdm_filecodfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frightsymbol | 符号 | varchar | 50 |  | √ | ' ' | 符号,枚举: ) :) )) :)) ))) :))) |
| 3 | fvalue | 值 | varchar | 50 |  | √ | ' ' | 值 |
| 4 | fcomparesymbol | 比较符 | varchar | 50 |  | √ | ' ' | 比较符,枚举: = :等于 != :不等于 |
| 5 | fmanufacturerid | 制造商 | int8 | 64 |  | √ | 0 | 制造商 mpdm_manufacturer |
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
| 1 | pk_mpdm_filecodfilter |  | fentryid |
| 2 | idx_mpdm_filecodfilter |  | fid |

---

## 文件编码规则-多语言表 t_mpdm_filecodingrule_l

- **表名称：** 文件编码规则-多语言表
- **表名：** t_mpdm_filecodingrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_filecodingrule_l |  | fid,flocaleid |
| 2 | pk_mpdm_filecodingrule_l |  | fpkid |

---

## 编码规则-子表 t_mpdm_filecodeentry

- **表名称：** 编码规则-子表
- **表名：** t_mpdm_filecodeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freffield | 引用字段 | varchar | 50 |  | √ | ' ' | 引用字段 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: constant :常量 text :文本 qty :整数 refprop :引用属性 |
| 4 | ftrunctype | 截断方式 | varchar | 50 |  | √ | ' ' | 截断方式,枚举: left :左侧 right :右侧 |
| 5 | fdefalutvalue | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 6 | fconstantvalue | 常量值 | varchar | 10 |  | √ | ' ' | 常量值 |
| 7 | ffieldlenth | 字段长度 | int8 | 64 |  | √ | 0 | 字段长度 |
| 8 | flinkcode | 链接码 | varchar | 50 |  | √ | ' ' | 链接码 |
| 9 | fqtyrange | 数值范围 | varchar | 50 |  | √ | ' ' | 数值范围 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_filecodeentry |  | fentryid |
| 2 | idx_mpdm_filecodeentry |  | fid |

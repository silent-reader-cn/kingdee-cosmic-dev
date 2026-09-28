# 地址格式-cts_addressconfig

## 单据体1-子表 t_cts_addrconfigformat

- **表名称：** 单据体1-子表
- **表名：** t_cts_addrconfigformat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fisnewline | 另起一行 | bpchar | 1 |  | √ | ' ' | 另起一行 |
| 5 | fprefix | 前缀 | varchar | 30 |  | √ | ' ' | 前缀 |
| 6 | fcontainblank | 空格分隔符 | bpchar | 1 |  | √ | '0' | 空格分隔符 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fseq | 分录行号 | int2 | 16 |  | √ | 0 | 分录行号 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fpreconfigid | 字段名称 | int8 | 64 |  | √ | 0 | 地址字段 cts_addresspreconfig |
| 11 | freplaceattr | 使用属性替代 | int8 | 64 |  | √ | 0 | 控件属性替代 cts_address_attr |
| 12 | fsuffix | 后缀 | varchar | 30 |  | √ | ' ' | 后缀 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fisinclude | 包含 | bpchar | 1 |  | √ | ' ' | 包含 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cts_addrconfigformat |  | fentryid |
| 2 | idx_cts_addrconfigformat_fid |  | fid |

---

## 国家或地区-多选基础资料表 t_cts_addrconfigcountry

- **表名称：** 国家或地区-多选基础资料表
- **表名：** t_cts_addrconfigcountry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cts_addrconfigcountry_fid |  | fid,fbasedataid |
| 2 | pk_cts_addrconfigcountry |  | fpkid |

---

## 地址格式-多语言表 t_cts_addressconfig_l

- **表名称：** 地址格式-多语言表
- **表名：** t_cts_addressconfig_l

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
| 1 | idx_cts_addressconfig_l |  | fid,flocaleid |
| 2 | pk_cts_addressconfig_l |  | fpkid |

---

## 地址格式-主表 t_cts_addressconfig

- **表名称：** 地址格式-主表
- **表名：** t_cts_addressconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fiscontainadmin | 包含行政区划 | bpchar | 1 |  | √ | ' ' | 包含行政区划 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fadminlevel | 包含级次 | varchar | 10 |  | √ | ' ' | 包含级次,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fisdefault | 默认格式 | bpchar | 1 |  | √ | ' ' | 默认格式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cts_addrcfg_fnumber |  | fnumber |
| 2 | pk_cts_addressconfig |  | fid |

---

## 单据体-子表 t_cts_addrconfigstruct

- **表名称：** 单据体-子表
- **表名：** t_cts_addrconfigstruct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fisrequired | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fisnewline | 另起一行 | bpchar | 1 |  | √ | ' ' | 另起一行 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fseq | 分录行号 | int2 | 16 |  | √ | 0 | 分录行号 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fpreconfigid | 字段名称 | int8 | 64 |  | √ | 0 | 地址字段 cts_addresspreconfig |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | flengthspec | 长度 | varchar | 10 |  | √ | ' ' | 长度,枚举: 1 :短 2 :中 3 :长 |
| 13 | fuserdefinetag | 自定义标签 | varchar | 50 |  | √ | ' ' | 自定义标签 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fisshow | 显示 | bpchar | 1 |  | √ | ' ' | 显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cts_addrconfigstruct_fid |  | fid |
| 2 | pk_cts_addrconfigstruct |  | fentryid |

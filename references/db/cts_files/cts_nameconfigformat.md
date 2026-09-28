# 姓名文本格式-cts_nameconfigformat

## 单据体2-子表 t_cts_nameconfigcountries

- **表名称：** 单据体2-子表
- **表名：** t_cts_nameconfigcountries

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 5 | fcountry | 国家地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cts_ncc_country |  | fcountry |
| 2 | pk_t_cts_nameconfigcountries |  | fentryid |

---

## 国家或地区-多选基础资料表 t_cts_nameconfigcountry

- **表名称：** 国家或地区-多选基础资料表
- **表名：** t_cts_nameconfigcountry

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
| 1 | pk_cts_nameconfigcountry |  | fpkid |
| 2 | idx_t_cts_namecfgcy_fid |  | fid,fbasedataid |

---

## 姓名文本格式-多语言表 t_cts_nametextconfig_l

- **表名称：** 姓名文本格式-多语言表
- **表名：** t_cts_nametextconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cts_nametextcfg_l_fid |  | fid,flocaleid |
| 2 | pk_cts_nametextconfig_l |  | fpkid |

---

## 单据体1-子表 t_cts_nameconfigformat

- **表名称：** 单据体1-子表
- **表名：** t_cts_nameconfigformat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisspaceseperator | 空格分隔符 | bpchar | 1 |  | √ | '0' | 空格分隔符 |
| 3 | fprefix | 前缀 | varchar | 50 |  | √ | ' ' | 前缀 |
| 4 | fseq | 分录行号 | int2 | 16 |  | √ | 0 | 分录行号 |
| 5 | fpreconfigid | 字段名称 | int8 | 64 |  | √ | 0 | 姓名预置字段 cts_nameprefield |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fisinclude | 包含于姓名 | bpchar | 1 |  | √ | '0' | 包含于姓名 |
| 8 | fsuffix | 后缀 | varchar | 50 |  | √ | ' ' | 后缀 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cts_nameconfigformat |  | fentryid |
| 2 | idx_cts_namecfgformat_fid |  | fid |

---

## 姓名文本格式-主表 t_cts_nametextconfig

- **表名称：** 姓名文本格式-主表
- **表名：** t_cts_nametextconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisglobaldefault | 全局默认格式 | bpchar | 1 |  | √ | '0' | 全局默认格式 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fnameconfigid | 姓名单据格式 | int8 | 64 |  | √ | 0 | 姓名单据格式 cts_nameconfigstruct |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fiscountrydefault | 国家地区默认格式 | bpchar | 1 |  | √ | '0' | 国家地区默认格式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cts_nametextconfig |  | fid |
| 2 | idx_cts_nametextconfig |  | fnumber |

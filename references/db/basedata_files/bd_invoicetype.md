# 发票种类-bd_invoicetype

## 发票种类-多语言表 t_bd_invoicetype_l

- **表名称：** 发票种类-多语言表
- **表名：** t_bd_invoicetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 120 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 120 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdesc | 备注 | varchar | 120 |  | √ | ' ' | 备注 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_invoicetype_l_pkey |  | fpkid |
| 2 | idx_bd_invoicetype_l_id |  | fid,flocaleid |

---

## 发票种类-主表 t_bd_invoicetype

- **表名称：** 发票种类-主表
- **表名：** t_bd_invoicetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 发票类型分组 | int8 | 64 |  | √ | 0 | [发票类型分组 bd_invoicetypegroup](../basedata_files/bd_invoicetypegroup.md) |
| 4 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffullname | ffullname | varchar | 50 |  | √ | ' ' |  |
| 7 | ftaxcontrolcode | 发票税控编码 | varchar | 50 |  | √ | ' ' | 发票税控编码 |
| 8 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 9 | fissueiv | 开票 | bpchar | 1 |  | √ | '0' | 开票 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fissystem | 系统预设 | varchar | 30 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 15 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 2 :保存 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fdesc | fdesc | varchar | 50 |  | √ | ' ' |  |
| 18 | freceiveiv | 收票 | bpchar | 1 |  | √ | '0' | 收票 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_invoicetype_pkey |  | fid |
| 2 | idx_bd_invoicetype_num |  | fnumber |

---

## 应用领域-多选基础资料表 t_bd_applicationfield

- **表名称：** 应用领域-多选基础资料表
- **表名：** t_bd_applicationfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 18 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_applicationfield_pkey |  | fpkid |
| 2 | idx_bd_applicationfield_id |  | fid |

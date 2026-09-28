# 行政区划预置数据-bd_admindivision_preset

## 行政区划预置数据-多语言表 t_bd_admindivisionpre_l

- **表名称：** 行政区划预置数据-多语言表
- **表名：** t_bd_admindivisionpre_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 1024 |  | √ | ' ' | 长名称 |
| 4 | fsimplename | fsimplename | varchar | 255 |  | √ | ' ' |  |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_adminpre_l_id |  | fid,flocaleid |
| 2 | pk_bd_admindivisionpre_l |  | fpkid |

---

## 行政区划预置数据-主表 t_bd_admindivisionpre

- **表名称：** 行政区划预置数据-主表
- **表名：** t_bd_admindivisionpre

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fcitynumber | 电话区号 | varchar | 80 |  | √ | ' ' | 电话区号 |
| 6 | fiscity | 城市 | bpchar | 1 |  | √ | '0' | 城市 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 11 | fareacode | 参考码 | varchar | 10 |  | √ | ' ' | 参考码 |
| 12 | fsimplespell | 英文简称 | varchar | 255 |  | √ | ' ' | 英文简称 |
| 13 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fparentid | 上级行政区划 | int8 | 64 |  | √ | 0 | 上级行政区划 |
| 16 | ffullname | 长名称 | varchar | 1024 |  | √ | ' ' | 长名称 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 19 | fcountryid | 所属国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 20 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 22 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 23 | ffullspell | 英文全称 | varchar | 255 |  | √ | ' ' | 英文全称 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | fadmindivisionlvid | 行政级次 | int8 | 64 |  | √ | 0 | 行政级次 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_adminpre_counrynum |  | fnumber,fcountryid |
| 2 | pk_bd_admindivisionpre |  | fid |

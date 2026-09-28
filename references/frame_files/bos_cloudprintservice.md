# 云打印服务-bos_cloudprintservice

## 云打印服务-多语言表 t_bas_cloudprintservice_l

- **表名称：** 云打印服务-多语言表
- **表名：** t_bas_cloudprintservice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_cloudprintservice_l |  | fid,flocaleid |
| 2 | t_bas_cloudprintservice_l_fid_flocaleid_key |  | fid,flocaleid |
| 3 | t_bas_cloudprintservice_l_pkey |  | fpkid |

---

## 云打印服务-主表 t_bas_cloudprintservice

- **表名称：** 云打印服务-主表
- **表名：** t_bas_cloudprintservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | fapproverid | int8 | 64 |  | √ | 0 |  |
| 3 | fforbidstatus | fforbidstatus | bpchar | 1 |  |  | ' ' |  |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | bpchar | 1 |  |  | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatedate | fcreatedate | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmodifydate | fmodifydate | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 10 | fforbiderid | fforbiderid | int8 | 64 |  | √ | 0 |  |
| 11 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 12 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fparentid | 上级 | int8 | 64 |  |  | null | 云打印服务 bos_cloudprintservice |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 17 | ffullname | 长名称 | varchar | 100 |  | √ | ' ' | 长名称 |
| 18 | flongnumber | 长编码 | varchar | 256 |  | √ | ' ' | 长编码 |
| 19 | fservicetype | 服务类型 | bpchar | 1 |  | √ | 'A' | 服务类型,枚举: A :旧服务 B :新服务 |
| 20 | flevel | 级次 | int8 | 64 |  |  | null | 级次 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 24 | fforbiddate | fforbiddate | timestamp | 0 |  |  | null |  |
| 25 | faccountid | 帐套ID | int8 | 64 |  |  | null | 帐套ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_cloudprintservice |  | fnumber |
| 2 | t_bas_cloudprintservice_pkey |  | fid |

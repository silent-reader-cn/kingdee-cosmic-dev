# 云打印机-bos_cloudprinter

## 云打印机-多语言表 t_bas_cloudprinter_l

- **表名称：** 云打印机-多语言表
- **表名：** t_bas_cloudprinter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 256 |  | √ | ' ' | 名称 |
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
| 1 | t_bas_cloudprinter_l_pkey |  | fpkid |
| 2 | idx_bas_cloudprinter_l |  | fid,flocaleid |
| 3 | t_bas_cloudprinter_l_fid_flocaleid_key |  | fid,flocaleid |

---

## 云打印机-主表 t_bas_cloudprinter

- **表名称：** 云打印机-主表
- **表名：** t_bas_cloudprinter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | fapproverid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fforbidstatus | fforbidstatus | bpchar | 1 |  |  | ' ' |  |
| 5 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  |  | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatedate | fcreatedate | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifydate | fmodifydate | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 12 | fforbiderid | fforbiderid | int8 | 64 |  | √ | 0 |  |
| 13 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 14 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 15 | fserviceid | 服务 | int8 | 64 |  |  | null | [云打印服务 bos_cloudprintservice](../frame_files/bos_cloudprintservice.md) |
| 16 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 17 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 名称 | varchar | 256 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 21 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 1 :逐级分配 2 :自由分配 5 :全局共享 6 :管控范围内共享 7 :私有 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  |  | null | 编码 |
| 24 | fprintername | 打印机地址 | varchar | 256 |  | √ | ' ' | 打印机地址 |
| 25 | fforbiddate | fforbiddate | timestamp | 0 |  |  | null |  |
| 26 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_cprinter |  | fnumber |
| 2 | idx_bas_cprinter_fmasterid |  | fmasterid |
| 3 | idx_t_bas_cloudprinter_createorg |  | fcreateorgid |
| 4 | idx_t_bas_cloudprinter_master |  | fmasterid |
| 5 | t_bas_cloudprinter_pkey |  | fid |
| 6 | idx_bas_cprinter_fcreateorgid |  | fcreateorgid |

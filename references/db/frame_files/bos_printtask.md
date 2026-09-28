# 云打印任务-bos_printtask

## 云打印任务-主表 t_bas_printtask

- **表名称：** 云打印任务-主表
- **表名：** t_bas_printtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbsdprinter | 云打印机 | int8 | 64 |  |  | null | [云打印机 bos_cloudprinter](../frame_files/bos_cloudprinter.md) |
| 3 | fapproverid | fapproverid | int8 | 64 |  | √ | 0 |  |
| 4 | fprintstatus | 打印状态 | bpchar | 1 |  | √ | ' ' | 打印状态,枚举: 1 :未打印 2 :打印中 3 :已打印 4 :废弃 |
| 5 | fforbidstatus | fforbidstatus | bpchar | 1 |  |  | ' ' |  |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  |  | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatedate | fcreatedate | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 10 | fprinteraddress | 打印机地址 | varchar | 256 |  | √ | ' ' | 打印机地址 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmodifydate | fmodifydate | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 14 | fcreatetimestamp | 创建日期时间戳 | int8 | 64 |  | √ | 0 | 创建日期时间戳 |
| 15 | fserviceid | 服务名称 | int8 | 64 |  |  | null | [云打印服务 bos_cloudprintservice](../frame_files/bos_cloudprintservice.md) |
| 16 | fcacheid | 缓存Id | varchar | 256 |  | √ | ' ' | 缓存Id |
| 17 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 20 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fcachekey | 缓存配置Key | varchar | 256 |  | √ | ' ' | 缓存配置Key |
| 22 | fprinttype | 打印类型 | varchar | 10 |  | √ | ' ' | 打印类型,枚举: pdf :PDF zpl :ZPL epl :EPL |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 80 |  |  | null | 编码 |
| 25 | ffilepath | 文件地址 | varchar | 256 |  | √ | ' ' | 文件地址 |
| 26 | faccountid | 帐套ID | varchar | 64 |  | √ | ' ' | 帐套ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_printtask_pkey |  | fid |
| 2 | idx_bas_printtask |  | faccountid,fserviceid |

---

## 云打印任务-多语言表 t_bas_printtask_l

- **表名称：** 云打印任务-多语言表
- **表名：** t_bas_printtask_l

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
| 1 | t_bas_printtask_l_fid_flocaleid_key |  | fid,flocaleid |
| 2 | t_bas_printtask_l_pkey |  | fpkid |
| 3 | idx_bas_printtask_l |  | fid,flocaleid |

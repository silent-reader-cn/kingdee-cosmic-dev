# 物理文件属性-plm_plmdc_physical_file

## 物理文件属性-多语言表 t_plmdc_physical_file_l

- **表名称：** 物理文件属性-多语言表
- **表名：** t_plmdc_physical_file_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_physical_file_l_0 |  | fid,flocaleid |
| 2 | pk_plmdc_physical_file_l |  | fpkid |

---

## 物理文件属性-使用范围表 t_plmdc_physical_file_u

- **表名称：** 物理文件属性-使用范围表
- **表名：** t_plmdc_physical_file_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_physical_file_u |  | fdataid,fuseorgid |
| 2 | idx_t_plmdc_physical_file_u_uo |  | fuseorgid |

---

## 物理文件属性-主表 t_plmdc_physical_file

- **表名称：** 物理文件属性-主表
- **表名：** t_plmdc_physical_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | flightfileid | 轻量化文件 | int8 | 64 |  | √ | 0 | 轻量化文件 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fpdffileid | PDF文件 | int8 | 64 |  | √ | 0 | PDF文件 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ffilename | 文件名 | varchar | 50 |  | √ | ' ' | 文件名 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fdownloadurl | 下载路径 | varchar | 300 |  | √ | ' ' | 下载路径 |
| 14 | fthumbnail | 轻量化缩略图 | varchar | 255 |  | √ | ' ' | 轻量化缩略图 |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fpicturefield | 缩略图 | varchar | 255 |  | √ | ' ' | 缩略图 |
| 17 | ffilesize | 物理文件大小 | varchar | 50 |  | √ | ' ' | 物理文件大小 |
| 18 | fpath | 文件路径 | varchar | 200 |  | √ | ' ' | 文件路径 |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 22 | fpicturefield1 | fpicturefield1 | varchar | 255 |  | √ | ' ' |  |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | ffiletype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型 |
| 25 | fhtmlfileid | html文件ID | int8 | 64 |  | √ | 0 | html文件ID |
| 26 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | fstepfileid | step文件 | int8 | 64 |  | √ | 0 | step文件 |
| 28 | ffilebytes | 文件字节数 | int8 | 64 |  | √ | 0 | 文件字节数 |
| 29 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fhash | HASH值 | varchar | 300 |  | √ | ' ' | HASH值 |
| 31 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 32 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plmdc_physical_file_master |  | fmasterid |
| 2 | idx_plmdc_physical_file_number |  | fnumber |
| 3 | idx_t_plmdc_physical_file_createorg |  | fcreateorgid |
| 4 | pk_plmdc_physical_file |  | fid |

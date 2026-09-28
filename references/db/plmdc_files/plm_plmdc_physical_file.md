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
| 1 | idx_t_plmdc_physical_file_u_uo |  | fuseorgid |
| 2 | pk_t_plmdc_physical_file_u |  | fdataid,fuseorgid |

---

## 物理文件属性-主表 t_plmdc_physical_file

- **表名称：** 物理文件属性-主表
- **表名：** t_plmdc_physical_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | flightfileid | 轻量化文件 | int8 | 64 |  | √ | 0 | 轻量化文件 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fstoragetype | 存储类型 | varchar | 50 |  | √ | ' ' | 存储类型,枚举: fileserver :云端存储 minio :本地存储 fileservertransminio :云端转存本地 customcontrol :自定义控件 |
| 7 | fpdffileid | PDF文件 | int8 | 64 |  | √ | 0 | PDF文件 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ffilename | 文件名 | varchar | 50 |  | √ | ' ' | 文件名 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fdownloadurl | 下载路径 | varchar | 300 |  | √ | ' ' | 下载路径 |
| 15 | fthumbnail | 轻量化缩略图 | varchar | 255 |  | √ | ' ' | 轻量化缩略图 |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fpicturefield | 缩略图 | varchar | 255 |  | √ | ' ' | 缩略图 |
| 18 | ffilesize | 物理文件大小 | varchar | 50 |  | √ | ' ' | 物理文件大小 |
| 19 | fpath | 文件路径 | varchar | 200 |  | √ | ' ' | 文件路径 |
| 20 | figesfileid | iges文件 | int8 | 64 |  | √ | 0 | iges文件 |
| 21 | fkingdeebrieffileid | 金蝶简略轻量化ID | int8 | 64 |  | √ | 0 | 金蝶简略轻量化ID |
| 22 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 25 | fpicturefield1 | fpicturefield1 | varchar | 255 |  | √ | ' ' |  |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | ffiletype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型 |
| 28 | ftransferfileid | 转换IID | int8 | 64 |  | √ | 0 | 转换IID |
| 29 | flowercasename | 小写文件名 | varchar | 255 |  | √ | ' ' | 小写文件名 |
| 30 | fhtmlfileid | html文件ID | int8 | 64 |  | √ | 0 | html文件ID |
| 31 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 32 | fstepfileid | step文件 | int8 | 64 |  | √ | 0 | step文件 |
| 33 | ffilebytes | 文件字节数 | int8 | 64 |  | √ | 0 | 文件字节数 |
| 34 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fhash | HASH值 | varchar | 300 |  | √ | ' ' | HASH值 |
| 36 | fuploadoption | 上传的状态 | varchar | 50 |  | √ | ' ' | 上传的状态,枚举: succeed :成功 fail :失败 |
| 37 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 38 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 39 | fkingdeefileid | 金蝶标准轻量化ID | int8 | 64 |  | √ | 0 | 金蝶标准轻量化ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_lowercar_filename |  | flowercasename |
| 2 | idx_t_plmdc_physical_file_master |  | fmasterid |
| 3 | idx_plmdc_physical_file_number |  | fnumber |
| 4 | idx_t_plmdc_physical_file_createorg |  | fcreateorgid |
| 5 | pk_plmdc_physical_file |  | fid |

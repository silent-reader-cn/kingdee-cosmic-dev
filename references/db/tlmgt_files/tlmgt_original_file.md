# 抽取原始文件-tlmgt_original_file

## 抽取原始文件-多语言表 t_tlmgt_original_file_l

- **表名称：** 抽取原始文件-多语言表
- **表名：** t_tlmgt_original_file_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilename | 文件名称 | varchar | 255 |  | √ | ' ' | 文件名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tlmgt_ori_file_l |  | fid |
| 2 | pk_t_tlmgt_original_file_l |  | fpkid |

---

## 抽取原始文件-主表 t_tlmgt_original_file

- **表名称：** 抽取原始文件-主表
- **表名：** t_tlmgt_original_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresourcefiletype | 资源文件类型 | varchar | 64 |  | √ | ' ' | 资源文件类型 |
| 3 | ffileattr | 文件属性 | varchar | 1024 |  | √ | ' ' | 文件属性 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fworddatatype | 词条数据类型 | varchar | 64 |  | √ | ' ' | 词条数据类型 |
| 7 | ffileversion | 文件版本号 | varchar | 128 |  | √ | ' ' | 文件版本号 |
| 8 | fschemeid | 抽取方案 | int8 | 64 |  | √ | 0 | [抽取方案 tlmgt_extract_scheme](../tlmgt_files/tlmgt_extract_scheme.md) |
| 9 | fresourceidentifier | 资源标识 | varchar | 64 |  | √ | ' ' | 资源标识 |
| 10 | fwordtype | 词条类型 | varchar | 64 |  | √ | ' ' | 词条类型 |
| 11 | ffileisv | 文件开发商标识 | varchar | 128 |  | √ | ' ' | 文件开发商标识 |
| 12 | fexecuteno | 执行编号 | varchar | 64 |  | √ | ' ' | 执行编号 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | ffileinherit | 文件继承关系 | varchar | 500 |  | √ | ' ' | 文件继承关系 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fresourcetype | 资源类型 | varchar | 64 |  | √ | ' ' | 资源类型 |
| 17 | ffilename | 文件名称 | varchar | 255 |  | √ | ' ' | 文件名称 |
| 18 | fdomainidentifier | 领域标识 | varchar | 64 |  | √ | ' ' | 领域标识 |
| 19 | ffiledependence | 文件依赖关系 | varchar | 500 |  | √ | ' ' | 文件依赖关系 |
| 20 | ffilecode | 文件编码 | varchar | 128 |  | √ | ' ' | 文件编码 |
| 21 | fmoduleidentifier | 模块标识 | varchar | 64 |  | √ | ' ' | 模块标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tlmgt_original_file |  | fid |
| 2 | idx_t_tlgmt_ori_scope |  | fresourcetype,fdomainidentifier,fmoduleidentifier,fresourceidentifier |
| 3 | idx_t_tlmgt_ori_file |  | ffilecode |

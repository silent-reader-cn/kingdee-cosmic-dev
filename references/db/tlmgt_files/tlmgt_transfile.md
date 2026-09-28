# 翻译文件-tlmgt_transfile

## 翻译文件-主表 t_tlmgt_transfile

- **表名称：** 翻译文件-主表
- **表名：** t_tlmgt_transfile

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 文件名称 | varchar | 255 |  | √ | ' ' | 文件名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ffileattr | 文件属性 | varchar | 1024 |  | √ | ' ' | 文件属性 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffileversion | 文件版本号 | varchar | 128 |  | √ | ' ' | 文件版本号 |
| 7 | ffileisv | 文件开发商标识 | varchar | 128 |  | √ | ' ' | 文件开发商标识 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 32 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | ffileinherit | 文件继承关系 | varchar | 500 |  | √ | ' ' | 文件继承关系 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fresourcetype | 资源类型 | int8 | 64 |  | √ | 0 | [资源类型 tlmgt_resource_type](../tlmgt_files/tlmgt_resource_type.md) |
| 14 | fapp | 所属应用 | varchar | 64 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 15 | fenable | 使用状态 | varchar | 32 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | ffiledependence | 文件依赖关系 | varchar | 500 |  | √ | ' ' | 文件依赖关系 |
| 17 | fnumber | 文件长编码 | varchar | 64 |  | √ | ' ' | 文件长编码 |
| 18 | fcloud | 所属云 | varchar | 64 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 19 | ffilecode | 文件编码 | varchar | 64 |  | √ | ' ' | 文件编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tlmgt_file_cloud |  | fcloud |
| 2 | pk_t_tlmgt_transfile |  | fid |
| 3 | idx_t_tlgmt_file |  | fnumber |
| 4 | idx_t_tlmgt_file_app |  | fapp |

---

## 翻译文件-多语言表 t_tlmgt_transfile_l

- **表名称：** 翻译文件-多语言表
- **表名：** t_tlmgt_transfile_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 文件名称 | varchar | 255 |  | √ | ' ' | 文件名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tlmgt_transfile_l |  | fpkid |
| 2 | idx_t_tlmgt_file_l |  | fid |

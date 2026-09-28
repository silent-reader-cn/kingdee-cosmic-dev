# 实施文档-ippm_catalog

## 实施文档-主表 t_ippm_catalog

- **表名称：** 实施文档-主表
- **表名：** t_ippm_catalog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fseelog | 查看日志 | varchar | 100 |  | √ | ' ' | 查看日志 |
| 4 | fname | 文件名称 | varchar | 200 |  | √ | ' ' | 文件名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fgroupid | 文件夹 | int8 | 64 |  | √ | 0 | [文件夹 ippm_categorygroup](../ippm_files/ippm_categorygroup.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdowntimes | 下载次数 | int4 | 32 |  | √ | 0 | 下载次数 |
| 10 | fsize | 大小 | varchar | 100 |  | √ | ' ' | 大小 |
| 11 | fuserfield | fuserfield | int8 | 64 |  | √ | 0 |  |
| 12 | fviewtimes | 查看次数 | int4 | 32 |  | √ | 0 | 查看次数 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ippm_catalog_gid |  | fgroupid |
| 2 | pk_t_ippm_catalog |  | fid |

---

## 实施文档-多语言表 t_ippm_catalog_l

- **表名称：** 实施文档-多语言表
- **表名：** t_ippm_catalog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 文件名称 | varchar | 200 |  | √ | ' ' | 文件名称 |
| 3 | flocaleid | flocaleid | varchar | 200 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_catalog_l |  | fpkid |

---

## 附件-附件表 t_ippm_impldoc_file

- **表名称：** 附件-附件表
- **表名：** t_ippm_impldoc_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_impldoc_file |  | fid |
| 2 | pk_t_ippm_impldoc_file |  | fpkid |

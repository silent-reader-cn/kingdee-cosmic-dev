# 资源目录-iscx_catalog

## 资源目录-多语言表 t_iscx_res_catalog_l

- **表名称：** 资源目录-多语言表
- **表名：** t_iscx_res_catalog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 150 |  |  | null | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscx_catalog_l |  | fid,flocaleid |
| 2 | pk_t_iscx_res_catalog_l |  | fpkid |

---

## 资源目录-主表 t_iscx_res_catalog

- **表名称：** 资源目录-主表
- **表名：** t_iscx_res_catalog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 4 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 5 | ficon_url | 图标URL | varchar | 255 |  |  | null | 图标URL |
| 6 | flong_number | 长编码 | varchar | 50 |  |  | null | 长编码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fpriority | 顺序号 | int8 | 64 |  |  | null | 顺序号 |
| 9 | fsourceapp | 来源应用 | varchar | 50 |  | √ | ' ' | 来源应用 |
| 10 | fmodifier | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdetails | 解决方案详细信息 | varchar | 255 |  |  | null | 解决方案详细信息 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fdetails_tag | 解决方案详细信息_详情 | text | 0 |  |  | null | 解决方案详细信息_详情 |
| 14 | ftype | 类别 | varchar | 50 |  | √ | ' ' | 类别,枚举: Industry :连接器 System :系统 Module :模块 Scene :场景 Solution :解决方案 Common :公共资源 |
| 15 | fparent | 上级目录 | int8 | 64 |  |  | null | [资源目录 iscx_catalog](../iscx_files/iscx_catalog.md) |
| 16 | fnumber | 编码 | varchar | 30 |  |  | null | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscx_res_catalog_n |  | flong_number |
| 2 | pk_t_iscx_res_catalog |  | fid |

---

## 解决方案关联系统-多选基础资料表 t_iscx_catalog_systems

- **表名称：** 解决方案关联系统-多选基础资料表
- **表名：** t_iscx_catalog_systems

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [资源目录 iscx_catalog](../iscx_files/iscx_catalog.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscx_catalog_systems_fk2 |  | fbasedataid |
| 2 | idx_iscx_catalog_systems_fk |  | fid |
| 3 | pk_t_iscx_catalog_systems |  | fpkid |

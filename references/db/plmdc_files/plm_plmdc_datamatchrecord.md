# 数据源配置匹配记录-plm_plmdc_datamatchrecord

## 匹配物料-多选基础资料表 t_plmdc_matchmatid

- **表名称：** 匹配物料-多选基础资料表
- **表名：** t_plmdc_matchmatid

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料版本 plm_pdm_material_revision](../plmsm_files/plm_pdm_material_revision.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmfc_matchmatid |  | fid |
| 2 | pk_t_plmdc_matchmatid |  | fpkid |

---

## 数据源配置匹配记录-主表 t_plmdc_datamatchrecord

- **表名称：** 数据源配置匹配记录-主表
- **表名：** t_plmdc_datamatchrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fsymboltype | 图符类型 | varchar | 50 |  | √ | 'common' | 图符类型,枚举: common :公共图符 local :本地图符 |
| 4 | fcadtype | 文件类型 | int8 | 64 |  | √ | 0 | [文件类型 plm_plmdc_file_type](../plmdc_files/plm_plmdc_file_type.md) |
| 5 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fcomponentindex | 元器件索引 | int4 | 32 |  | √ | 0 | 元器件索引 |
| 7 | fsymbolpath | 图符路径 | varchar | 255 |  | √ | ' ' | 图符路径 |
| 8 | fsymbolname | 图符名称 | varchar | 255 |  | √ | ' ' | 图符名称 |
| 9 | fcreatedata | fcreatedata | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_datamatchrecord |  | fid |
| 2 | idx_plmdc_datamatchedcord |  | fsymbolname,fsymbolpath |

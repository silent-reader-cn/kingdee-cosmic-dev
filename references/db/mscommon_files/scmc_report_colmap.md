# 报表数据源字段映射-scmc_report_colmap

## 报表数据源字段映射-主表 t_scmc_rpt_colmap

- **表名称：** 报表数据源字段映射-主表
- **表名：** t_scmc_rpt_colmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | freportentity | 字段库实体 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmapinfo_tag | 字段映射信息_详情 | text | 0 |  |  | null | 字段映射信息_详情 |
| 6 | fsysdata | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 7 | fmapinfo | 字段映射信息 | varchar | 1 |  | √ | ' ' | 字段映射信息 |
| 8 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | fsrcentity | 来源实体 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scmc_rpt_colmap |  | fid |
| 2 | idx_t_scmc_rpt_colmap_fnumber |  | fnumber |
| 3 | idx_rpt_colmap_freportentity |  | freportentity |
| 4 | idx_rpt_colmap_fsrcentity |  | fsrcentity |

---

## 报表数据源字段映射-多语言表 t_scmc_rpt_colmap_l

- **表名称：** 报表数据源字段映射-多语言表
- **表名：** t_scmc_rpt_colmap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scmc_rpt_colmap_l |  | fpkid |
| 2 | idx_t_scmc_rpt_colmap_l_id |  | fid,flocaleid |

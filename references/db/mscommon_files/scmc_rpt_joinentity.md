# 报表关联实体配置-scmc_rpt_joinentity

## 报表关联实体配置-主表 t_scmc_rpt_joinentity

- **表名称：** 报表关联实体配置-主表
- **表名：** t_scmc_rpt_joinentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmapinfo | 字段映射信息 | varchar | 1 |  | √ | ' ' | 字段映射信息 |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsqlinfo | sql信息 | varchar | 1 |  | √ | ' ' | sql信息 |
| 6 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | floadtype | 加载策略 | bpchar | 1 |  | √ | '1' | 加载策略,枚举: 1 :推送关联条件 2 :不推送关联条件 3 :超级查询 |
| 8 | frepoentity | 字段库 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fsysdata | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | fmapinfo_tag | 字段映射信息_详情 | text | 0 |  |  | null | 字段映射信息_详情 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | fsqlinfo_tag | sql信息_详情 | text | 0 |  |  | null | sql信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rpt_joinentity_frepo |  | frepoentity |
| 2 | idx_rpt_joinentity_fno |  | fnumber |
| 3 | pk_t_scmc_rpt_joinentity |  | fid |

---

## 报表关联实体配置-多语言表 t_scmc_rpt_joinentity_l

- **表名称：** 报表关联实体配置-多语言表
- **表名：** t_scmc_rpt_joinentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scmc_rpt_joinentity_l |  | fpkid |
| 2 | idx_rpt_joinentity_l_id |  | fid,flocaleid |

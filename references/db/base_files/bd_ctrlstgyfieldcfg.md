# 基础数据管控字段配置-bd_ctrlstgyfieldcfg

## 基础数据管控字段配置-主表 t_bd_ctrlstgyfieldcfg

- **表名称：** 基础数据管控字段配置-主表
- **表名：** t_bd_ctrlstgyfieldcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbasedataid | 基础数据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fisdefaultrule | 默认规则 | bpchar | 1 |  | √ | '0' | 默认规则 |
| 6 | ffielddefaultvalue | 默认值 | varchar | 255 |  | √ | ' ' | 默认值 |
| 7 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 8 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 9 | ffieldcontroltype | 控制方式 | varchar | 50 |  | √ | ' ' | 控制方式,枚举: 1 :留空 2 :默认 3 :携带 |
| 10 | fmanualfield | 手动设置字段规则中可见 | bpchar | 1 |  | √ | '0' | 手动设置字段规则中可见 |
| 11 | fisallowshare | 允许共享 | bpchar | 1 |  | √ | '0' | 允许共享 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fisvisible | 是否可见 | bpchar | 1 |  | √ | '1' | 是否可见 |
| 14 | fisallowupdate | 允许修改 | bpchar | 1 |  | √ | '0' | 允许修改 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fisfieldlock | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 21 | fxkseq | 序列 | int4 | 32 |  | √ | 0 | 序列 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_ctrlstgyfieldcfg_pkey |  | fid |
| 2 | idx_bd_ctrlstgyfieldcfg_data |  | fbasedataid |

---

## 基础数据管控字段配置-多语言表 t_bd_ctrlstgyfieldcfg_l

- **表名称：** 基础数据管控字段配置-多语言表
- **表名：** t_bd_ctrlstgyfieldcfg_l

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
| 1 | idx_bd_ctrlstgyfieldcfg_l_fid |  | fid,flocaleid |
| 2 | t_bd_ctrlstgyfieldcfg_l_pkey |  | fpkid |

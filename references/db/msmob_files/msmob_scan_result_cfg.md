# 扫描结果配置-msmob_scan_result_cfg

## 扫描结果配置-多语言表 t_msmob_scan_result_cfg_l

- **表名称：** 扫描结果配置-多语言表
- **表名：** t_msmob_scan_result_cfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 配置名称 | varchar | 50 |  | √ | ' ' | 配置名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msmob_scan_result_cfg_l |  | fpkid |
| 2 | idx_mob_scan_re_l_id |  | flocaleid,fid |

---

## 技能选择分录关系-子表 t_msmob_skill_entry

- **表名称：** 技能选择分录关系-子表
- **表名：** t_msmob_skill_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdefaultenabled | 默认使用 | bpchar | 1 |  | √ | '0' | 默认使用 |
| 3 | fskilldescription | fskilldescription | varchar | 255 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fskillname | 技能名称 | int8 | 64 |  | √ | 0 | [技能 msmob_skill](../msmob_files/msmob_skill.md) |
| 6 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fispreset | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mob_skill_entry_fk |  | fskillname |
| 2 | pk_t_msmob_skill_entry |  | fentryid |

---

## 扫描结果配置-主表 t_msmob_scan_result_cfg

- **表名称：** 扫描结果配置-主表
- **表名：** t_msmob_scan_result_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 配置名称 | varchar | 50 |  | √ | ' ' | 配置名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fresultpage | 结果页 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fskill_family | 技能族 | int8 | 64 |  | √ | 0 | [技能族 msmob_skill_family](../msmob_files/msmob_skill_family.md) |
| 7 | fcomments | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 配置编码 | varchar | 50 |  | √ | ' ' | 配置编码 |
| 14 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmob_scan_result_cfg |  | fid |
| 2 | idx_msmob_name_nubmer |  | fnumber,fname |

# 共享过滤方案-bos_share_filterscheme

## 共享过滤方案-主表 t_bas_sharefilterscheme

- **表名称：** 共享过滤方案-主表
- **表名：** t_bas_sharefilterscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsharetime | 长日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 长日期 |
| 3 | fschemeid | 方案名称 | varchar | 20 |  | √ | ' ' | [过滤方案 bos_filterscheme](../cts_files/bos_filterscheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_sharefilterscheme_pkey |  | fid |
| 2 | idx_bas_sharefiltersch_schid |  | fschemeid |

---

## 共享用户-多选基础资料表 t_bas_schemeshareusers

- **表名称：** 共享用户-多选基础资料表
- **表名：** t_bas_schemeshareusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fisdefault | fisdefault | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_schemeshareusers_pkey |  | fpkid |
| 2 | idx_bas_schemeshareusers_fid |  | fid |

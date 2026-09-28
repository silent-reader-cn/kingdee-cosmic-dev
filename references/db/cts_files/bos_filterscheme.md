# 过滤方案-bos_filterscheme

## 过滤方案-多语言表 t_bas_filterscheme_l

- **表名称：** 过滤方案-多语言表
- **表名：** t_bas_filterscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 20 |  |  | null |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | fschemeid | fschemeid | varchar | 20 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 方案内容 | varchar | 255 |  | √ | ' ' | 方案内容 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_filterscheme_l_fid_flocaleid_key |  | fid,flocaleid |
| 2 | idx_bas_filterscheme_l_fid |  | fid,flocaleid |
| 3 | t_bas_filterscheme_l_pkey |  | fpkid |

---

## 过滤方案-主表 t_bas_filterscheme

- **表名称：** 过滤方案-主表
- **表名：** t_bas_filterscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 2 | fentryentity | fentryentity | varchar | 50 |  | √ | ' ' |  |
| 3 | fisshare | fisshare | bpchar | 1 |  | √ | '0' |  |
| 4 | fschemeid | fschemeid | varchar | 20 |  | √ | ' ' | id |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fuserid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fnextentryscheme | fnextentryscheme | bpchar | 1 |  | √ | '0' |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fisf7 | 是否f7 | bpchar | 1 |  | √ | '0' | 是否f7 |
| 10 | fschemename | fschemename | varchar | 100 |  | √ | ' ' |  |
| 11 | fisfixed | 全局方案 | bpchar | 1 |  | √ | '0' | 全局方案 |
| 12 | fscheme | fscheme | text | 0 |  |  | null |  |
| 13 | fformid | 绑定表单 | varchar | 36 |  | √ | ' ' | [全局方案表单 globalscheme_form](../mdl_files/globalscheme_form.md) |
| 14 | fisdefault | fisdefault | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fschemeid | fschemeid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_filterscheme_fformid |  | fformid,fuserid |
| 2 | t_bas_filterscheme_pkey |  | fschemeid |

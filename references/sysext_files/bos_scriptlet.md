# 脚本片段-bos_scriptlet

## 脚本片段-主表 t_ks_scriptlet

- **表名称：** 脚本片段-主表
- **表名：** t_ks_scriptlet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 脚本片段分组 bos_scriptlet_group |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fscript_context | 脚本内容 | varchar | 255 |  |  | null | 脚本内容 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftitle | 脚本标题 | varchar | 50 |  |  | null | 脚本标题 |
| 9 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fscript_import_code | 脚本缩写代码 | varchar | 50 |  |  | null | 脚本缩写代码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fscript_context_tag | 脚本内容_详情 | text | 0 |  |  | null | 脚本内容_详情 |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ks_scriptlet_name |  | fname |
| 2 | idx_ks_scriptlet_number |  | fnumber |
| 3 | pk_t_ks_scriptlet |  | fid |

---

## 脚本片段-多语言表 t_ks_scriptlet_l

- **表名称：** 脚本片段-多语言表
- **表名：** t_ks_scriptlet_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 脚本标题 | varchar | 185 |  | √ | ' ' | 脚本标题 |
| 3 | fname | 标题 | varchar | 185 |  | √ | ' ' | 标题 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ks_st_l_fid |  | fid |
| 2 | pk_t_ks_scriptlet_l |  | fpkid |
| 3 | idx_ks_st_l_fname |  | fname |

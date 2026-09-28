# 组织结构历史-bos_org_structure_history

## 组织结构历史-主表 t_org_structure_h

- **表名称：** 组织结构历史-主表
- **表名：** t_org_structure_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisstatsum | 统计汇总 | bpchar | 1 |  | √ | '1' | 统计汇总 |
| 3 | fmodifyorgid | fmodifyorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fyzjorgid | 云之家组织内码 | varchar | 36 |  | √ | ' ' | 云之家组织内码 |
| 5 | fisleaf | 叶子节点 | bpchar | 1 |  | √ | ' ' | 叶子节点 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fyzjparentorgid | 上级云之家组织内码 | varchar | 36 |  | √ | ' ' | 上级云之家组织内码 |
| 11 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fishr | 启用HR | bpchar | 1 |  | √ | ' ' | 启用HR |
| 15 | fsealuptime | 封存日期 | timestamp | 0 |  |  | null | 封存日期 |
| 16 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fparentid | 上级组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | ffullname | 长名称 | varchar | 1024 |  | √ | ' ' | 长名称 |
| 21 | fviewid | 组织视图 | int8 | 64 |  | √ | 0 | [组织视图方案 bos_org_viewschema](../base_files/bos_org_viewschema.md) |
| 22 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 23 | fsortcode | 字符串排序码 | varchar | 50 |  | √ | ' ' | 字符串排序码 |
| 24 | fisctrlunit | 管控单元 | bpchar | 1 |  | √ | '1' | 管控单元 |
| 25 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 26 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 27 | fisfreeze | 封存 | bpchar | 1 |  | √ | ' ' | 封存 |
| 28 | fsortnumber | 排序码 | int8 | 64 |  | √ | 0 | 排序码 |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 31 | fisbizunit | 业务实体 | bpchar | 1 |  | √ | '0' | 业务实体 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_org_structure_h_parent |  | fparentid |
| 2 | idx_org_struct_h_orgviewlnum |  | forgid,fviewid,flongnumber |
| 3 | idx_org_structure_h_time |  | fcreatetime |
| 4 | t_org_structure_h_pkey |  | fid |

---

## 组织结构历史-多语言表 t_org_structure_h_l

- **表名称：** 组织结构历史-多语言表
- **表名：** t_org_structure_h_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 1024 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_org_structure_h_l_pkey |  | fpkid |
| 2 | idx_t_org_structure_h_fid |  | fid,flocaleid |

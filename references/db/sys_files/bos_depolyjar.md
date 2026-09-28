# 热部署-bos_depolyjar

## 热部署-主表 t_meta_ext_jar

- **表名称：** 热部署-主表
- **表名：** t_meta_ext_jar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapp | 所属应用 | varchar | 50 |  | √ | ' ' | [业务应用列表 bos_devp_bizapplist](../devnew_files/bos_devp_bizapplist.md) |
| 3 | flast_modifier | flast_modifier | int8 | 64 |  | √ | 0 |  |
| 4 | fisv | ISV | varchar | 50 |  | √ | ' ' | ISV |
| 5 | fjar | fjar | bytea | 0 |  |  | null |  |
| 6 | fhash | fhash | int8 | 64 |  | √ | 0 |  |
| 7 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 8 | fdescription | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 9 | fenabled | fenabled | bpchar | 1 |  | √ | '1' |  |
| 10 | flast_modified_time | 更新日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 更新日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_ext_jar_pkey |  | fid |
| 2 | idx_meta_ext_fnumber |  | fnumber |
